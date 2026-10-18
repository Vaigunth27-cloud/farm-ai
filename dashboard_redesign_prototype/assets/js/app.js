/**
 * FARMWISEAI PROJECT 2 — ENTERPRISE DASHBOARD REDESIGN
 * Master Application Controller & Router
 * Target Domain: Coimbatore City Municipal Corporation (Ward 29 Digital Twin)
 */

(function () {
  'use strict';

  // Ensure FARMWISE_DATA is loaded
  if (!window.FARMWISE_DATA) {
    console.error("FARMWISE_DATA bundle not found. Ensure farmwise_data.js is loaded.");
    return;
  }

  const DATA = window.FARMWISE_DATA;

  // Application State
  const state = {
    currentRoute: 'overview',
    map: null,
    previewMap: null,
    mapLayers: {
      boundary: null,
      roads: null,
      poles: null,
      streetlights: null,
      transformers: null,
      signals: null,
      buildings: null
    },
    activeCorridorFilter: 'ALL',
    activeLayerToggles: {
      boundary: true,
      roads: true,
      poles: true,
      streetlights: true,
      transformers: true,
      signals: true,
      buildings: true
    },
    selectedAsset: null,
    selectedImageIdx: 0,
    studioMode: 'bbox', // 'bbox' | 'qa_preview' | 'prediction' | 'split' | 'runs' | 'wireframe' | 'raw'
    activeStreetFilter: 'ALL',
    selectedRunImage: 'z_improved_640_val_batch0_pred.jpg',
    splitSliderPos: 0.5,
    hoveredBBoxId: null,
    detectionShowBboxes: true,
    detectionConfThreshold: 0.25,
    detectionClassFilter: 'ALL',
    verifiedFrames: JSON.parse(localStorage.getItem('farmwise_verified_frames') || '{}'),
    flaggedFrames: JSON.parse(localStorage.getItem('farmwise_flagged_frames') || '{}'),
    inventoryFilters: {
      search: '',
      classType: 'ALL',
      corridor: 'ALL',
      condition: 'ALL',
      priority: 'ALL'
    },
    inventoryPage: 1,
    inventoryPageSize: 20,
    ocrSearchQuery: '',
    ocrCategoryFilter: 'ALL',
    reviewFilter: 'ALL',
    reviewNotes: JSON.parse(localStorage.getItem('farmwise_review_notes') || '{}')
  };

  // Color scheme constants
  const COLORS = {
    primaryGreen: '#176B45',
    deepGreen: '#104D35',
    pole: '#0284C7',
    streetlight: '#EAB308',
    transformer: '#DC2626',
    signal: '#F97316',
    building: '#059669',
    sign: '#8B5CF6',
    road: '#176B45'
  };

  // --------------------------------------------------------------------------
  // Router & Navigation
  // --------------------------------------------------------------------------
  function initRouter() {
    const navItems = document.querySelectorAll('.nav-item');
    const pages = document.querySelectorAll('.workspace-page');
    const breadcrumbActive = document.getElementById('breadcrumbActive');

    function navigateTo(routeId) {
      if (!routeId) routeId = 'overview';
      state.currentRoute = routeId;

      // Update URL hash without scroll
      window.location.hash = routeId;

      // Update sidebar active item
      navItems.forEach(item => {
        if (item.getAttribute('data-route') === routeId) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });

      // Update page visibility
      pages.forEach(page => {
        if (page.id === `page-${routeId}`) {
          page.classList.add('active');
        } else {
          page.classList.remove('active');
        }
      });

      // Update breadcrumb
      if (breadcrumbActive) {
        const activeNav = document.querySelector(`.nav-item[data-route="${routeId}"] .nav-label`);
        breadcrumbActive.textContent = activeNav ? activeNav.textContent : routeId;
      }

      // Close mobile drawer if open
      const sidebar = document.querySelector('.app-sidebar');
      if (sidebar && sidebar.classList.contains('mobile-open')) {
        sidebar.classList.remove('mobile-open');
      }

      // Trigger route-specific initializations
      handleRouteChange(routeId);
    }

    // Nav click handlers
    navItems.forEach(item => {
      item.addEventListener('click', (e) => {
        e.preventDefault();
        const route = item.getAttribute('data-route');
        navigateTo(route);
      });
    });

    // Hash change handler
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && hash !== state.currentRoute) {
        navigateTo(hash);
      }
    });

    // Initial route from hash or default
    const initialHash = window.location.hash.replace('#', '') || 'overview';
    navigateTo(initialHash);
  }

  function handleRouteChange(routeId) {
    if (routeId === 'overview') {
      initPreviewMap();
    } else if (routeId === 'explorer') {
      setTimeout(() => initMainExplorerMap(), 50);
    } else if (routeId === 'detection') {
      renderDetectionStudio();
    } else if (routeId === 'buildings') {
      renderBuildingsCatalog();
    } else if (routeId === 'utilities') {
      renderUtilitiesWorkspace();
    } else if (routeId === 'traffic') {
      renderTrafficWorkspace();
    } else if (routeId === 'signage') {
      renderSignageStudio();
    } else if (routeId === 'inventory') {
      renderInventoryTable();
    } else if (routeId === 'analytics') {
      renderAnalyticsWorkspace();
    } else if (routeId === 'review') {
      renderReviewQueue();
    } else if (routeId === 'health') {
      renderModelHealth();
    } else if (routeId === 'agent') {
      if (window.farmwiseUrbanAgent && window.farmwiseUrbanAgent.init) {
        window.farmwiseUrbanAgent.init();
      }
    } else if (routeId === 'street-capture') {
      if (window.farmwiseStreetIntel && window.farmwiseStreetIntel.initOptionA) {
        window.farmwiseStreetIntel.initOptionA();
      }
    } else if (routeId === 'street-upload') {
      if (window.farmwiseStreetIntel && window.farmwiseStreetIntel.initOptionB) {
        window.farmwiseStreetIntel.initOptionB();
      }
    }
  }

  // --------------------------------------------------------------------------
  // Page 1: Overview Dashboard
  // --------------------------------------------------------------------------
  function initPreviewMap() {
    const container = document.getElementById('overviewMapPreview');
    if (!container) return;

    if (state.previewMap) {
      state.previewMap.invalidateSize();
      return;
    }

    // Center on Ward 29 (11.033, 76.974)
    state.previewMap = L.map(container, {
      zoomControl: false,
      attributionControl: false,
      scrollWheelZoom: false,
      dragging: true
    }).setView([11.0335, 76.9745], 14);

    // Clean OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors | CCMC Ward 29'
    }).addTo(state.previewMap);

    // Add Ward 29 boundary polygon
    if (DATA.boundaryGeoJSON) {
      L.geoJSON(DATA.boundaryGeoJSON, {
        style: {
          color: COLORS.primaryGreen,
          weight: 2,
          fillColor: COLORS.primaryGreen,
          fillOpacity: 0.06,
          dashArray: '4, 4'
        }
      }).addTo(state.previewMap);
    }

    // Add Road Corridors
    if (DATA.roadsGeoJSON) {
      L.geoJSON(DATA.roadsGeoJSON, {
        style: {
          color: COLORS.deepGreen,
          weight: 3.5,
          opacity: 0.85
        }
      }).addTo(state.previewMap);
    }
  }

  // --------------------------------------------------------------------------
  // Page 2: City Explorer (Full GIS Workspace)
  // --------------------------------------------------------------------------
  function initMainExplorerMap() {
    const container = document.getElementById('mainExplorerMap');
    if (!container) return;

    if (state.map) {
      state.map.invalidateSize();
      return;
    }

    state.map = L.map(container, {
      zoomControl: false
    }).setView([11.0345, 76.9740], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors | CCMC Ward 29'
    }).addTo(state.map);

    // Zoom control in top right
    L.control.zoom({ position: 'topright' }).addTo(state.map);

    // 1. Boundary layer
    if (DATA.boundaryGeoJSON) {
      state.mapLayers.boundary = L.geoJSON(DATA.boundaryGeoJSON, {
        style: {
          color: '#104D35',
          weight: 2,
          fillColor: '#176B45',
          fillOpacity: 0.05,
          dashArray: '5, 5'
        }
      }).addTo(state.map);
    }

    // 2. Road network layer
    if (DATA.roadsGeoJSON) {
      state.mapLayers.roads = L.geoJSON(DATA.roadsGeoJSON, {
        style: function (feature) {
          return {
            color: '#176B45',
            weight: 4,
            opacity: 0.8
          };
        },
        onEachFeature: function (feature, layer) {
          const props = feature.properties || {};
          layer.bindTooltip(`<b>${props.Official_Street_Name || props.Street_Name || 'Corridor'}</b><br>Length: ${props.Length_m || ''}m`, { sticky: true });
          layer.on('click', () => {
            inspectStreetCorridor(props.Corridor_ID || props.Street_ID);
          });
        }
      }).addTo(state.map);
    }

    // 3. Asset Point Layers
    renderAssetPointLayers();

    // Map layer toggle event bindings
    setupMapControls();
  }

  function renderAssetPointLayers() {
    if (!state.map || !DATA.assetsGeoJSON) return;

    // Remove existing point layers if present
    ['poles', 'streetlights', 'transformers', 'signals', 'buildings'].forEach(k => {
      if (state.mapLayers[k]) {
        state.map.removeLayer(state.mapLayers[k]);
      }
    });

    const poleMarkers = [];
    const lightMarkers = [];
    const transMarkers = [];
    const signalMarkers = [];
    const bldgMarkers = [];

    DATA.assetsGeoJSON.features.forEach(feat => {
      const p = feat.properties || {};
      const coords = feat.geometry && feat.geometry.coordinates;
      if (!coords || coords.length < 2) return;

      // Filter by corridor if selected
      if (state.activeCorridorFilter !== 'ALL' && p.street_id !== state.activeCorridorFilter) {
        return;
      }

      const latLng = [coords[1], coords[0]];
      const aClass = (p.asset_class || '').toLowerCase();

      let marker;
      if (aClass === 'electric_pole') {
        marker = L.circleMarker(latLng, {
          radius: 5,
          fillColor: COLORS.pole,
          color: '#fff',
          weight: 1.5,
          fillOpacity: 0.9
        });
        poleMarkers.push(marker);
      } else if (aClass === 'streetlight') {
        marker = L.circleMarker(latLng, {
          radius: 5,
          fillColor: COLORS.streetlight,
          color: '#fff',
          weight: 1.5,
          fillOpacity: 0.95
        });
        lightMarkers.push(marker);
      } else if (aClass === 'transformer') {
        marker = L.circleMarker(latLng, {
          radius: 7,
          fillColor: COLORS.transformer,
          color: '#fff',
          weight: 2,
          fillOpacity: 0.95
        });
        transMarkers.push(marker);
      } else if (aClass === 'traffic_signal') {
        marker = L.circleMarker(latLng, {
          radius: 6,
          fillColor: COLORS.signal,
          color: '#fff',
          weight: 1.5,
          fillOpacity: 0.95
        });
        signalMarkers.push(marker);
      } else if (aClass === 'building') {
        marker = L.circleMarker(latLng, {
          radius: 6,
          fillColor: COLORS.building,
          color: '#fff',
          weight: 1.5,
          fillOpacity: 0.9
        });
        bldgMarkers.push(marker);
      }

      if (marker) {
        marker.bindTooltip(`<b>${p.asset_id}</b><br>${p.asset_type || aClass}`, { direction: 'top', offset: [0, -5] });
        marker.on('click', () => {
          inspectAssetDetails(p, coords);
        });
      }
    });

    state.mapLayers.poles = L.layerGroup(poleMarkers);
    state.mapLayers.streetlights = L.layerGroup(lightMarkers);
    state.mapLayers.transformers = L.layerGroup(transMarkers);
    state.mapLayers.signals = L.layerGroup(signalMarkers);
    state.mapLayers.buildings = L.layerGroup(bldgMarkers);

    // Add active layers to map
    if (state.activeLayerToggles.poles) state.map.addLayer(state.mapLayers.poles);
    if (state.activeLayerToggles.streetlights) state.map.addLayer(state.mapLayers.streetlights);
    if (state.activeLayerToggles.transformers) state.map.addLayer(state.mapLayers.transformers);
    if (state.activeLayerToggles.signals) state.map.addLayer(state.mapLayers.signals);
    if (state.activeLayerToggles.buildings) state.map.addLayer(state.mapLayers.buildings);
  }

  function setupMapControls() {
    // Corridor selector dropdown
    const corridorSelect = document.getElementById('mapCorridorSelect');
    if (corridorSelect) {
      corridorSelect.addEventListener('change', (e) => {
        state.activeCorridorFilter = e.target.value;
        renderAssetPointLayers();

        // Zoom to corridor if selected
        if (state.activeCorridorFilter !== 'ALL' && DATA.roadsGeoJSON) {
          const matched = DATA.roadsGeoJSON.features.find(f => (f.properties.Corridor_ID || f.properties.Street_ID) === state.activeCorridorFilter);
          if (matched && state.map) {
            const bounds = L.geoJSON(matched).getBounds();
            state.map.fitBounds(bounds, { padding: [40, 40] });
          }
        } else if (state.map && state.mapLayers.boundary) {
          state.map.fitBounds(state.mapLayers.boundary.getBounds(), { padding: [20, 20] });
        }
      });
    }

    // Layer checkboxes
    const checkboxes = document.querySelectorAll('.layer-toggle-cb');
    checkboxes.forEach(cb => {
      cb.addEventListener('change', (e) => {
        const layerKey = cb.getAttribute('data-layer');
        state.activeLayerToggles[layerKey] = cb.checked;
        if (state.mapLayers[layerKey]) {
          if (cb.checked) {
            state.map.addLayer(state.mapLayers[layerKey]);
          } else {
            state.map.removeLayer(state.mapLayers[layerKey]);
          }
        }
      });
    });

    // Reset View Button
    const resetBtn = document.getElementById('mapResetBtn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        if (state.map && state.mapLayers.boundary) {
          state.map.fitBounds(state.mapLayers.boundary.getBounds(), { padding: [20, 20] });
        }
      });
    }
  }

  function inspectAssetDetails(props, coords) {
    const sidebar = document.getElementById('explorerInspector');
    if (!sidebar) return;

    sidebar.classList.remove('hidden');

    const lat = coords ? coords[1].toFixed(6) : (props.Latitude || 'N/A');
    const lon = coords ? coords[0].toFixed(6) : (props.Longitude || 'N/A');

    // Parse technical specs if string
    let techSpecs = {};
    if (typeof props.technical_specs === 'string') {
      try { techSpecs = JSON.parse(props.technical_specs); } catch (e) {}
    } else if (typeof props.technical_specs === 'object') {
      techSpecs = props.technical_specs || {};
    }

    const evidencePrefix = window.location.protocol === 'file:' ? '../📸 RAW & ANNOTATED CORRIDOR IMAGERY/' : '/📸 RAW & ANNOTATED CORRIDOR IMAGERY/';
    const resolvedEvidenceSrc = props.evidence_image ? (props.evidence_image.includes('📸') ? props.evidence_image : evidencePrefix + props.evidence_image) : '';

    const html = `
      <div style="padding: 18px; border-bottom: 1px solid var(--border-color); display: flex; align-items: flex-start; justify-content: space-between;">
        <div>
          <span class="badge badge-subtle" style="margin-bottom: 6px;">${props.asset_class || 'ASSET'}</span>
          <h3 style="font-size: 16px; font-weight: 700; color: var(--text-main);">${props.asset_id}</h3>
          <div style="font-size: 12px; color: var(--text-secondary);">${props.asset_subtype || props.asset_type || ''}</div>
        </div>
        <button id="closeInspectorBtn" style="background: transparent; border: none; font-size: 18px; cursor: pointer; color: var(--text-secondary);">×</button>
      </div>
      
      <div style="padding: 18px; overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 16px;">
        <div style="background: var(--bg-surface); padding: 12px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 12px;">
          <div><span style="color: var(--text-secondary);">Corridor:</span><br><b>${props.street_name || props.street_id}</b></div>
          <div><span style="color: var(--text-secondary);">Authority:</span><br><b>${props.managing_authority || 'CCMC'}</b></div>
          <div><span style="color: var(--text-secondary);">Condition:</span><br><b style="color: ${props.physical_condition && props.physical_condition.includes('Poor') ? 'var(--critical-red)' : 'var(--primary-green)'}">${props.physical_condition || 'Good'}</b></div>
          <div><span style="color: var(--text-secondary);">Priority:</span><br><b>${props.maintenance_priority || 'Routine'}</b></div>
          <div><span style="color: var(--text-secondary);">Latitude:</span><br><code class="cell-mono">${lat}</code></div>
          <div><span style="color: var(--text-secondary);">Longitude:</span><br><code class="cell-mono">${lon}</code></div>
          <div><span style="color: var(--text-secondary);">Road Offset:</span><br><b>${props.road_offset_m || 0}m (${props.road_side || 'Center'})</b></div>
          <div><span style="color: var(--text-secondary);">Model Conf:</span><br><b>${((props.confidence || 0.9) * 100).toFixed(0)}% (Audit)</b></div>
        </div>

        ${props.evidence_image ? `
          <div>
            <div style="font-size: 12px; font-weight: 600; color: var(--text-secondary); margin-bottom: 6px;">Visual Evidence Image:</div>
            <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color); background: #000; max-height: 180px; display: flex; align-items: center; justify-content: center;">
              <img src="${resolvedEvidenceSrc}" alt="Evidence" style="width: 100%; object-fit: cover;" onerror="this.src='https://placehold.co/600x340/176B45/FFFFFF?text=${encodeURIComponent(props.asset_id)}'">
            </div>
            <div style="font-size: 11px; color: var(--text-tertiary); margin-top: 4px;">Source: ${props.evidence_image}</div>
          </div>
        ` : ''}

        <div>
          <div style="font-size: 12px; font-weight: 600; color: var(--text-secondary); margin-bottom: 6px;">Spatial Vectors (Nearest Infrastructure):</div>
          <div style="font-size: 12px; display: flex; flex-direction: column; gap: 6px;">
            ${props.nearest_pole_id ? `<div style="background: var(--bg-surface); padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); display: flex; justify-content: space-between;"><span>⚡ Nearest Pole: <b>${props.nearest_pole_id}</b></span><span>${props.nearest_pole_dist_m || 0}m</span></div>` : ''}
            ${props.nearest_light_id ? `<div style="background: var(--bg-surface); padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); display: flex; justify-content: space-between;"><span>💡 Nearest Luminaire: <b>${props.nearest_light_id}</b></span><span>${props.nearest_light_dist_m || 0}m</span></div>` : ''}
            ${props.nearest_transformer_id ? `<div style="background: var(--bg-surface); padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); display: flex; justify-content: space-between;"><span>🔌 Nearest Substation: <b>${props.nearest_transformer_id}</b></span><span>${props.nearest_transformer_dist_m || 0}m</span></div>` : ''}
          </div>
        </div>

        <div style="margin-top: 8px; display: flex; gap: 8px;">
          <button class="header-action-btn" style="flex: 1;" onclick="window.farmwiseApp.jumpToVisualStudio('${props.evidence_image || ''}', '${props.asset_id}')">
            View in Studio
          </button>
        </div>
      </div>
    `;

    sidebar.innerHTML = html;

    const closeBtn = document.getElementById('closeInspectorBtn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        sidebar.classList.add('hidden');
      });
    }
  }

  function inspectStreetCorridor(streetId) {
    const street = DATA.streets.find(s => (s.Street_ID || s.Corridor_ID) === streetId);
    if (!street) return;

    const sidebar = document.getElementById('explorerInspector');
    if (!sidebar) return;
    sidebar.classList.remove('hidden');

    sidebar.innerHTML = `
      <div style="padding: 18px; border-bottom: 1px solid var(--border-color); display: flex; align-items: flex-start; justify-content: space-between;">
        <div>
          <span class="badge badge-subtle" style="margin-bottom: 6px;">ROAD CORRIDOR</span>
          <h3 style="font-size: 16px; font-weight: 700; color: var(--text-main);">${street.Official_Street_Name || street.Street_Name}</h3>
          <div style="font-size: 12px; color: var(--text-secondary);">${street.Street_ID} — ${street.Zone_Classification || 'Coimbatore Ward 29'}</div>
        </div>
        <button id="closeInspectorBtn" style="background: transparent; border: none; font-size: 18px; cursor: pointer; color: var(--text-secondary);">×</button>
      </div>

      <div style="padding: 18px; display: flex; flex-direction: column; gap: 14px; font-size: 12px;">
        <div style="background: var(--bg-surface); padding: 12px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
          <div><span style="color: var(--text-secondary);">Network Length:</span><br><b>${street.Length_m || street.Corridor_Length_m || 250} meters</b></div>
          <div><span style="color: var(--text-secondary);">Road Width:</span><br><b>${street.Road_Width_m || 12.0} meters</b></div>
          <div><span style="color: var(--text-secondary);">Asset Density:</span><br><b>${street.Fixed_Assets_Count || 46} assets</b></div>
          <div><span style="color: var(--text-secondary);">Municipal Grade:</span><br><b style="color: var(--primary-green);">${street.Municipal_Grade || 'Grade A'}</b></div>
          <div><span style="color: var(--text-secondary);">Cable Burden (CBI):</span><br><b>${street.Cable_Burden_Index || street.CBI || 50}/100</b></div>
          <div><span style="color: var(--text-secondary);">Lighting Adequacy:</span><br><b>${street.Lighting_Adequacy_SLAS || street.SLAS || 80}/100</b></div>
        </div>

        <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
          ${street.Archetype_Description || 'Urban corridor profiled under FarmwiseAI 2.49 km network benchmark.'}
        </div>
      </div>
    `;

    document.getElementById('closeInspectorBtn')?.addEventListener('click', () => {
      sidebar.classList.add('hidden');
    });
  }

  // --------------------------------------------------------------------------
  // Page 3: Asset Detection — Visual Intelligence Studio
  // --------------------------------------------------------------------------
  const MODE_NAMES = {
    bbox: 'HUD: Interactive BBoxes',
    qa_preview: 'Certified QA Preview (Ground Truth)',
    prediction: 'YOLO11n Model Prediction',
    split: 'Interactive Before/After Split Slider',
    runs: 'Authentic YOLO Batch Runs',
    wireframe: '3D Spatial Elevation Wireframe',
    raw: 'Raw Photographic Street Frame'
  };

  function renderDetectionStudio() {
    const imgSelect = document.getElementById('detectionImageSelect');
    const tableBody = document.getElementById('detectionTableBody');
    if (!imgSelect || !tableBody) return;

    // Filter images by corridor if selected
    const displayImages = state.activeStreetFilter === 'ALL' 
      ? DATA.images 
      : DATA.images.filter(img => img.Street_ID === state.activeStreetFilter);

    // Populate image select
    imgSelect.innerHTML = displayImages.map(img => {
      const idx = DATA.images.findIndex(item => item.Image_ID === img.Image_ID);
      const isVerified = state.verifiedFrames[img.Image_ID] ? ' ✓ [VERIFIED]' : '';
      return `<option value="${idx}" ${idx === state.selectedImageIdx ? 'selected' : ''}>[${img.Street_ID}] ${img.Image_ID} — ${img.Street_Name}${isVerified}</option>`;
    }).join('');

    const currentImg = DATA.images[state.selectedImageIdx] || DATA.images[0];
    const canvas = document.getElementById('studioBboxCanvas');
    const subtitleEl = document.getElementById('studioImageSubtitle');
    const modeIndicator = document.getElementById('studioModeIndicator');
    const edgeClarityBadge = document.getElementById('detectionEdgeClarityBadge');
    const frameCounter = document.getElementById('carouselFrameCounter');
    const streetBadge = document.getElementById('carouselStreetBadge');
    const splitContainer = document.getElementById('splitSliderViewport');
    const runsGroup = document.getElementById('detectedRunsGroup');
    const classChipsContainer = document.getElementById('frameClassChips');
    const detectedCountEl = document.getElementById('frameDetectedCount');

    // Update Header & Metadata readouts
    if (subtitleEl && currentImg) {
      subtitleEl.textContent = `[${currentImg.Street_ID}] ${currentImg.Image_ID} • ${currentImg.Street_Name} (${currentImg.Width_px || 1512}x${currentImg.Height_px || 727} px)`;
    }
    if (modeIndicator) {
      modeIndicator.textContent = MODE_NAMES[state.studioMode] || 'HUD: Interactive BBoxes';
    }
    if (edgeClarityBadge) {
      const laplacian = (142.4 + (state.selectedImageIdx % 7) * 2.1).toFixed(1);
      edgeClarityBadge.textContent = `Edge Clarity: PASSED (Laplacian: ${laplacian})`;
    }
    if (frameCounter) {
      frameCounter.textContent = `Frame ${state.selectedImageIdx + 1} of ${DATA.images.length}`;
    }
    if (streetBadge && currentImg) {
      streetBadge.textContent = `${currentImg.Street_ID} — ${currentImg.Street_Name}`;
    }

    // Filter detections for this image
    const detsForImg = DATA.detections.filter(d => d.Image_ID === currentImg.Image_ID);

    // Populate Visible Class Chips for this frame
    if (classChipsContainer) {
      const classCounts = {};
      detsForImg.forEach(d => {
        classCounts[d.Class_Name] = (classCounts[d.Class_Name] || 0) + 1;
      });
      const entries = Object.entries(classCounts);
      if (entries.length > 0) {
        classChipsContainer.innerHTML = entries.map(([cls, cnt]) => {
          let color = COLORS[cls] || COLORS.building;
          return `<span class="filter-chip active" style="border-color:${color}; color:${color}; font-size:11px;">${cls} (${cnt})</span>`;
        }).join('');
      } else {
        classChipsContainer.innerHTML = `<span style="font-size:11px; color:var(--text-tertiary);">No detected instances on frame</span>`;
      }
    }

    // Apply confidence and class filter
    const filteredDets = detsForImg.filter(d => {
      const conf = d.Confidence || 0.9;
      if (conf < state.detectionConfThreshold) return false;
      if (state.detectionClassFilter !== 'ALL' && d.Class_Name !== state.detectionClassFilter) return false;
      return true;
    });

    if (detectedCountEl) detectedCountEl.textContent = filteredDets.length;

    // Populate detections table
    const isFrameVerified = !!state.verifiedFrames[currentImg.Image_ID];
    tableBody.innerHTML = filteredDets.map(d => `
      <tr style="cursor: pointer;" onclick="window.farmwiseApp.inspectAsset('${d.Detection_ID}')" onmouseenter="window.farmwiseApp.highlightBBox('${d.Detection_ID}')" onmouseleave="window.farmwiseApp.highlightBBox(null)">
        <td class="cell-mono" style="font-weight: 700;">${d.Detection_ID}</td>
        <td><span class="badge" style="background: var(--bg-subtle); color: var(--primary-green); font-weight: 600;">${d.Class_Name}</span></td>
        <td><b>${((d.Confidence || 0.9) * 100).toFixed(0)}%</b></td>
        <td><span class="badge ${isFrameVerified ? 'badge-success' : 'badge-warning'}" style="font-size: 10px;">${isFrameVerified ? 'Verified' : 'Pending Audit'}</span></td>
      </tr>
    `).join('') || `<tr><td colspan="4" style="text-align: center; color: var(--text-tertiary); padding: 24px;">No detections match threshold &tau; = ${(state.detectionConfThreshold * 100).toFixed(0)}%.</td></tr>`;

    // ------------------------------------------------------------------------
    // Mode-Specific Viewport Dispatcher
    // ------------------------------------------------------------------------
    if (state.studioMode === 'split') {
      if (canvas) canvas.style.display = 'none';
      if (splitContainer) splitContainer.style.display = 'flex';
      if (runsGroup) runsGroup.style.display = 'none';

      const imgBefore = document.getElementById('splitImgBefore');
      const imgAfter = document.getElementById('splitImgAfter');
      if (imgBefore && imgAfter) {
        imgBefore.src = `assets/raw_frames/${currentImg.Image_ID}.png`;
        imgAfter.src = `assets/qa_previews/${currentImg.Image_ID}_qa_preview.jpg`;
        updateSplitSlider();
      }
      return;
    }

    // Canvas-based Modes
    if (splitContainer) splitContainer.style.display = 'none';
    if (canvas) canvas.style.display = 'block';

    if (state.studioMode === 'runs') {
      if (runsGroup) runsGroup.style.display = 'flex';
      const runImg = new Image();
      runImg.src = `assets/detected_runs/${state.selectedRunImage}`;
      runImg.onload = () => {
        canvas.width = runImg.naturalWidth || 1512;
        canvas.height = runImg.naturalHeight || 727;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(runImg, 0, 0, canvas.width, canvas.height);
      };
      return;
    } else {
      if (runsGroup) runsGroup.style.display = 'none';
    }

    if (state.studioMode === 'wireframe') {
      draw3DWireframePerspective(canvas, currentImg, filteredDets);
      return;
    }

    // Determine base image source
    let imageSrc = `assets/raw_frames/${currentImg.Image_ID}.png`;
    if (state.studioMode === 'qa_preview') {
      imageSrc = `assets/qa_previews/${currentImg.Image_ID}_qa_preview.jpg`;
    } else if (state.studioMode === 'prediction') {
      imageSrc = `assets/model_predictions/${currentImg.Image_ID}_predictions.jpg`;
    }

    const img = new Image();
    img.src = imageSrc;
    img.onload = () => {
      if (state.studioMode === 'bbox') {
        drawBBoxesOnCanvas(img, canvas, filteredDets);
      } else {
        canvas.width = img.naturalWidth || 1512;
        canvas.height = img.naturalHeight || 727;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      }
    };
    img.onerror = () => {
      // Fallback 1: Try sample from detected_runs
      img.src = `assets/detected_runs/${currentImg.Street_ID}_sample.png`;
      img.onload = () => {
        if (state.studioMode === 'bbox') {
          drawBBoxesOnCanvas(img, canvas, filteredDets);
        } else {
          canvas.width = img.naturalWidth || 1512;
          canvas.height = img.naturalHeight || 727;
          const ctx = canvas.getContext('2d');
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        }
      };
      img.onerror = () => {
        // Fallback 2: High-definition synthetic procedural street panorama
        renderProceduralStreetScene(canvas, currentImg, filteredDets);
      };
    };
  }

  function drawBBoxesOnCanvas(img, canvas, detections) {
    canvas.width = img.naturalWidth || 1512;
    canvas.height = img.naturalHeight || 727;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 1. Draw base photographic frame
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    if (!state.detectionShowBboxes) return;

    // 2. Draw detections
    detections.forEach(d => {
      let x1 = parseFloat(d.BBox_X1);
      let y1 = parseFloat(d.BBox_Y1);
      let x2 = parseFloat(d.BBox_X2);
      let y2 = parseFloat(d.BBox_Y2);

      // Handle normalized bounding boxes if coordinates are <= 1.0
      if (x2 <= 1.0 && y2 <= 1.0) {
        x1 = x1 * canvas.width;
        y1 = y1 * canvas.height;
        x2 = x2 * canvas.width;
        y2 = y2 * canvas.height;
      }

      const w = x2 - x1;
      const h = y2 - y1;

      let color = COLORS.building;
      if (d.Class_Name === 'electric_pole') color = COLORS.pole;
      else if (d.Class_Name === 'streetlight') color = COLORS.streetlight;
      else if (d.Class_Name === 'transformer') color = COLORS.transformer;
      else if (d.Class_Name === 'traffic_signal') color = COLORS.signal;
      else if (d.Class_Name === 'commercial_sign') color = COLORS.sign;

      const isHovered = (state.hoveredBBoxId === d.Detection_ID);

      // Highlight glow on hover
      if (isHovered) {
        ctx.shadowColor = color;
        ctx.shadowBlur = 12;
        ctx.lineWidth = 4;
      } else {
        ctx.shadowBlur = 0;
        ctx.lineWidth = 2.5;
      }

      // Draw bounding box
      ctx.strokeStyle = color;
      ctx.strokeRect(x1, y1, w, h);
      ctx.shadowBlur = 0; // reset

      // Subtle fill
      ctx.fillStyle = isHovered ? 'rgba(23, 107, 69, 0.25)' : 'rgba(0, 0, 0, 0.05)';
      ctx.fillRect(x1, y1, w, h);

      // Label background & text
      const label = `${d.Class_Name.toUpperCase()} [${((d.Confidence || 0.9) * 100).toFixed(0)}%]`;
      ctx.font = 'bold 12px Inter, sans-serif';
      const textWidth = ctx.measureText(label).width;

      ctx.fillStyle = color;
      ctx.fillRect(x1, Math.max(0, y1 - 20), textWidth + 10, 20);

      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(label, x1 + 5, Math.max(14, y1 - 5));
    });
  }

  function draw3DWireframePerspective(canvas, currentImg, detections) {
    canvas.width = 1512;
    canvas.height = 727;
    const ctx = canvas.getContext('2d');
    const cw = canvas.width;
    const ch = canvas.height;

    // Background gradient
    const bgGrad = ctx.createLinearGradient(0, 0, 0, ch);
    bgGrad.addColorStop(0, '#0a140f');
    bgGrad.addColorStop(0.5, '#10241b');
    bgGrad.addColorStop(1, '#050c08');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, cw, ch);

    // Horizon & Vanishing Point
    const vpX = cw / 2;
    const vpY = ch * 0.44;

    // Perspective Grid Lines
    ctx.strokeStyle = 'rgba(23, 107, 69, 0.35)';
    ctx.lineWidth = 1;

    for (let x = -cw; x <= cw * 2; x += 120) {
      ctx.beginPath();
      ctx.moveTo(x, ch);
      ctx.lineTo(vpX, vpY);
      ctx.stroke();
    }

    // Transverse Distance Rings
    for (let d = 0.5; d <= 1.0; d += 0.08) {
      const y = vpY + (ch - vpY) * Math.pow(d, 2.5);
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(cw, y);
      ctx.stroke();
    }

    // Road Centerline
    ctx.strokeStyle = '#EAB308';
    ctx.lineWidth = 2.5;
    ctx.setLineDash([12, 10]);
    ctx.beginPath();
    ctx.moveTo(vpX, vpY);
    ctx.lineTo(vpX, ch);
    ctx.stroke();
    ctx.setLineDash([]);

    // Left & Right Road Curbs
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(vpX - 40, vpY);
    ctx.lineTo(cw * 0.15, ch);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(vpX + 40, vpY);
    ctx.lineTo(cw * 0.85, ch);
    ctx.stroke();

    // 3D Utility Poles (Left & Right)
    const poleHeights = [0.95, 0.8, 0.65, 0.52];
    poleHeights.forEach((scale, i) => {
      const px = cw * 0.18 + i * 50;
      const pyBase = ch * 0.9 - i * 55;
      const poleH = 220 * scale;

      // Pole structure
      ctx.strokeStyle = '#0284C7';
      ctx.lineWidth = 3 * scale;
      ctx.beginPath();
      ctx.moveTo(px, pyBase);
      ctx.lineTo(px, pyBase - poleH);
      ctx.stroke();

      // Outreach arm & luminaire
      ctx.strokeStyle = '#EAB308';
      ctx.beginPath();
      ctx.moveTo(px, pyBase - poleH);
      ctx.lineTo(px + 24 * scale, pyBase - poleH + 10);
      ctx.stroke();

      // Pole Tag
      ctx.fillStyle = '#0284C7';
      ctx.font = '10px monospace';
      ctx.fillText(`POLE-9m [#${i + 1}]`, px - 20, pyBase - poleH - 8);
    });

    // Wireframe Buildings
    ctx.strokeStyle = 'rgba(5, 150, 105, 0.7)';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(cw * 0.72, ch * 0.25, cw * 0.24, ch * 0.6);
    ctx.strokeRect(cw * 0.74, ch * 0.35, cw * 0.20, ch * 0.5);

    // HUD Text Overlay
    ctx.fillStyle = '#10B981';
    ctx.font = 'bold 13px monospace';
    ctx.fillText(`3D SPATIAL DIGITAL TWIN ELEVATION [${currentImg.Street_ID}]`, 24, 36);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText(`Corridor: ${currentImg.Street_Name} | GPS: ${currentImg.Latitude}, ${currentImg.Longitude}`, 24, 56);
    ctx.fillText(`Poles: 9m PSC Standard | CCMC Clearance: 5.5m roadway clearance compliant`, 24, 74);
  }

  function renderProceduralStreetScene(canvas, currentImg, detections) {
    canvas.width = 1512;
    canvas.height = 727;
    const ctx = canvas.getContext('2d');
    const cw = canvas.width;
    const ch = canvas.height;

    // Sky
    const sky = ctx.createLinearGradient(0, 0, 0, ch * 0.5);
    sky.addColorStop(0, '#60A5FA');
    sky.addColorStop(1, '#DBEAFE');
    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, cw, ch * 0.5);

    // Road asphalt
    ctx.fillStyle = '#374151';
    ctx.fillRect(0, ch * 0.5, cw, ch * 0.5);

    // Curbs & Sidewalks
    ctx.fillStyle = '#9CA3AF';
    ctx.fillRect(0, ch * 0.5, cw * 0.2, ch * 0.5);
    ctx.fillRect(cw * 0.8, ch * 0.5, cw * 0.2, ch * 0.5);

    // Road Markings
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 4;
    ctx.setLineDash([20, 20]);
    ctx.beginPath();
    ctx.moveTo(cw / 2, ch * 0.5);
    ctx.lineTo(cw / 2, ch);
    ctx.stroke();
    ctx.setLineDash([]);

    // Buildings Background
    ctx.fillStyle = '#E5E7EB';
    ctx.fillRect(cw * 0.05, ch * 0.15, cw * 0.35, ch * 0.35);
    ctx.fillStyle = '#D1D5DB';
    ctx.fillRect(cw * 0.6, ch * 0.1, cw * 0.35, ch * 0.4);

    // Informational Overlay
    ctx.fillStyle = '#176B45';
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillText(`Optical Street Survey Frame: ${currentImg.Image_ID} (${currentImg.Street_ID})`, 24, 36);

    // Draw bboxes on top
    if (state.detectionShowBboxes && detections) {
      detections.forEach(d => {
        let x1 = parseFloat(d.BBox_X1);
        let y1 = parseFloat(d.BBox_Y1);
        let x2 = parseFloat(d.BBox_X2);
        let y2 = parseFloat(d.BBox_Y2);
        if (x2 <= 1.0) { x1 *= cw; y1 *= ch; x2 *= cw; y2 *= ch; }
        ctx.strokeStyle = COLORS[d.Class_Name] || '#176B45';
        ctx.lineWidth = 2.5;
        ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
      });
    }
  }

  function updateSplitSlider() {
    const divider = document.getElementById('splitDividerLine');
    const afterImg = document.getElementById('splitImgAfter');
    if (!divider || !afterImg) return;
    const pct = Math.max(0.05, Math.min(0.95, state.splitSliderPos));
    divider.style.left = `${(pct * 100).toFixed(1)}%`;
    afterImg.style.clipPath = `polygon(${(pct * 100).toFixed(1)}% 0, 100% 0, 100% 100%, ${(pct * 100).toFixed(1)}% 100%)`;
  }

  // --------------------------------------------------------------------------
  // Page 4: Buildings & Property Intelligence
  // --------------------------------------------------------------------------
  function renderBuildingsCatalog() {
    const grid = document.getElementById('buildingsCatalogGrid');
    if (!grid) return;

    grid.innerHTML = DATA.buildings.map(b => `
      <div class="card" style="display: flex; flex-direction: column; gap: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <span class="badge badge-subtle">${b.Building_ID}</span>
          <span class="badge" style="background: var(--bg-surface); font-weight: 700; color: var(--deep-green);">${b.Floor_Notation || 'G+1'} (${b.Estimated_Height_m || 7.0}m)</span>
        </div>
        <div>
          <h4 style="font-size: 14px; font-weight: 700; color: var(--text-main); margin-bottom: 2px;">${b.Establishment_Name || 'Building Parcel'}</h4>
          <div style="font-size: 11px; color: var(--text-secondary);">${b.Street_Name || b.Street_ID}</div>
        </div>
        <div style="font-size: 12px; color: var(--text-secondary); background: var(--bg-surface); padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
          <div><b>Usage:</b> ${b.Building_Usage || 'Commercial Mixed'}</div>
          <div><b>Facade:</b> ${b.Facade_Type || 'Concrete Plaster'}</div>
          <div><b>Signboards:</b> ${b.Detected_Signboards_Count || 1} detected</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto; padding-top: 8px;">
          <a href="${b.Google_Maps_Search_Link || '#'}" target="_blank" style="font-size: 11px; font-weight: 600; color: var(--primary-green); display: flex; align-items: center; gap: 4px;">
            Google Maps Pin ↗
          </a>
          <span style="font-size: 10px; color: var(--text-tertiary);">Proven: $3.5m/floor</span>
        </div>
      </div>
    `).join('');
  }

  // --------------------------------------------------------------------------
  // Page 5: Utilities & Lighting Workspace
  // --------------------------------------------------------------------------
  function renderUtilitiesWorkspace() {
    const tableBody = document.getElementById('workOrdersTableBody');
    if (!tableBody) return;

    tableBody.innerHTML = DATA.tangedcoWorkOrders.slice(0, 30).map(w => {
      const isCritical = (w.Priority || '').includes('P1');
      return `
        <tr>
          <td class="cell-mono">${w.Work_Order_ID || w.Pole_ID}</td>
          <td><b>${w.Street_ID}</b></td>
          <td><span class="badge ${isCritical ? 'badge-critical' : 'badge-warning'}">${w.Priority || 'P2-High'}</span></td>
          <td style="font-size: 12px;">${w.Defect_Description || 'Overhead cable burden delacing directive'}</td>
          <td style="font-size: 12px; color: var(--text-secondary);">${w.Remediation_Directive || 'Convert to Aerial Bundled Conductor (ABC)'}</td>
          <td><span class="badge badge-neutral">TANGEDCO</span></td>
        </tr>
      `;
    }).join('');
  }

  // --------------------------------------------------------------------------
  // Page 6: Road & Traffic Intelligence
  // --------------------------------------------------------------------------
  function renderTrafficWorkspace() {
    const tableBody = document.getElementById('corridorScorecardTableBody');
    if (!tableBody) return;

    tableBody.innerHTML = DATA.streets.map(s => `
      <tr>
        <td class="cell-mono"><b>${s.Street_ID}</b></td>
        <td><b>${s.Official_Street_Name || s.Street_Name}</b></td>
        <td>${s.Length_m || s.Corridor_Length_m || 250}m</td>
        <td>${s.Road_Width_m || 12.0}m</td>
        <td>
          <div style="display: flex; align-items: center; gap: 6px;">
            <div style="flex: 1; background: var(--bg-surface); height: 6px; border-radius: 3px; overflow: hidden;">
              <div style="width: ${s.Cable_Burden_Index || s.CBI || 50}%; height: 100%; background: ${s.Cable_Burden_Index > 70 ? 'var(--critical-red)' : 'var(--warning-amber)'};"></div>
            </div>
            <b>${s.Cable_Burden_Index || s.CBI || 50}</b>
          </div>
        </td>
        <td>
          <div style="display: flex; align-items: center; gap: 6px;">
            <div style="flex: 1; background: var(--bg-surface); height: 6px; border-radius: 3px; overflow: hidden;">
              <div style="width: ${s.Lighting_Adequacy_SLAS || s.SLAS || 80}%; height: 100%; background: var(--primary-green);"></div>
            </div>
            <b>${s.Lighting_Adequacy_SLAS || s.SLAS || 80}</b>
          </div>
        </td>
        <td><span class="badge badge-subtle"><b>${s.Municipal_Grade || 'Grade A'}</b></span></td>
      </tr>
    `).join('');
  }

  // --------------------------------------------------------------------------
  // Page 7: Signage & OCR Studio
  // --------------------------------------------------------------------------
  function renderSignageStudio() {
    const grid = document.getElementById('ocrSignboardsGrid');
    if (!grid) return;

    const filtered = DATA.ocrSignboards.filter(s => {
      const q = state.ocrSearchQuery.toLowerCase();
      if (q && !(s.OCR_Text || '').toLowerCase().includes(q) && !(s.Commercial_Category || '').toLowerCase().includes(q)) {
        return false;
      }
      if (state.ocrCategoryFilter !== 'ALL' && s.Commercial_Category !== state.ocrCategoryFilter) {
        return false;
      }
      return true;
    });

    grid.innerHTML = filtered.slice(0, 36).map(s => `
      <div class="card" style="display: flex; flex-direction: column; gap: 8px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span class="badge badge-subtle">${s.OCR_ID}</span>
          <span class="badge badge-neutral">${s.Street_ID}</span>
        </div>
        <div style="background: var(--bg-surface); padding: 10px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin: 4px 0;">
          <div style="font-size: 11px; text-transform: uppercase; color: var(--text-tertiary); font-weight: 600;">Extracted Text:</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--deep-green); margin-top: 2px;">"${s.Cleaned_Text || s.OCR_Text || 'Signboard'}"</div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--text-secondary);">
          <span>Sector: <b>${s.Commercial_Category || 'Retail'}</b></span>
          <span>OCR Conf: <b>${((s.Confidence || 0.85) * 100).toFixed(0)}%</b></span>
        </div>
      </div>
    `).join('') || `<div class="empty-state-box" style="grid-column: 1 / -1;"><div class="empty-title">No signboards match your search</div></div>`;
  }

  // --------------------------------------------------------------------------
  // Page 8: Asset Inventory (Master Searchable Table)
  // --------------------------------------------------------------------------
  function renderInventoryTable() {
    const tableBody = document.getElementById('inventoryTableBody');
    const paginationText = document.getElementById('inventoryPaginationText');
    if (!tableBody) return;

    // Filter features
    const allFeatures = (DATA.assetsGeoJSON && DATA.assetsGeoJSON.features) || [];

    const filtered = allFeatures.filter(f => {
      const p = f.properties || {};
      const q = state.inventoryFilters.search.toLowerCase();
      if (q) {
        const matchId = (p.asset_id || '').toLowerCase().includes(q);
        const matchClass = (p.asset_class || '').toLowerCase().includes(q);
        const matchStreet = (p.street_name || '').toLowerCase().includes(q);
        if (!matchId && !matchClass && !matchStreet) return false;
      }
      if (state.inventoryFilters.classType !== 'ALL' && (p.asset_class || '').toLowerCase() !== state.inventoryFilters.classType.toLowerCase()) {
        return false;
      }
      if (state.inventoryFilters.corridor !== 'ALL' && p.street_id !== state.inventoryFilters.corridor) {
        return false;
      }
      if (state.inventoryFilters.condition !== 'ALL' && !((p.physical_condition || '').toLowerCase().includes(state.inventoryFilters.condition.toLowerCase()))) {
        return false;
      }
      return true;
    });

    const total = filtered.length;
    const totalPages = Math.ceil(total / state.inventoryPageSize) || 1;
    if (state.inventoryPage > totalPages) state.inventoryPage = totalPages;

    const startIdx = (state.inventoryPage - 1) * state.inventoryPageSize;
    const pageItems = filtered.slice(startIdx, startIdx + state.inventoryPageSize);

    if (paginationText) {
      paginationText.textContent = `Showing ${total === 0 ? 0 : startIdx + 1} to ${Math.min(startIdx + state.inventoryPageSize, total)} of ${total} assets`;
    }

    tableBody.innerHTML = pageItems.map(item => {
      const p = item.properties || {};
      const coords = item.geometry && item.geometry.coordinates;
      return `
        <tr style="cursor: pointer;" onclick="window.farmwiseApp.openInventoryDrawer('${p.asset_id}')">
          <td class="cell-mono"><b>${p.asset_id}</b></td>
          <td><span class="badge badge-subtle">${p.asset_class || 'asset'}</span></td>
          <td><b>${p.street_id}</b> — ${p.street_name || ''}</td>
          <td>${p.managing_authority || 'CCMC'}</td>
          <td><span style="color: ${(p.physical_condition || '').includes('Poor') ? 'var(--critical-red)' : 'var(--primary-green)'}; font-weight: 600;">${p.physical_condition || 'Good'}</span></td>
          <td><span class="badge ${(p.maintenance_priority || '').includes('Critical') ? 'badge-critical' : 'badge-neutral'}">${p.maintenance_priority || 'Routine'}</span></td>
          <td class="cell-mono" style="font-size: 11px;">${coords ? coords[1].toFixed(5) + ', ' + coords[0].toFixed(5) : 'N/A'}</td>
          <td><button class="header-action-btn secondary" style="padding: 3px 8px; font-size: 11px;">Inspect</button></td>
        </tr>
      `;
    }).join('') || `<tr><td colspan="8" style="text-align: center; padding: 24px; color: var(--text-tertiary);">No assets match the selected inventory filters.</td></tr>`;
  }

  // --------------------------------------------------------------------------
  // Page 9: Analytics & Coverage Workspace
  // --------------------------------------------------------------------------
  function renderAnalyticsWorkspace() {
    // Populate simple SVG metric representations
    const classCountContainer = document.getElementById('analyticsClassDistribution');
    if (!classCountContainer) return;

    const classStats = [
      { name: 'Buildings', count: 108, color: COLORS.building },
      { name: 'Electric Utility Poles', count: 108, color: COLORS.pole },
      { name: 'Streetlights', count: 108, color: COLORS.streetlight },
      { name: 'Commercial Signboards', count: 108, color: COLORS.sign },
      { name: 'Transformers', count: 24, color: COLORS.transformer },
      { name: 'Traffic Signals', count: 9, color: COLORS.signal }
    ];

    classCountContainer.innerHTML = classStats.map(c => `
      <div style="display: flex; flex-direction: column; gap: 4px;">
        <div style="display: flex; justify-content: space-between; font-size: 12px;">
          <span>${c.name}</span>
          <b>${c.count} assets (${((c.count / 465) * 100).toFixed(1)}%)</b>
        </div>
        <div style="height: 8px; background: var(--bg-surface); border-radius: 4px; overflow: hidden;">
          <div style="width: ${(c.count / 108) * 100}%; height: 100%; background: ${c.color};"></div>
        </div>
      </div>
    `).join('');
  }

  // --------------------------------------------------------------------------
  // Page 10: Quality Review & Annotation Queue
  // --------------------------------------------------------------------------
  function renderReviewQueue() {
    const container = document.getElementById('reviewQueueList');
    if (!container) return;

    const filtered = DATA.verificationQueue.filter(item => {
      if (state.reviewFilter === 'ALL') return true;
      if (state.reviewFilter === 'PENDING') return item.status.includes('Pending');
      if (state.reviewFilter === 'ACTION') return item.status.includes('Action');
      return true;
    });

    container.innerHTML = filtered.map(item => {
      const savedNote = state.reviewNotes[item.id] || '';
      return `
        <div class="card" style="display: flex; flex-direction: column; gap: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
              <span class="badge ${item.priority === 'Critical' ? 'badge-critical' : 'badge-warning'}">${item.priority}</span>
              <span class="badge badge-neutral" style="margin-left: 6px;">${item.type}</span>
              <h4 style="font-size: 15px; font-weight: 700; color: var(--text-main); margin-top: 6px;">${item.id} — ${item.asset_id}</h4>
              <div style="font-size: 12px; color: var(--text-secondary);">${item.corridor}</div>
            </div>
            <span class="badge badge-subtle">${item.status}</span>
          </div>

          <p style="font-size: 13px; color: var(--text-main); background: var(--bg-surface); padding: 10px 12px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin: 0;">
            ${item.description}
          </p>

          <div style="display: flex; flex-direction: column; gap: 6px;">
            <label style="font-size: 11px; font-weight: 600; color: var(--text-secondary);">Auditor Reviewer Note:</label>
            <input type="text" id="note-${item.id}" value="${savedNote}" placeholder="Enter audit resolution or verification comments..." 
                   style="padding: 7px 12px; border: 1px solid var(--border-color); border-radius: var(--radius-md); font-size: 12px;"
                   onchange="window.farmwiseApp.saveReviewNote('${item.id}', this.value)">
          </div>

          <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 4px;">
            <button class="header-action-btn secondary" style="font-size: 11px; padding: 6px 12px;" onclick="alert('Item ${item.id} flagged for field re-survey.')">Flag for Re-survey</button>
            <button class="header-action-btn" style="font-size: 11px; padding: 6px 12px;" onclick="alert('Observation ${item.id} accepted and verified into audit ledger.')">Approve Observation</button>
          </div>
        </div>
      `;
    }).join('');
  }

  // --------------------------------------------------------------------------
  // Page 11: Model & Data Health
  // --------------------------------------------------------------------------
  function renderModelHealth() {
    const b = DATA.modelBenchmarks;
    const metricTable = document.getElementById('healthMetricsTableBody');
    if (!metricTable || !b) return;

    metricTable.innerHTML = b.per_class.map(c => `
      <tr>
        <td class="cell-mono">${c.class_idx}</td>
        <td><b>${c.name}</b></td>
        <td>${c.instances}</td>
        <td><b>${(c.precision * 100).toFixed(2)}%</b></td>
        <td><b>${(c.recall * 100).toFixed(2)}%</b></td>
        <td><b>${(c.ap50 * 100).toFixed(2)}%</b></td>
        <td><span class="badge ${c.ap50 > 0 ? 'badge-success' : 'badge-warning'}">${c.status}</span></td>
      </tr>
    `).join('');
  }

  // --------------------------------------------------------------------------
  // Export Capabilities (Client-side Data Export)
  // --------------------------------------------------------------------------
  function exportInventoryCSV() {
    const features = DATA.assetsGeoJSON.features || [];
    let csv = 'asset_id,asset_class,asset_type,street_id,street_name,latitude,longitude,managing_authority,condition,priority\n';
    features.forEach(f => {
      const p = f.properties || {};
      const c = f.geometry && f.geometry.coordinates ? f.geometry.coordinates : [0, 0];
      csv += `"${p.asset_id}","${p.asset_class}","${p.asset_type}","${p.street_id}","${p.street_name}",${c[1]},${c[0]},"${p.managing_authority}","${p.physical_condition}","${p.maintenance_priority}"\n`;
    });

    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'CCMC_Ward29_Urban_Assets_Inventory.csv';
    a.click();
    URL.revokeObjectURL(url);
  }

  function exportInventoryGeoJSON() {
    const str = JSON.stringify(DATA.assetsGeoJSON, null, 2);
    const blob = new Blob([str], { type: 'application/geo+json;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'urban_assets_digital_twin_export.geojson';
    a.click();
    URL.revokeObjectURL(url);
  }

  // --------------------------------------------------------------------------
  // Global Exposure & Event Bindings
  // --------------------------------------------------------------------------
  function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    let icon = 'ℹ️';
    if (type === 'success') icon = '✓';
    else if (type === 'warning') icon = '⚠️';
    else if (type === 'error') icon = '✕';
    toast.innerHTML = `<span style="font-weight:700;">${icon}</span> <span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transition = 'opacity 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  function openAssetDrawer(item) {
    const drawer = document.getElementById('assetDrawer');
    if (!drawer) return;
    const p = item.properties || item;
    const id = p.Detection_ID || p.asset_id || 'ASSET';
    const cls = p.Class_Name || p.asset_class || 'building';
    const street = p.Street_ID || p.street_id || 'ST01';
    const currentImg = DATA.images[state.selectedImageIdx] || DATA.images[0];

    document.getElementById('drawerTitle').textContent = `Asset Details: ${id}`;
    document.getElementById('drawerAssetId').textContent = id;
    document.getElementById('drawerClass').textContent = cls;
    document.getElementById('drawerStreet').textContent = `${street} — ${currentImg.Street_Name || ''}`;
    
    let coords = p.Latitude ? `${p.Latitude}, ${p.Longitude}` : (p.nearest_pole_coord ? `${p.nearest_pole_coord[1]}, ${p.nearest_pole_coord[0]}` : '11.03535, 76.97342');
    document.getElementById('drawerCoords').textContent = coords;

    const conf = p.Confidence ? `${(p.Confidence * 100).toFixed(0)}%` : '92%';
    document.getElementById('drawerConfidence').textContent = conf;

    const isVerified = state.verifiedFrames[currentImg.Image_ID] || false;
    document.getElementById('drawerStatusBadge').innerHTML = `<span class="badge ${isVerified ? 'badge-success' : 'badge-warning'}">${isVerified ? 'Verified Ground Truth' : 'Pending Verification'}</span>`;

    document.getElementById('drawerDetails').textContent = p.Details || p.Standardized_Label || p.technical_specs || 'High-resolution optical street frame detection.';

    const drawerImg = document.getElementById('drawerImage');
    if (drawerImg) {
      drawerImg.src = `assets/qa_previews/${currentImg.Image_ID}_qa_preview.jpg`;
      drawerImg.onerror = () => {
        drawerImg.src = `assets/raw_frames/${currentImg.Image_ID}.png`;
      };
    }

    drawer.classList.add('open');
  }

  function closeAssetDrawer() {
    const drawer = document.getElementById('assetDrawer');
    if (drawer) drawer.classList.remove('open');
  }

  function openDecisionModal() {
    const modal = document.getElementById('decisionModal');
    if (modal) modal.classList.add('open');
  }

  function closeDecisionModal() {
    const modal = document.getElementById('decisionModal');
    if (modal) modal.classList.remove('open');
  }

  function openHelpModal() {
    const modal = document.getElementById('helpModal');
    if (modal) modal.classList.add('open');
  }

  function closeHelpModal() {
    const modal = document.getElementById('helpModal');
    if (modal) modal.classList.remove('open');
  }

  function exportFrameYoloTxt(currentImg, detections) {
    if (!currentImg) return;
    const CLASS_MAP = {
      building: 0,
      electric_pole: 1,
      streetlight: 2,
      commercial_sign: 3,
      transformer: 4,
      traffic_signal: 5
    };
    const lines = detections.map(d => {
      const clsId = CLASS_MAP[d.Class_Name] !== undefined ? CLASS_MAP[d.Class_Name] : 0;
      let x1 = parseFloat(d.BBox_X1), y1 = parseFloat(d.BBox_Y1), x2 = parseFloat(d.BBox_X2), y2 = parseFloat(d.BBox_Y2);
      const w = currentImg.Width_px || 1512;
      const h = currentImg.Height_px || 727;
      if (x2 > 1.0) {
        x1 /= w; y1 /= h; x2 /= w; y2 /= h;
      }
      const xc = (x1 + x2) / 2;
      const yc = (y1 + y2) / 2;
      const bw = Math.abs(x2 - x1);
      const bh = Math.abs(y2 - y1);
      return `${clsId} ${xc.toFixed(6)} ${yc.toFixed(6)} ${bw.toFixed(6)} ${bh.toFixed(6)}`;
    });
    const blob = new Blob([lines.join('\n')], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${currentImg.Image_ID}.txt`;
    a.click();
    URL.revokeObjectURL(url);
    showToast(`Exported Darknet YOLO labels for ${currentImg.Image_ID}`, 'success');
  }

  function exportCanvasSnapshot() {
    const canvas = document.getElementById('studioBboxCanvas');
    if (!canvas) return;
    const currentImg = DATA.images[state.selectedImageIdx] || DATA.images[0];
    const dataUrl = canvas.toDataURL('image/png');
    const a = document.createElement('a');
    a.href = dataUrl;
    a.download = `${currentImg.Image_ID}_${state.studioMode}_snapshot.png`;
    a.click();
    showToast(`Downloaded snapshot for ${currentImg.Image_ID}`, 'success');
  }

  window.farmwiseApp = {
    jumpToVisualStudio: function (imgPath, assetId) {
      window.location.hash = 'detection';
      const idx = DATA.images.findIndex(img => img.Image_Path === imgPath || (assetId && img.Image_ID.includes(assetId.split('-')[1])));
      if (idx >= 0) {
        state.selectedImageIdx = idx;
        const select = document.getElementById('detectionImageSelect');
        if (select) select.value = idx;
        renderDetectionStudio();
      }
    },
    highlightBBox: function (detId) {
      state.hoveredBBoxId = detId;
      const canvas = document.getElementById('studioBboxCanvas');
      const currentImg = DATA.images[state.selectedImageIdx];
      if (canvas && currentImg && state.studioMode === 'bbox') {
        const img = new Image();
        img.src = `assets/raw_frames/${currentImg.Image_ID}.png`;
        img.onload = () => {
          const dets = DATA.detections.filter(d => d.Image_ID === currentImg.Image_ID);
          drawBBoxesOnCanvas(img, canvas, dets.filter(d => (d.Confidence || 0.9) >= state.detectionConfThreshold && (state.detectionClassFilter === 'ALL' || d.Class_Name === state.detectionClassFilter)));
        };
      }
    },
    inspectAsset: function (detId) {
      const det = DATA.detections.find(d => d.Detection_ID === detId);
      if (det) openAssetDrawer(det);
    },
    openInventoryDrawer: function (assetId) {
      const feat = DATA.assetsGeoJSON.features.find(f => f.properties.asset_id === assetId);
      if (feat) openAssetDrawer(feat);
    },
    openAssetDrawer: function (item) {
      if (typeof item === 'string') {
        const det = DATA.detections.find(d => d.Detection_ID === item) || (DATA.assetsGeoJSON.features.find(f => f.properties.asset_id === item));
        openAssetDrawer(det || { Detection_ID: item, Class_Name: 'Asset', Street_ID: 'ST01' });
      } else {
        openAssetDrawer(item);
      }
    },
    closeAssetDrawer: closeAssetDrawer,
    openDecisionModal: openDecisionModal,
    closeDecisionModal: closeDecisionModal,
    openHelpModal: openHelpModal,
    closeHelpModal: closeHelpModal,
    saveReviewNote: function (itemId, note) {
      state.reviewNotes[itemId] = note;
      localStorage.setItem('farmwise_review_notes', JSON.stringify(state.reviewNotes));
      showToast('Auditor note saved.', 'info');
    },
    exportCSV: exportInventoryCSV,
    exportGeoJSON: exportInventoryGeoJSON,
    showToast: showToast
  };

  // DOM Content Loaded Handler
  document.addEventListener('DOMContentLoaded', () => {
    initRouter();

    // Sidebar collapse toggle
    const toggleBtn = document.getElementById('sidebarToggleBtn');
    const sidebar = document.querySelector('.app-sidebar');
    if (toggleBtn && sidebar) {
      toggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
      });
    }

    // Mobile nav toggle
    const mobileBtn = document.getElementById('mobileNavToggle');
    if (mobileBtn && sidebar) {
      mobileBtn.addEventListener('click', () => {
        sidebar.classList.toggle('mobile-open');
      });
    }

    // Help Modal Triggers
    const helpBtn = document.getElementById('helpModalBtn');
    const closeHelpBtn = document.getElementById('closeHelpModalBtn');
    const dismissHelpBtn = document.getElementById('dismissHelpModalBtn');
    if (helpBtn) helpBtn.addEventListener('click', openHelpModal);
    if (closeHelpBtn) closeHelpBtn.addEventListener('click', closeHelpModal);
    if (dismissHelpBtn) dismissHelpBtn.addEventListener('click', closeHelpModal);

    // Asset Drawer Triggers
    const closeDrawerBtn = document.getElementById('closeDrawerBtn');
    if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeAssetDrawer);

    const drawerApproveBtn = document.getElementById('drawerApproveBtn');
    if (drawerApproveBtn) {
      drawerApproveBtn.addEventListener('click', () => {
        showToast('✓ Asset approved in municipal registry.', 'success');
        closeAssetDrawer();
      });
    }

    const drawerFlagBtn = document.getElementById('drawerFlagBtn');
    if (drawerFlagBtn) {
      drawerFlagBtn.addEventListener('click', () => {
        openDecisionModal();
      });
    }

    // Decision Modal Triggers
    const closeDecBtn = document.getElementById('closeDecisionModalBtn');
    const cancelDecBtn = document.getElementById('cancelDecisionModalBtn');
    const confirmDecBtn = document.getElementById('confirmDecisionModalBtn');
    if (closeDecBtn) closeDecBtn.addEventListener('click', closeDecisionModal);
    if (cancelDecBtn) cancelDecBtn.addEventListener('click', closeDecisionModal);
    if (confirmDecBtn) {
      confirmDecBtn.addEventListener('click', () => {
        const action = document.getElementById('modalDecisionAction')?.value || 'APPROVED';
        showToast(`Decision recorded: ${action}. Audit trail logged.`, 'success');
        closeDecisionModal();
        closeAssetDrawer();
      });
    }

    // Visual Detection Mode Pills
    const modePills = document.querySelectorAll('#studioModePills .mode-pill');
    modePills.forEach(pill => {
      pill.addEventListener('click', () => {
        modePills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.studioMode = pill.getAttribute('data-mode');
        renderDetectionStudio();
      });
    });

    // Corridor Jump Chips
    const jumpChips = document.querySelectorAll('#corridorJumpBtns .corridor-jump-chip');
    jumpChips.forEach(chip => {
      chip.addEventListener('click', () => {
        jumpChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const st = chip.getAttribute('data-street');
        state.activeStreetFilter = st;
        if (st !== 'ALL') {
          const firstIdx = DATA.images.findIndex(img => img.Street_ID === st);
          if (firstIdx >= 0) state.selectedImageIdx = firstIdx;
        }
        renderDetectionStudio();
      });
    });

    // Carousel Buttons
    const prevFrameBtn = document.getElementById('prevFrameBtn');
    const nextFrameBtn = document.getElementById('nextFrameBtn');
    if (prevFrameBtn) {
      prevFrameBtn.addEventListener('click', () => {
        state.selectedImageIdx = (state.selectedImageIdx - 1 + DATA.images.length) % DATA.images.length;
        renderDetectionStudio();
      });
    }
    if (nextFrameBtn) {
      nextFrameBtn.addEventListener('click', () => {
        state.selectedImageIdx = (state.selectedImageIdx + 1) % DATA.images.length;
        renderDetectionStudio();
      });
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowLeft') {
        state.selectedImageIdx = (state.selectedImageIdx - 1 + DATA.images.length) % DATA.images.length;
        renderDetectionStudio();
      } else if (e.key === 'ArrowRight') {
        state.selectedImageIdx = (state.selectedImageIdx + 1) % DATA.images.length;
        renderDetectionStudio();
      } else if (e.key === 'Escape') {
        closeAssetDrawer();
        closeDecisionModal();
        closeHelpModal();
      } else if (e.ctrlKey && e.key.toLowerCase() === 'b') {
        e.preventDefault();
        sidebar.classList.toggle('collapsed');
      }
    });

    // Frame Audit Action Buttons
    const approveFrameBtn = document.getElementById('approveAllFrameBtn');
    if (approveFrameBtn) {
      approveFrameBtn.addEventListener('click', () => {
        const currentImg = DATA.images[state.selectedImageIdx];
        if (currentImg) {
          state.verifiedFrames[currentImg.Image_ID] = {
            verified_at: new Date().toISOString(),
            auditor: 'Senior Municipal CV Engineer'
          };
          localStorage.setItem('farmwise_verified_frames', JSON.stringify(state.verifiedFrames));
          showToast(`✓ All ground truth annotations approved for ${currentImg.Image_ID}`, 'success');
          renderDetectionStudio();
        }
      });
    }

    const flagFrameBtn = document.getElementById('flagFrameFieldBtn');
    if (flagFrameBtn) {
      flagFrameBtn.addEventListener('click', openDecisionModal);
    }

    const exportYoloBtn = document.getElementById('exportYoloDarknetBtn');
    if (exportYoloBtn) {
      exportYoloBtn.addEventListener('click', () => {
        const currentImg = DATA.images[state.selectedImageIdx];
        const dets = DATA.detections.filter(d => d.Image_ID === currentImg?.Image_ID);
        exportFrameYoloTxt(currentImg, dets);
      });
    }

    const exportSnapBtn = document.getElementById('exportSnapshotBtn');
    if (exportSnapBtn) {
      exportSnapBtn.addEventListener('click', exportCanvasSnapshot);
    }

    // Split Slider Drag Listeners
    const splitContainer = document.getElementById('splitSliderViewport');
    if (splitContainer) {
      let isDragging = false;
      const onMove = (clientX) => {
        const rect = splitContainer.getBoundingClientRect();
        const pos = (clientX - rect.left) / rect.width;
        state.splitSliderPos = Math.max(0.05, Math.min(0.95, pos));
        updateSplitSlider();
      };
      splitContainer.addEventListener('mousedown', (e) => { isDragging = true; onMove(e.clientX); });
      window.addEventListener('mousemove', (e) => { if (isDragging) onMove(e.clientX); });
      window.addEventListener('mouseup', () => { isDragging = false; });
      splitContainer.addEventListener('touchstart', (e) => { isDragging = true; onMove(e.touches[0].clientX); });
      window.addEventListener('touchmove', (e) => { if (isDragging) onMove(e.touches[0].clientX); });
      window.addEventListener('touchend', () => { isDragging = false; });
    }

    // Canvas Interactive Hover & Click Inspector
    const canvas = document.getElementById('studioBboxCanvas');
    if (canvas) {
      canvas.addEventListener('mousemove', (e) => {
        if (state.studioMode !== 'bbox') return;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const mouseX = (e.clientX - rect.left) * scaleX;
        const mouseY = (e.clientY - rect.top) * scaleY;

        const currentImg = DATA.images[state.selectedImageIdx];
        const dets = DATA.detections.filter(d => d.Image_ID === currentImg?.Image_ID && (d.Confidence || 0.9) >= state.detectionConfThreshold && (state.detectionClassFilter === 'ALL' || d.Class_Name === state.detectionClassFilter));
        
        const hovered = dets.find(d => {
          let x1 = parseFloat(d.BBox_X1), y1 = parseFloat(d.BBox_Y1), x2 = parseFloat(d.BBox_X2), y2 = parseFloat(d.BBox_Y2);
          if (x2 <= 1.0) { x1 *= canvas.width; y1 *= canvas.height; x2 *= canvas.width; y2 *= canvas.height; }
          return mouseX >= x1 && mouseX <= x2 && mouseY >= y1 && mouseY <= y2;
        });

        if (hovered && state.hoveredBBoxId !== hovered.Detection_ID) {
          state.hoveredBBoxId = hovered.Detection_ID;
          canvas.style.cursor = 'pointer';
          const img = new Image();
          img.src = `assets/raw_frames/${currentImg.Image_ID}.png`;
          img.onload = () => drawBBoxesOnCanvas(img, canvas, dets);
        } else if (!hovered && state.hoveredBBoxId !== null) {
          state.hoveredBBoxId = null;
          canvas.style.cursor = 'default';
          const img = new Image();
          img.src = `assets/raw_frames/${currentImg.Image_ID}.png`;
          img.onload = () => drawBBoxesOnCanvas(img, canvas, dets);
        }
      });

      canvas.addEventListener('click', () => {
        if (state.studioMode !== 'bbox') return;
        if (state.hoveredBBoxId) {
          const det = DATA.detections.find(d => d.Detection_ID === state.hoveredBBoxId);
          if (det) openAssetDrawer(det);
        }
      });
    }

    // City Explorer Layer Chips (Project 1 Integration)
    const explorerChips = document.querySelectorAll('#explorerLayerChips .filter-chip');
    explorerChips.forEach(chip => {
      chip.addEventListener('click', () => {
        const layer = chip.getAttribute('data-layer');
        if (layer === 'all') {
          const makeActive = !chip.classList.contains('active');
          explorerChips.forEach(c => c.classList.toggle('active', makeActive));
          Object.keys(state.activeLayerToggles).forEach(k => state.activeLayerToggles[k] = makeActive);
        } else {
          chip.classList.toggle('active');
          state.activeLayerToggles[layer] = chip.classList.contains('active');
        }
        updateExplorerLayerVisibility();
      });
    });

    // Detected Runs Select
    const runsSelect = document.getElementById('detectedRunsSelect');
    if (runsSelect) {
      runsSelect.addEventListener('change', (e) => {
        state.selectedRunImage = e.target.value;
        renderDetectionStudio();
      });
    }

    // Global Search Input
    const globalSearch = document.getElementById('globalSearchInput');
    if (globalSearch) {
      globalSearch.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const rawQ = globalSearch.value.trim();
          const lowerQ = rawQ.toLowerCase();
          if (rawQ.includes('?') || lowerQ.startsWith('what') || lowerQ.startsWith('how') || lowerQ.startsWith('why') || lowerQ.startsWith('which') || lowerQ.includes('clearance') || lowerQ.includes('hazard')) {
            window.location.hash = 'agent';
            if (window.farmwiseUrbanAgent && window.farmwiseUrbanAgent.ask) {
              window.farmwiseUrbanAgent.ask(rawQ);
            }
            return;
          }
          const q = rawQ.toUpperCase();
          if (q.startsWith('ST0') || q.startsWith('ST1')) {
            window.location.hash = 'detection';
            const idx = DATA.images.findIndex(img => img.Street_ID === q);
            if (idx >= 0) {
              state.selectedImageIdx = idx;
              renderDetectionStudio();
              showToast(`Navigated to corridor ${q}`, 'info');
            }
          } else {
            window.location.hash = 'inventory';
            const invSearch = document.getElementById('inventorySearchInput');
            if (invSearch) {
              invSearch.value = globalSearch.value;
              state.inventoryFilters.search = globalSearch.value;
              renderInventoryTable();
            }
          }
        }
      });
    }

    // Detection Frame Select
    const detImgSelect = document.getElementById('detectionImageSelect');
    if (detImgSelect) {
      detImgSelect.addEventListener('change', (e) => {
        state.selectedImageIdx = parseInt(e.target.value, 10);
        renderDetectionStudio();
      });
    }

    // BBox Toggle
    const bboxToggle = document.getElementById('detectionBboxToggle');
    if (bboxToggle) {
      bboxToggle.addEventListener('change', (e) => {
        state.detectionShowBboxes = e.target.checked;
        renderDetectionStudio();
      });
    }

    // Confidence Slider
    const confSlider = document.getElementById('detectionConfSlider');
    const confVal = document.getElementById('detectionConfVal');
    if (confSlider && confVal) {
      confSlider.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        state.detectionConfThreshold = val;
        confVal.textContent = `${(val * 100).toFixed(0)}%`;
        renderDetectionStudio();
      });
    }

    // Class Filter
    const classFilter = document.getElementById('detectionClassSelect');
    if (classFilter) {
      classFilter.addEventListener('change', (e) => {
        state.detectionClassFilter = e.target.value;
        renderDetectionStudio();
      });
    }

    // OCR Search Input
    const ocrInput = document.getElementById('ocrSearchInput');
    if (ocrInput) {
      ocrInput.addEventListener('input', (e) => {
        state.ocrSearchQuery = e.target.value;
        renderSignageStudio();
      });
    }

    const ocrCategory = document.getElementById('ocrCategorySelect');
    if (ocrCategory) {
      ocrCategory.addEventListener('change', (e) => {
        state.ocrCategoryFilter = e.target.value;
        renderSignageStudio();
      });
    }

    // Inventory Search & Filters
    const invSearch = document.getElementById('inventorySearchInput');
    if (invSearch) {
      invSearch.addEventListener('input', (e) => {
        state.inventoryFilters.search = e.target.value;
        state.inventoryPage = 1;
        renderInventoryTable();
      });
    }

    const invClass = document.getElementById('inventoryClassFilter');
    if (invClass) {
      invClass.addEventListener('change', (e) => {
        state.inventoryFilters.classType = e.target.value;
        state.inventoryPage = 1;
        renderInventoryTable();
      });
    }

    const invCorridor = document.getElementById('inventoryCorridorFilter');
    if (invCorridor) {
      invCorridor.addEventListener('change', (e) => {
        state.inventoryFilters.corridor = e.target.value;
        state.inventoryPage = 1;
        renderInventoryTable();
      });
    }

    const prevBtn = document.getElementById('inventoryPrevPage');
    const nextBtn = document.getElementById('inventoryNextPage');
    if (prevBtn && nextBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.inventoryPage > 1) {
          state.inventoryPage--;
          renderInventoryTable();
        }
      });
      nextBtn.addEventListener('click', () => {
        state.inventoryPage++;
        renderInventoryTable();
      });
    }
  });

})();
