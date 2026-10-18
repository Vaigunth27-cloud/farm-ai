# FarmwiseAI Project 2 — Reusable UI Components Library

**Architecture:** Pure CSS3 & Vanilla JavaScript Components  
**Target Design:** Modern, White & Forest Green Enterprise Geospatial Intelligence  
**CSS File:** `assets/css/design_system.css`  
**JS Controller:** `assets/js/app.js`  

---

## 1. Core Component Index

| Component Name | CSS Class / Selector | Visual Purpose & Capabilities |
| :--- | :--- | :--- |
| **KPI Metric Card** | `.kpi-card`, `.kpi-grid` | Hero summary cards with uppercase label, metric value, positive/amber pill, and icon container. Interactive hover state (`translateY(-2px)`). |
| **Interactive Card** | `.card`, `.card.interactive` | Rounded white surface card with subtle border (`#E2EAE3`), subtle shadow, and clean padding. Clickable variant provides hover border tint. |
| **Filter Toolbar** | `.filter-toolbar`, `.filter-group` | Responsive flex toolbar containing select dropdowns, search inputs, and filter pill buttons. |
| **Status & Class Badges** | `.badge`, `.badge-subtle`, `.badge-warning`, `.badge-critical` | Full-pill status indicators for asset classes, municipal priorities, and data quality alerts. |
| **Data Table** | `.data-table`, `.table-container` | High-density data grid with pale green header (`#F5F9F5`), zebra hover, monospaced ID styling (`.cell-mono`), and clean cell padding. |
| **GIS Map Viewport** | `.map-workspace-wrap`, `.map-viewport` | Responsive Leaflet container with floating control panels (`.map-card-panel`) and right-side inspection drawer (`.map-inspector-sidebar`). |
| **Visual Canvas Viewer** | `.canvas-viewport-card`, `.canvas-container` | Responsive canvas wrapper for high-res Street View frames with dynamic bounding box overlay rendering. |
| **Inspector Drawer** | `.map-inspector-sidebar` | Slide-out panel for selected assets, displaying digital passports, condition ratings, nearest infrastructure links, and evidence thumbnails. |
| **Empty / Neutral State** | `.empty-state-box`, `.empty-icon` | Centered informational placeholder with icon, title, and descriptive guidance for empty filters or search queries. |
| **Responsive Sidebar** | `.app-sidebar`, `.collapsed`, `.mobile-open` | Persistent left navigation rail with brand header, section labels, active left-accent border, and mobile slide-in drawer. |

---

## 2. Component Code Patterns & Specifications

### 2.1 KPI Metric Card
```html
<div class="kpi-card" onclick="location.hash='inventory'">
  <div class="kpi-header">
    <span class="kpi-label">Fixed Infrastructure Assets</span>
    <div class="kpi-icon-wrap">📍</div>
  </div>
  <div class="kpi-value">465</div>
  <div class="kpi-meta">
    <span class="kpi-pill positive">100% Passports</span>
    <span>Poles, Lights, Signals, Signs</span>
  </div>
</div>
```

### 2.2 Status Badges
```html
<!-- Forest Green Active Badge -->
<span class="badge badge-subtle">building</span>

<!-- Critical P1 Defect Badge -->
<span class="badge badge-critical">33 P1-CRITICAL</span>

<!-- Muted Amber Verification Badge -->
<span class="badge badge-warning">Pending Review</span>

<!-- Neutral Bordered Tag -->
<span class="badge badge-neutral">TANGEDCO</span>
```

### 2.3 Filter Toolbar with Search & Dropdowns
```html
<div class="filter-toolbar">
  <div class="filter-group">
    <input type="text" class="filter-search-input" placeholder="Search by UUID, street, or class...">
  </div>
  <div class="filter-group">
    <select class="filter-select">
      <option value="ALL">All Asset Classes</option>
      <option value="electric_pole">Electric Utility Poles</option>
      <option value="streetlight">Streetlights</option>
    </select>
  </div>
</div>
```

### 2.4 Data Table with Monospaced Identifiers
```html
<div class="table-container">
  <table class="data-table">
    <thead>
      <tr>
        <th>Asset UUID</th>
        <th>Class</th>
        <th>Corridor</th>
        <th>Managing Agency</th>
        <th>Condition</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="cell-mono"><b>POLE-ST01-001</b></td>
        <td><span class="badge badge-subtle">electric_pole</span></td>
        <td>ST01 — Sathy Road</td>
        <td>TANGEDCO</td>
        <td><span class="badge badge-success">Good</span></td>
      </tr>
    </tbody>
  </table>
</div>
```
