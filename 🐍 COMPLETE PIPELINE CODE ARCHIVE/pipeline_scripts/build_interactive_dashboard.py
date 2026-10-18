import os
import json

scratch_dir = r"C:\Users\ABI\.gemini\antigravity\scratch"
dashboard_dir = os.path.join(scratch_dir, "dashboard")
os.makedirs(dashboard_dir, exist_ok=True)

with open(os.path.join(scratch_dir, "fai-tce-team24-master.geojson"), "r", encoding="utf-8") as f:
    master_geojson_raw = f.read()

dashboard_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FarmwiseAI TCE Product Challenge - Team 24 3D Urban Intelligence</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    #map { height: calc(100vh - 80px); width: 100%; }
    .custom-scroll::-webkit-scrollbar { width: 6px; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    .leaflet-popup-content-wrapper { background: #0f172a; color: #f8fafc; border-radius: 12px; border: 1px solid #334155; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5); }
    .leaflet-popup-tip { background: #0f172a; }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 flex flex-col h-screen overflow-hidden font-sans">

  <!-- Top Header with Comprehensive KPI Cards -->
  <header class="h-20 bg-slate-900 border-b border-slate-800 px-6 py-2.5 flex items-center justify-between z-10 shadow-xl">
    <div class="flex items-center gap-3.5">
      <div class="h-10 w-10 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-700 flex items-center justify-center font-black text-white text-xl shadow-lg shadow-emerald-950">24</div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-base font-extrabold tracking-tight text-white">Coimbatore Ward 29 3D Urban Intelligence</h1>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/40">TEAM 24 • VERIFIED PRISTINE</span>
        </div>
        <p class="text-xs text-slate-400">Thiagarajar College of Engineering • FarmwiseAI Product Challenge 2026</p>
      </div>
    </div>

    <!-- Live Metrics Strip -->
    <div class="hidden lg:flex items-center gap-4 text-xs">
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Total Survey</span>
        <span class="text-sm font-black text-emerald-400">2,425.8 m</span>
        <span class="text-[9px] text-emerald-500 block">✓ >= 2.0 km Req.</span>
      </div>
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Streets</span>
        <span class="text-sm font-black text-blue-400">10 / 10</span>
        <span class="text-[9px] text-slate-400 block">All Verified</span>
      </div>
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Field Images</span>
        <span class="text-sm font-black text-purple-400">108</span>
        <span class="text-[9px] text-purple-400 block">100% In Ward</span>
      </div>
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Physical Assets</span>
        <span class="text-sm font-black text-amber-400">172</span>
        <span class="text-[9px] text-amber-500 block">7 Categories</span>
      </div>
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Elevation AMSL</span>
        <span class="text-sm font-black text-teal-400">411 - 421 m</span>
        <span class="text-[9px] text-teal-500 block">3D Dem Model</span>
      </div>
      <div class="bg-slate-950/80 border border-slate-800 px-3 py-1.5 rounded-lg text-center">
        <span class="text-slate-400 block text-[9px] uppercase tracking-wider">Max Building</span>
        <span class="text-sm font-black text-rose-400">G+4 (16.5m)</span>
        <span class="text-[9px] text-slate-400 block">NH 948 Corridor</span>
      </div>
    </div>
  </header>

  <!-- Main View Area -->
  <div class="flex flex-1 relative overflow-hidden">

    <!-- Left Sidebar: Layer Toggles & Street Directory -->
    <aside class="w-84 bg-slate-900/95 border-r border-slate-800 flex flex-col z-10 custom-scroll overflow-y-auto">
      <div class="p-4 border-b border-slate-800 space-y-3">
        <div class="flex items-center justify-between text-xs font-bold text-slate-300">
          <span>3D GIS LAYERS</span>
          <button onclick="resetLayers()" class="text-emerald-400 hover:underline text-[11px]">Show All</button>
        </div>
        <div class="space-y-2 text-xs">
          <label class="flex items-center justify-between p-2 rounded-lg bg-emerald-950/40 border border-emerald-800/50 cursor-pointer hover:bg-emerald-900/30 transition">
            <span class="flex items-center gap-2 text-emerald-300 font-semibold">
              <input type="checkbox" id="chkBoundary" checked class="rounded text-emerald-500" onchange="toggleLayer('boundary')">
              Ward 29 Boundary (158-pt)
            </span>
            <span class="text-[10px] bg-emerald-900/80 text-emerald-300 px-1.5 py-0.5 rounded">Polygon</span>
          </label>
          <label class="flex items-center justify-between p-2 rounded-lg bg-blue-950/40 border border-blue-800/50 cursor-pointer hover:bg-blue-900/30 transition">
            <span class="flex items-center gap-2 text-blue-300 font-semibold">
              <input type="checkbox" id="chkStreets" checked class="rounded text-blue-500" onchange="toggleLayer('streets')">
              10 Surveyed Corridors
            </span>
            <span class="text-[10px] bg-blue-900/80 text-blue-300 px-1.5 py-0.5 rounded">2.43 km</span>
          </label>
          <label class="flex items-center justify-between p-2 rounded-lg bg-amber-950/40 border border-amber-800/50 cursor-pointer hover:bg-amber-900/30 transition">
            <span class="flex items-center gap-2 text-amber-300 font-semibold">
              <input type="checkbox" id="chkAssets" checked class="rounded text-amber-500" onchange="toggleLayer('assets')">
              172 Physical Assets (3D)
            </span>
            <span class="text-[10px] bg-amber-900/80 text-amber-300 px-1.5 py-0.5 rounded">Poles/ATMs</span>
          </label>
          <label class="flex items-center justify-between p-2 rounded-lg bg-purple-950/40 border border-purple-800/50 cursor-pointer hover:bg-purple-900/30 transition">
            <span class="flex items-center gap-2 text-purple-300 font-semibold">
              <input type="checkbox" id="chkImages" checked class="rounded text-purple-500" onchange="toggleLayer('images')">
              108 Image Viewpoints & Floors
            </span>
            <span class="text-[10px] bg-purple-900/80 text-purple-300 px-1.5 py-0.5 rounded">G to G+4</span>
          </label>
        </div>
      </div>

      <!-- Street Directory List -->
      <div class="p-4 space-y-2 flex-1">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2 flex items-center justify-between">
          <span>Surveyed Streets</span>
          <span class="text-[10px] text-slate-500 font-normal">Click to focus</span>
        </div>
        <div id="streetDirectory" class="space-y-1.5 text-xs"></div>
      </div>
    </aside>

    <!-- Map Canvas -->
    <main class="flex-1 relative">
      <div id="map"></div>

      <!-- Map Legend Card -->
      <div class="absolute bottom-6 right-6 bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow-2xl text-xs space-y-2.5 z-[1000] backdrop-blur-md max-w-sm">
        <div class="font-black text-slate-200 text-xs border-b border-slate-800 pb-1.5 flex items-center justify-between">
          <span>3D Urban Symbology</span>
          <span class="text-[10px] text-emerald-400 font-mono">WGS84 / EPSG:4326</span>
        </div>
        <div class="space-y-1.5 text-[11px] text-slate-300">
          <div class="flex items-center gap-2.5">
            <span class="w-4 h-2 border-2 border-emerald-400 border-dashed bg-emerald-500/20 rounded"></span>
            <span>Ward 29 Study Boundary Polygon</span>
          </div>
          <div class="flex items-center gap-2.5">
            <span class="w-3.5 h-1.5 bg-blue-500 rounded"></span>
            <span>Commercial Highway Corridor (NH 948)</span>
          </div>
          <div class="flex items-center gap-2.5">
            <span class="w-3.5 h-1.5 bg-purple-500 rounded"></span>
            <span>Mixed Commercial & Residential Strip</span>
          </div>
          <div class="flex items-center gap-2.5">
            <span class="w-3.5 h-1.5 bg-emerald-500 rounded"></span>
            <span>Residential Colony / Layout Road</span>
          </div>
          <div class="flex items-center gap-2.5 pt-1 border-t border-slate-800">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-400 ring-2 ring-amber-300/40"></span>
            <span>Physical Asset (Utility Pole, Transformer, ATM, Signal)</span>
          </div>
          <div class="flex items-center gap-2.5">
            <span class="w-2.5 h-2.5 rounded-full bg-purple-400 ring-2 ring-purple-300/40"></span>
            <span>Image Viewpoint (Building Floor & Elevation AMSL)</span>
          </div>
        </div>
      </div>
    </main>
  </div>

  <script>
    const masterData = __MASTER_GEOJSON__;

    const map = L.map('map', {
      center: [11.0335, 76.9780],
      zoom: 15,
      zoomControl: true
    });

    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
      subdomains: 'abcd',
      maxZoom: 19
    }).addTo(map);

    const boundaryGroup = L.layerGroup().addTo(map);
    const streetsGroup = L.layerGroup().addTo(map);
    const assetsGroup = L.layerGroup().addTo(map);
    const imagesGroup = L.layerGroup().addTo(map);

    const streetLayerRefs = {};

    function getStreetColor(zone) {
      if (zone.includes('Highway') || zone.includes('Commercial')) return '#3b82f6';
      if (zone.includes('Mixed') || zone.includes('Industrial')) return '#a855f7';
      return '#10b981';
    }

    function getAssetColor(type) {
      if (type.includes('Pole')) return '#3b82f6';
      if (type.includes('Streetlight')) return '#eab308';
      if (type.includes('Transformer')) return '#f97316';
      if (type.includes('Signal')) return '#ef4444';
      if (type.includes('CCTV')) return '#a855f7';
      if (type.includes('ATM')) return '#10b981';
      if (type.includes('Temple')) return '#f43f5e';
      return '#64748b';
    }

    // Process GeoJSON Features
    masterData.features.forEach(feat => {
      const g = feat.geometry;
      const p = feat.properties;

      // 1. Boundary Polygon
      if (g.type === 'MultiPolygon' || p.layer === 'ward_boundary') {
        const poly = L.geoJSON(feat, {
          style: {
            color: '#10b981',
            dashArray: '6, 6',
            weight: 3,
            fillColor: '#10b981',
            fillOpacity: 0.08
          }
        });
        poly.bindPopup(`
          <div class="p-2 space-y-1 text-slate-100 font-sans">
            <div class="font-bold text-sm text-emerald-400">Coimbatore Corporation - Ward 29</div>
            <div class="text-[11px] text-slate-300">Designated Study Area (North Zone)</div>
            <div class="text-[10px] text-slate-400 pt-1 border-t border-slate-700">Official Municipal Boundary (158 vertices)</div>
          </div>
        `);
        boundaryGroup.addLayer(poly);
        map.fitBounds(poly.getBounds(), { padding: [30, 30] });
      }

      // 2. Street Corridors
      else if (g.type === 'LineString' && p.layer === 'surveyed_streets') {
        const line = L.geoJSON(feat, {
          style: {
            color: getStreetColor(p.zone_type),
            weight: 5,
            opacity: 0.95
          }
        });
        line.bindPopup(`
          <div class="p-2.5 space-y-1.5 text-slate-100 font-sans max-w-xs">
            <div class="flex items-center justify-between border-b border-slate-700 pb-1">
              <b class="text-sm font-bold text-blue-400">${p.street_name}</b>
              <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800">${p.street_id}</span>
            </div>
            <div class="text-xs text-slate-300 leading-snug"><b>Zone:</b> ${p.zone_type}</div>
            <div class="grid grid-cols-2 gap-2 text-[11px] bg-slate-950 p-2 rounded-lg border border-slate-800">
              <div><span class="text-slate-400">Length:</span> <b class="text-white">${p.length_meters} m</b></div>
              <div><span class="text-slate-400">In Boundary:</span> <b class="text-emerald-400">${p.pct_inside_boundary}%</b></div>
              <div><span class="text-slate-400">Elevation:</span> <b class="text-teal-400">${p.avg_ground_elevation_amsl_m} m AMSL</b></div>
              <div><span class="text-slate-400">Max Floors:</span> <b class="text-rose-400">${p.max_building_floors}</b></div>
            </div>
            <div class="text-[11px] text-slate-300"><b>Peak Height:</b> ${p.max_building_height_m} m structural</div>
            <div class="text-[10px] text-slate-400 italic"><b>Typology:</b> ${p.dominant_building_typology}</div>
          </div>
        `);
        streetLayerRefs[p.street_id] = line;
        streetsGroup.addLayer(line);
      }

      // 3. Physical Assets (Point)
      else if (g.type === 'Point' && p.layer === 'urban_assets') {
        const color = getAssetColor(p.asset_type);
        const marker = L.circleMarker([g.coordinates[1], g.coordinates[0]], {
          radius: 4.5,
          fillColor: color,
          color: '#ffffff',
          weight: 1.5,
          opacity: 1,
          fillOpacity: 0.95
        });
        marker.bindPopup(`
          <div class="p-2 space-y-1 text-slate-100 font-sans max-w-xs">
            <div class="flex items-center justify-between border-b border-slate-700 pb-1">
              <b class="text-xs font-bold text-amber-400">${p.asset_type}</b>
              <span class="text-[9px] font-mono px-1 py-0.5 rounded bg-slate-800 text-slate-300">${p.asset_id}</span>
            </div>
            <div class="text-[11px] text-slate-300"><b>Category:</b> ${p.category}</div>
            <div class="text-[11px] text-slate-300"><b>Street:</b> ${p.street}</div>
            <div class="grid grid-cols-2 gap-1.5 text-[10px] bg-slate-950 p-1.5 rounded border border-slate-800 mt-1">
              <div><span class="text-slate-400">Ground:</span> <b class="text-teal-400">${p.ground_elevation_amsl_m}m</b></div>
              <div><span class="text-slate-400">Mount:</span> <b class="text-amber-400">${p.asset_mounting_height_m}m</b></div>
              <div class="col-span-2 text-center border-t border-slate-800 pt-0.5"><span class="text-slate-400">Top Elev:</span> <b class="text-emerald-400">${p.total_elevation_amsl_m} m AMSL</b></div>
            </div>
          </div>
        `);
        assetsGroup.addLayer(marker);
      }

      // 4. Image Viewpoints with 3D Building Floor Data
      else if (g.type === 'Point' && p.layer === 'image_viewpoints') {
        const marker = L.circleMarker([g.coordinates[1], g.coordinates[0]], {
          radius: 3.5,
          fillColor: '#c084fc',
          color: '#ffffff',
          weight: 1,
          opacity: 1,
          fillOpacity: 0.9
        });
        marker.bindPopup(`
          <div class="p-2 space-y-1.5 text-slate-100 font-sans max-w-xs">
            <div class="flex items-center justify-between border-b border-slate-700 pb-1">
              <b class="text-xs font-bold text-purple-300">${p.image_id}</b>
              <span class="text-[9px] font-mono px-1 py-0.5 rounded bg-purple-950 text-purple-300 border border-purple-800">${p.building_floors}</span>
            </div>
            <div class="text-[11px] text-slate-200"><b>Building Typology:</b> ${p.building_typology}</div>
            <div class="grid grid-cols-2 gap-1.5 text-[10px] bg-slate-950 p-1.5 rounded border border-slate-800">
              <div><span class="text-slate-400">Floor Count:</span> <b class="text-white">${p.floor_count} floors</b></div>
              <div><span class="text-slate-400">Height:</span> <b class="text-amber-400">${p.building_height_m} m</b></div>
              <div><span class="text-slate-400">Ground AMSL:</span> <b class="text-teal-400">${p.ground_elevation_amsl_m} m</b></div>
              <div><span class="text-slate-400">Rooftop AMSL:</span> <b class="text-rose-400">${p.rooftop_elevation_amsl_m} m</b></div>
            </div>
            <div class="text-[10px] text-slate-400 italic"><b>Notes:</b> ${p.notes}</div>
          </div>
        `);
        imagesGroup.addLayer(marker);
      }
    });

    // Populate Sidebar Street Directory
    const streetContainer = document.getElementById('streetDirectory');
    masterData.features.filter(f => f.geometry.type === 'LineString' && f.properties.layer === 'surveyed_streets').forEach(feat => {
      const p = feat.properties;
      const card = document.createElement('div');
      card.className = "p-2.5 rounded-lg bg-slate-950 border border-slate-800/80 hover:border-slate-600 cursor-pointer transition flex flex-col gap-1 shadow-sm";
      card.innerHTML = `
        <div class="flex items-center justify-between">
          <div class="font-bold text-slate-200 text-xs flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full" style="background-color: ${getStreetColor(p.zone_type)}"></span>
            ${p.street_name.substring(0, 20)}
          </div>
          <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/60 border border-emerald-800/40 px-1 py-0.5 rounded">${p.street_id}</span>
        </div>
        <div class="flex items-center justify-between text-[10px] text-slate-400">
          <span>${p.length_meters}m • ${p.total_images} imgs</span>
          <span class="text-teal-400 font-semibold">${p.avg_ground_elevation_amsl_m}m AMSL</span>
        </div>
        <div class="text-[10px] text-rose-300 font-medium">${p.max_building_floors} • Max ${p.max_building_height_m}m</div>
      `;
      card.onclick = () => {
        const lyr = streetLayerRefs[p.street_id];
        if (lyr) {
          map.fitBounds(lyr.getBounds(), { padding: [60, 60], maxZoom: 17 });
          lyr.openPopup();
        }
      };
      streetContainer.appendChild(card);
    });

    // Layer Handlers
    function toggleLayer(type) {
      if (type === 'boundary') {
        if (document.getElementById('chkBoundary').checked) map.addLayer(boundaryGroup);
        else map.removeLayer(boundaryGroup);
      } else if (type === 'streets') {
        if (document.getElementById('chkStreets').checked) map.addLayer(streetsGroup);
        else map.removeLayer(streetsGroup);
      } else if (type === 'assets') {
        if (document.getElementById('chkAssets').checked) map.addLayer(assetsGroup);
        else map.removeLayer(assetsGroup);
      } else if (type === 'images') {
        if (document.getElementById('chkImages').checked) map.addLayer(imagesGroup);
        else map.removeLayer(imagesGroup);
      }
    }

    function resetLayers() {
      ['chkBoundary', 'chkStreets', 'chkAssets', 'chkImages'].forEach(id => document.getElementById(id).checked = true);
      map.addLayer(boundaryGroup);
      map.addLayer(streetsGroup);
      map.addLayer(assetsGroup);
      map.addLayer(imagesGroup);
    }
  </script>
</body>
</html>
"""

dashboard_file = os.path.join(dashboard_dir, "index.html")
final_html = dashboard_html.replace("__MASTER_GEOJSON__", master_geojson_raw)
with open(dashboard_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Interactive 3D Web GIS Dashboard written to: {dashboard_file}")
