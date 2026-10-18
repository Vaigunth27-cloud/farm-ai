# FarmwiseAI Design System — Urban Geospatial Intelligence Platform

**Version:** 2.5-Enterprise  
**Domain:** Coimbatore City Municipal Corporation (CCMC) — Ward 29 Digital Twin  
**Aesthetic:** Clean, high-tech, organic enterprise geospatial intelligence. Minimal, spacious, white and forest green with soft sage and pale surfaces.

---

## 1. Brand Identity & Design Principles

1. **Spatial Clarity Over Clutter:** Interfaces prioritize geographic and visual context. Information density is managed through deliberate hierarchy and progressive disclosure—never cramming every metric onto a single viewport.
2. **Authentic Data Trust:** Direct sensor and camera observations are cleanly distinguished from model inferences, synthetic placeholders, and derived tabular attributes.
3. **Restrained Color Discipline:** Color is used functionally—for active navigation, layer distinction, data density, and urgent alerts—never decoratively.
4. **Accessible & Responsive:** Fluid navigation adapts from multi-monitor GIS workstations down to tablet and mobile inspection devices.

---

## 2. Color Palette & Semantic Tokens

| Token Name | Hex Value | Role / Usage | Contrast Ratio |
| :--- | :---: | :--- | :---: |
| `--bg-primary` | `#FFFFFF` | Primary viewport & card background | Baseline |
| `--bg-surface` | `#F5F9F5` | Pale green table headers, muted controls, soft containers | Soft contrast |
| `--bg-subtle` | `#EAF4EC` | Soft sage active navigation, highlights, pill tags | Subtle green accent |
| `--primary-green` | `#176B45` | Primary brand green, active nav indicators, primary buttons | 5.2:1 on White (AA) |
| `--deep-green` | `#104D35` | High-contrast headers, brand logo, strong emphasis text | 9.8:1 on White (AAA) |
| `--text-main` | `#1F3328` | Primary body and heading typography | 11.4:1 on White (AAA) |
| `--text-secondary` | `#68776D` | Subtitles, metadata labels, secondary descriptors | 4.8:1 on White (AA) |
| `--border-color` | `#E2EAE3` | Card dividers, table borders, input containers | Clean delineation |
| `--warning-amber` | `#D97706` | Pending reviews, unverified bounding boxes, warnings | High visibility |
| `--critical-red` | `#DC2626` | P1 electrical clearance violations, emergency alerts | Immediate attention |
| `--info-blue` | `#2563EB` | Neutral informational vectors, utilities, GIS telemetry | Clear contrast |

---

## 3. Typography & Hierarchy

The platform standardizes on **Inter** (with system fallback `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`).

| Style | Size | Weight | Line Height | Tracking | Usage |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Display Title** | 22px | 700 | 1.25 | -0.02em | Workspace page titles |
| **Section Header** | 16px | 700 | 1.30 | -0.01em | Inspector titles, card headers |
| **Card Title** | 14px | 600 | 1.40 | 0.00em | Widget titles, metric labels |
| **Body Regular** | 13px | 400 | 1.50 | 0.00em | Data table values, descriptions |
| **Caption / Meta** | 11px | 500 | 1.40 | +0.02em | Timestamps, coordinate labels |
| **Code / Mono** | 12px | 600 | 1.40 | 0.00em | UUIDs, GPS coordinates, hashes |

---

## 4. Elevation, Spacing & Borders

- **Spacing Scale:** 4px, 8px, 12px, 16px, 20px, 24px, 32px, 48px
- **Border Radii:**
  - Micro tags / pills: `4px`
  - Form inputs & buttons: `6px`
  - Cards & inspector drawers: `10px`
  - Outer map & canvas frames: `14px`
  - Badges & search pills: `9999px` (full pill)
- **Shadows:**
  - Card baseline: `0 1px 3px rgba(16, 77, 53, 0.05)`
  - Card hover: `0 4px 6px -1px rgba(16, 77, 53, 0.07)`
  - Floating map controls / drawers: `0 10px 15px -3px rgba(16, 77, 53, 0.08)`
