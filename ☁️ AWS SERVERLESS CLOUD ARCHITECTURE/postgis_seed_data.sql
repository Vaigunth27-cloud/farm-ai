INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST01', 'Sathy Road (NH 948)', 292.5, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.973424 11.035355, 76.973506 11.035072, 76.973588 11.03479, 76.97367 11.034507, 76.973752 11.034225, 76.973833 11.033942, 76.973915 11.03366, 76.973997 11.033377, 76.974079 11.033095, 76.974161 11.032812)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST02', '4th Street, Sridevi Nagar', 296.2, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.973404 11.036796, 76.973544 11.036566, 76.973683 11.036337, 76.973823 11.036107, 76.973963 11.035878, 76.974103 11.035648, 76.974242 11.035418, 76.974382 11.035189, 76.974522 11.034959, 76.974661 11.03473, 76.974801 11.0345)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST03', 'Ganapathy Pudur 3rd Street', 205.7, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.974801 11.033632, 76.974958 11.033495, 76.975115 11.033358, 76.975271 11.033221, 76.975428 11.033084, 76.975585 11.032948, 76.975742 11.032811, 76.975898 11.032674, 76.976055 11.032537, 76.976212 11.0324)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST04', 'Gandhi Nagar Street', 196.0, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.9745 11.0382, 76.97461 11.03834, 76.97472 11.03848, 76.97483 11.03862, 76.97494 11.03876, 76.97505 11.0389, 76.97516 11.03904, 76.97527 11.03918, 76.97538 11.03932, 76.97549 11.03946, 76.9756 11.0396)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST05', 'Gopalasamy Kovil Street', 149.7, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.971928 11.034497, 76.972052 11.034584, 76.972176 11.034671, 76.972301 11.034758, 76.972425 11.034845, 76.972549 11.034931, 76.972673 11.035018, 76.972798 11.035105, 76.972922 11.035192, 76.973046 11.035279)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST06', 'KRG Nagar - Kattabomman Street', 237.9, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.980593 11.037542, 76.980773 11.037563, 76.980953 11.037584, 76.981133 11.037605, 76.981314 11.037626, 76.981494 11.037647, 76.981674 11.037668, 76.981854 11.03769, 76.982034 11.037711, 76.982214 11.037732, 76.982395 11.037753, 76.982575 11.037774, 76.982755 11.037795)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST07', 'PN Palayam Street', 275.8, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.972502 11.028301, 76.972761 11.028195, 76.97302 11.028089, 76.97328 11.027984, 76.973539 11.027878, 76.973798 11.027772, 76.974057 11.027666, 76.974317 11.027561, 76.974576 11.027455, 76.974835 11.027349)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST08', 'Raja Street - Sanganur Road', 363.9, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.974161 11.035397, 76.974211 11.035231, 76.97426 11.035065, 76.97431 11.034899, 76.97436 11.034733, 76.974409 11.034566, 76.974459 11.0344, 76.974509 11.034234, 76.974558 11.034068, 76.974608 11.033902, 76.974658 11.033736, 76.974708 11.03357, 76.974757 11.033404, 76.974807 11.033238, 76.974857 11.033072, 76.974906 11.032905, 76.974956 11.032739, 76.975006 11.032573, 76.975055 11.032407, 76.975105 11.032241)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST09', 'Sri Ganapathy Gardens 3rd Street', 156.4, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.9722 11.0392, 76.97238 11.03942, 76.97256 11.03964, 76.97274 11.03986, 76.97292 11.04008, 76.9731 11.0403)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('ST10', 'Ganapathy - Avarampalayam Road', 315.1, 7.0, 'Bitumen', ST_GeomFromText('LINESTRING(76.978492 11.031061, 76.978639 11.031513, 76.978786 11.031965, 76.978934 11.032417, 76.979081 11.03287, 76.979228 11.033322, 76.979375 11.033774)', 4326))
ON CONFLICT (street_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353182, 76.9732939, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9732939 11.0353182)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353655, 76.973461, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.973461 11.0353655)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353645, 76.9734574, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9734574 11.0353645)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353226, 76.9733096, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9733096 11.0353226)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353463, 76.9733932, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9733932 11.0353463)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0351089, 76.9736361, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9736361 11.0351089)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350615, 76.9734691, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9734691 11.0350615)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350625, 76.9734726, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9734726 11.0350625)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0351045, 76.9736204, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9736204 11.0351045)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350633, 76.9734752, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9734752 11.0350633)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034756, 76.9734679, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9734679 11.034756)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348005, 76.973625, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.973625 11.0348005)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347995, 76.9736214, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9736214 11.0347995)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347576, 76.9734736, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9734736 11.0347576)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348015, 76.9736285, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9736285 11.0348015)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344701, 76.9735399, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9735399 11.0344701)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344965, 76.9736331, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9736331 11.0344965)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344975, 76.9736366, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9736366 11.0344975)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344745, 76.9735556, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9735556 11.0344745)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342614, 76.9738823, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9738823 11.0342614)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342353, 76.973789, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.973789 11.0342353)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342344, 76.9737855, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9737855 11.0342344)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034257, 76.9738665, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9738665 11.034257)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0339079, 76.9737129, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9737129 11.0339079)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0339315, 76.9737961, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9737961 11.0339315)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0339325, 76.9737996, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9737996 11.0339325)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0339095, 76.9737186, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9737186 11.0339095)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0339305, 76.9737925, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9737925 11.0339305)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336232, 76.9737849, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9737849 11.0336232)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336705, 76.973952, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.973952 11.0336705)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336695, 76.9739484, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9739484 11.0336695)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336276, 76.9738006, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9738006 11.0336276)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334139, 76.9741271, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9741271 11.0334139)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333665, 76.9739601, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9739601 11.0333665)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333675, 76.9739636, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9739636 11.0333675)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334095, 76.9741114, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9741114 11.0334095)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333683, 76.9739662, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9739662 11.0333683)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.033061, 76.9739589, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9739589 11.033061)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331055, 76.974116, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.974116 11.0331055)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331045, 76.9741124, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9741124 11.0331045)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330626, 76.9739646, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9739646 11.0330626)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331065, 76.9741195, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9741195 11.0331065)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327752, 76.9740309, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9740309 11.0327752)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328015, 76.974124, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.974124 11.0328015)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328025, 76.9741276, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9741276 11.0328025)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327796, 76.9740466, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9740466 11.0327796)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0367271, 76.973288, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.973288 11.0367271)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0368156, 76.9734369, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9734369 11.0368156)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0368137, 76.9734338, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9734338 11.0368137)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0367354, 76.973302, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.973302 11.0367354)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0366348, 76.9736601, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9736601 11.0366348)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0365465, 76.973511, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.973511 11.0365465)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0365483, 76.9735142, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9735142 11.0365483)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0366265, 76.973646, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.973646 11.0366265)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0362734, 76.9735759, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9735759 11.0362734)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0363566, 76.9737159, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9737159 11.0363566)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0363547, 76.9737128, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9737128 11.0363547)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0362764, 76.973581, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.973581 11.0362764)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0360378, 76.9737071, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9737071 11.0360378)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0360874, 76.9737901, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9737901 11.0360874)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0360892, 76.9737932, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9737932 11.0360892)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0360462, 76.9737212, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9737212 11.0360462)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0359469, 76.974079, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.974079 11.0359469)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0358976, 76.9739959, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9739959 11.0358976)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0358957, 76.9739928, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9739928 11.0358957)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0359386, 76.974065, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974065 11.0359386)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0355847, 76.9739957, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9739957 11.0355847)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0356285, 76.97407, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.97407 11.0356285)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0356304, 76.9740731, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9740731 11.0356304)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0355877, 76.9740008, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9740008 11.0355877)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353488, 76.9741261, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9741261 11.0353488)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0354376, 76.9742749, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9742749 11.0354376)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0354358, 76.9742718, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9742718 11.0354358)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353572, 76.9741402, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9741402 11.0353572)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352579, 76.974498, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.974498 11.0352579)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0351694, 76.9743491, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9743491 11.0351694)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0351713, 76.9743522, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9743522 11.0351713)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352496, 76.974484, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974484 11.0352496)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348955, 76.9744149, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9744149 11.0348955)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349785, 76.974555, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.974555 11.0349785)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349767, 76.9745518, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9745518 11.0349767)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348985, 76.97442, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.97442 11.0348985)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346611, 76.974545, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.974545 11.0346611)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347104, 76.9746281, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9746281 11.0347104)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347123, 76.9746312, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9746312 11.0347123)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346694, 76.974559, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974559 11.0346694)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345689, 76.974917, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.974917 11.0345689)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345196, 76.9748339, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9748339 11.0345196)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345177, 76.9748308, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9748308 11.0345177)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345606, 76.974903, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974903 11.0345606)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335318, 76.9747114, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9747114 11.0335318)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336605, 76.9748264, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9748264 11.0336605)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0336578, 76.974824, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.974824 11.0336578)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335439, 76.9747222, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9747222 11.0335439)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335953, 76.9750476, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9750476 11.0335953)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334665, 76.9749326, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9749326 11.0334665)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334692, 76.974935, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.974935 11.0334692)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335831, 76.9750368, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9750368 11.0335831)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332657, 76.975032, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.975032 11.0332657)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333864, 76.9751405, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9751405 11.0333864)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333837, 76.9751381, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9751381 11.0333837)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332701, 76.975036, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975036 11.0332701)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333891, 76.975143, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.975143 11.0333891)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331208, 76.9751814, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9751814 11.0331208)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331925, 76.9752456, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9752456 11.0331925)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331952, 76.975248, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.975248 11.0331952)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331329, 76.9751922, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9751922 11.0331329)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331846, 76.9755172, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9755172 11.0331846)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331126, 76.9754533, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9754533 11.0331126)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331098, 76.9754509, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9754509 11.0331098)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0331724, 76.9755064, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9755064 11.0331724)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328555, 76.9755023, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9755023 11.0328555)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0329195, 76.9755596, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9755596 11.0329195)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0329222, 76.975562, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.975562 11.0329222)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328599, 76.9755062, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9755062 11.0328599)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0329168, 76.9755571, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9755571 11.0329168)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.032711, 76.9756521, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9756521 11.032711)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328394, 76.9757675, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9757675 11.0328394)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328367, 76.9757651, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9757651 11.0328367)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327231, 76.975663, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975663 11.0327231)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327743, 76.9759876, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9759876 11.0327743)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0326455, 76.9758726, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9758726 11.0326455)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0326482, 76.975875, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.975875 11.0326482)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327621, 76.9759768, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9759768 11.0327621)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324445, 76.9759723, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9759723 11.0324445)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325655, 76.9760804, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9760804 11.0325655)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325628, 76.976078, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.976078 11.0325628)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324489, 76.9759762, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9759762 11.0324489)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325682, 76.9760829, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9760829 11.0325682)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0322998, 76.9761224, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9761224 11.0322998)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323715, 76.9761866, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9761866 11.0323715)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323742, 76.976189, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.976189 11.0323742)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323119, 76.9761332, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9761332 11.0323119)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.038118, 76.9746069, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9746069 11.038118)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0382233, 76.9744696, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9744696 11.0382233)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0382211, 76.9744725, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9744725 11.0382211)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0381279, 76.974594, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974594 11.0381279)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.038422, 76.9745031, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9745031 11.038422)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0383167, 76.9746404, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9746404 11.0383167)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0383189, 76.9746375, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9746375 11.0383189)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0384121, 76.974516, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974516 11.0384121)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0384043, 76.9748187, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9748187 11.0384043)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385033, 76.9746896, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9746896 11.0385033)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385011, 76.9746925, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9746925 11.0385011)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0384079, 76.974814, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974814 11.0384079)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385055, 76.9746867, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9746867 11.0385055)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.038538, 76.9749369, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9749369 11.038538)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385967, 76.9748604, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9748604 11.0385967)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385989, 76.9748575, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9748575 11.0385989)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0385479, 76.974924, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974924 11.0385479)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.038842, 76.9748331, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9748331 11.038842)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0387833, 76.9749096, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9749096 11.0387833)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0387811, 76.9749125, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9749125 11.0387811)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388321, 76.974846, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974846 11.0388321)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388243, 76.9751487, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9751487 11.0388243)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388767, 76.9750804, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9750804 11.0388767)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388789, 76.9750775, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9750775 11.0388789)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388279, 76.975144, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975144 11.0388279)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0388745, 76.9750833, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9750833 11.0388745)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.038958, 76.9752669, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9752669 11.038958)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0390633, 76.9751296, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9751296 11.0390633)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0390611, 76.9751325, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9751325 11.0390611)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0389679, 76.975254, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975254 11.0389679)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.039262, 76.9751631, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9751631 11.039262)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0391567, 76.9753004, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9753004 11.0391567)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0391589, 76.9752975, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9752975 11.0391589)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0392521, 76.975176, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.975176 11.0392521)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0392443, 76.9754787, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9754787 11.0392443)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393433, 76.9753496, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9753496 11.0393433)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393411, 76.9753525, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9753525 11.0393411)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0392479, 76.975474, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975474 11.0392479)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393455, 76.9753467, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9753467 11.0393455)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.039378, 76.9755969, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9755969 11.039378)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0394367, 76.9755204, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9755204 11.0394367)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0394389, 76.9755175, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9755175 11.0394389)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393879, 76.975584, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.975584 11.0393879)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.039682, 76.9754931, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9754931 11.039682)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0396233, 76.9755696, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9755696 11.0396233)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0396211, 76.9755725, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9755725 11.0396211)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0396721, 76.975506, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.975506 11.0396721)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034388, 76.9720064, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9720064 11.034388)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034528, 76.9719057, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9719057 11.034528)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034525, 76.9719079, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9719079 11.034525)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344011, 76.9719969, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9719969 11.0344011)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346931, 76.9719736, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9719736 11.0346931)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034553, 76.9720743, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9720743 11.034553)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034556, 76.9720721, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9720721 11.034556)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346799, 76.9719831, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9719831 11.0346799)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345701, 76.9722479, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9722479 11.0345701)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347021, 76.9721539, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9721539 11.0347021)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346991, 76.972156, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972156 11.0346991)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345749, 76.9722445, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9722445 11.0345749)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034649, 76.9723793, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9723793 11.034649)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034727, 76.9723233, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9723233 11.034727)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.03473, 76.9723211, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9723211 11.03473)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0346621, 76.9723699, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9723699 11.0346621)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349545, 76.9723472, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9723472 11.0349545)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348761, 76.9724029, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9724029 11.0348761)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348731, 76.972405, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972405 11.0348731)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349412, 76.9723566, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9723566 11.0349412)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348304, 76.9726213, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9726213 11.0348304)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349, 76.9725713, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9725713 11.0349)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.034903, 76.9725691, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9725691 11.034903)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348351, 76.9726179, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9726179 11.0348351)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349087, 76.9727509, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9727509 11.0349087)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350491, 76.9726509, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9726509 11.0350491)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350461, 76.972653, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972653 11.0350461)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0349219, 76.9727415, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9727415 11.0349219)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352141, 76.9727196, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9727196 11.0352141)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035074, 76.9728203, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9728203 11.035074)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035077, 76.9728181, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9728181 11.035077)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352009, 76.9727291, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9727291 11.0352009)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350914, 76.9729943, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9729943 11.0350914)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035223, 76.9728997, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9728997 11.035223)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.03522, 76.9729019, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9729019 11.03522)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350961, 76.9729909, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9729909 11.0350961)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.03517, 76.9731244, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9731244 11.03517)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035248, 76.9730683, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9730683 11.035248)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035251, 76.9730661, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9730661 11.035251)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0351831, 76.9731149, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9731149 11.0351831)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374092, 76.9806089, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9806089 11.0374092)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375797, 76.9805885, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9805885 11.0375797)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375761, 76.9805889, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9805889 11.0375761)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374252, 76.980607, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.980607 11.0374252)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376958, 76.9807571, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9807571 11.0376958)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375253, 76.9807775, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9807775 11.0375253)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375289, 76.9807771, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9807771 11.0375289)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376798, 76.980759, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.980759 11.0376798)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374614, 76.9809676, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9809676 11.0374614)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376217, 76.9809485, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9809485 11.0376217)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376181, 76.9809489, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9809489 11.0376181)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374672, 76.980967, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.980967 11.0374672)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376253, 76.9809481, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9809481 11.0376253)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374722, 76.9811488, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9811488 11.0374722)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375673, 76.9811375, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9811375 11.0375673)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375709, 76.9811371, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9811371 11.0375709)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0374882, 76.9811469, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9811469 11.0374882)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377588, 76.9812981, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9812981 11.0377588)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376637, 76.9813095, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9813095 11.0376637)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376601, 76.9813099, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9813099 11.0376601)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377428, 76.9813, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9813 11.0377428)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375244, 76.9815086, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9815086 11.0375244)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376093, 76.9814985, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9814985 11.0376093)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376129, 76.9814981, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9814981 11.0376129)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375302, 76.981508, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.981508 11.0375302)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376057, 76.9814989, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9814989 11.0376057)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375353, 76.9816906, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9816906 11.0375353)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377057, 76.9816693, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9816693 11.0377057)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377021, 76.9816697, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9816697 11.0377021)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375513, 76.9816886, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9816886 11.0375513)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378229, 76.9818381, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9818381 11.0378229)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376523, 76.9818585, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9818585 11.0376523)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376559, 76.9818581, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9818581 11.0376559)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378068, 76.98184, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.98184 11.0378068)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375884, 76.9820486, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9820486 11.0375884)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377487, 76.9820295, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9820295 11.0377487)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377451, 76.9820299, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9820299 11.0377451)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375942, 76.982048, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.982048 11.0375942)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377523, 76.9820291, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9820291 11.0377523)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0375992, 76.9822298, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9822298 11.0375992)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376943, 76.9822185, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9822185 11.0376943)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376979, 76.9822181, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9822181 11.0376979)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376152, 76.9822279, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9822279 11.0376152)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378859, 76.9823791, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9823791 11.0378859)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377907, 76.9823905, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9823905 11.0377907)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377871, 76.9823909, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9823909 11.0377871)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378698, 76.982381, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.982381 11.0378698)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376514, 76.9825896, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9825896 11.0376514)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377363, 76.9825795, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9825795 11.0377363)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377399, 76.9825791, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9825791 11.0377399)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376572, 76.982589, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.982589 11.0376572)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0377327, 76.9825799, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9825799 11.0377327)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376622, 76.9827709, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9827709 11.0376622)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378327, 76.9827505, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9827505 11.0378327)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0378291, 76.9827509, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9827509 11.0378291)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0376782, 76.982769, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.982769 11.0376782)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281775, 76.9724502, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9724502 11.0281775)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0283361, 76.9725167, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9725167 11.0283361)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0283328, 76.9725153, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9725153 11.0283328)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281924, 76.9724565, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9724565 11.0281924)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0282718, 76.9724897, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9724897 11.0282718)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0283186, 76.9728128, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9728128 11.0283186)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281599, 76.9727463, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9727463 11.0281599)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281632, 76.9727477, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9727477 11.0281632)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0283036, 76.9728065, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9728065 11.0283036)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281658, 76.9727487, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9727487 11.0281658)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279747, 76.9729727, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9729727 11.0279747)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281242, 76.9730345, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9730345 11.0281242)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281208, 76.9730332, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9730332 11.0281208)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279802, 76.972975, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.972975 11.0279802)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0281275, 76.9730359, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9730359 11.0281275)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0278605, 76.9732282, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9732282 11.0278605)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279489, 76.9732653, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9732653 11.0279489)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279522, 76.9732667, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9732667 11.0279522)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0278754, 76.9732345, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9732345 11.0278754)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0280016, 76.9735908, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9735908 11.0280016)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279131, 76.9735537, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9735537 11.0279131)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279098, 76.9735523, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9735523 11.0279098)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0279866, 76.9735845, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9735845 11.0279866)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.027658, 76.9737502, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9737502 11.027658)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0277369, 76.9737833, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9737833 11.0277369)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0277402, 76.9737847, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9737847 11.0277402)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0276634, 76.9737525, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9737525 11.0276634)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0277336, 76.9737819, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9737819 11.0277336)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0275422, 76.9740058, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9740058 11.0275422)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0277012, 76.9740715, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9740715 11.0277012)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0276978, 76.9740702, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9740702 11.0276978)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0275572, 76.974012, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974012 11.0275572)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0276846, 76.9743688, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9743688 11.0276846)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0275259, 76.9743023, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9743023 11.0275259)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0275292, 76.9743037, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9743037 11.0275292)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0276696, 76.9743625, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9743625 11.0276696)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0275318, 76.9743047, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9743047 11.0275318)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.027341, 76.9745282, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9745282 11.027341)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0274901, 76.9745907, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9745907 11.0274901)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0274868, 76.9745893, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9745893 11.0274868)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0273464, 76.9745305, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9745305 11.0273464)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0274934, 76.9745921, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9745921 11.0274934)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0272254, 76.9747832, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9747832 11.0272254)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0273139, 76.9748203, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9748203 11.0273139)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0273172, 76.9748217, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9748217 11.0273172)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0272404, 76.9747895, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9747895 11.0272404)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353588, 76.9740313, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9740313 11.0353588)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0354078, 76.9741978, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9741978 11.0354078)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0354068, 76.9741943, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9741943 11.0354068)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0353635, 76.974047, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974047 11.0353635)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.035388, 76.9741303, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9741303 11.035388)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352685, 76.974341, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.974341 11.0352685)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352204, 76.9741741, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9741741 11.0352204)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352214, 76.9741776, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9741776 11.0352214)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352639, 76.9743252, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9743252 11.0352639)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0352221, 76.9741802, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9741802 11.0352221)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350298, 76.9741403, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9741403 11.0350298)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350758, 76.9742968, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9742968 11.0350758)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350748, 76.9742933, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9742933 11.0350748)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350315, 76.974146, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974146 11.0350315)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0350769, 76.9743004, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9743004 11.0350769)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348608, 76.9741803, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9741803 11.0348608)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348882, 76.9742732, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9742732 11.0348882)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348892, 76.9742767, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9742767 11.0348892)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0348655, 76.974196, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974196 11.0348655)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347702, 76.97449, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.97449 11.0347702)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347436, 76.9743969, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9743969 11.0347436)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347426, 76.9743934, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9743934 11.0347426)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0347657, 76.9744743, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9744743 11.0347657)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345308, 76.9742893, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9742893 11.0345308)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345552, 76.9743722, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9743722 11.0345552)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345562, 76.9743757, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9743757 11.0345562)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345325, 76.974295, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974295 11.0345325)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0345541, 76.9743686, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9743686 11.0345541)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0343618, 76.9743293, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9743293 11.0343618)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344108, 76.9744958, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9744958 11.0344108)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0344098, 76.9744923, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9744923 11.0344098)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0343665, 76.974345, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974345 11.0343665)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342715, 76.974639, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.974639 11.0342715)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342234, 76.9744721, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9744721 11.0342234)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342244, 76.9744756, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9744756 11.0342244)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342669, 76.9746232, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9746232 11.0342669)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0342251, 76.9744782, 3.5, 'Right of Roadway', ST_GeomFromText('POINT(76.9744782 11.0342251)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0340328, 76.9744383, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9744383 11.0340328)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0340788, 76.9745948, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9745948 11.0340788)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0340778, 76.9745913, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9745913 11.0340778)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0340345, 76.974444, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974444 11.0340345)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0340799, 76.9745984, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9745984 11.0340799)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0338638, 76.9744783, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9744783 11.0338638)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0338912, 76.9745712, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9745712 11.0338912)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0338922, 76.9745747, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9745747 11.0338922)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0338685, 76.974494, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974494 11.0338685)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337742, 76.9747877, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9747877 11.0337742)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337468, 76.9746948, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9746948 11.0337468)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337458, 76.9746913, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9746913 11.0337458)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337695, 76.974772, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974772 11.0337695)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335354, 76.9745881, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9745881 11.0335354)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335594, 76.9746711, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9746711 11.0335594)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335604, 76.9746746, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9746746 11.0335604)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335371, 76.9745938, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9745938 11.0335371)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0335584, 76.9746676, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9746676 11.0335584)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333658, 76.9746273, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9746273 11.0333658)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334148, 76.9747938, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9747938 11.0334148)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0334138, 76.9747903, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9747903 11.0334138)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333705, 76.974643, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974643 11.0333705)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332762, 76.9749367, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9749367 11.0332762)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332272, 76.9747702, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9747702 11.0332272)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332282, 76.9747737, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9747737 11.0332282)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332715, 76.974921, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.974921 11.0332715)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330376, 76.974737, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.974737 11.0330376)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330826, 76.9748939, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9748939 11.0330826)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330816, 76.9748904, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9748904 11.0330816)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330393, 76.9747427, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9747427 11.0330393)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0330836, 76.9748974, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9748974 11.0330836)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328668, 76.9747763, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9747763 11.0328668)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328942, 76.9748692, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9748692 11.0328942)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328952, 76.9748727, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9748727 11.0328952)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328715, 76.974792, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974792 11.0328715)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327772, 76.9750857, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9750857 11.0327772)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327498, 76.9749928, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9749928 11.0327498)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327488, 76.9749893, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9749893 11.0327488)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0327725, 76.97507, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.97507 11.0327725)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325384, 76.9748861, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9748861 11.0325384)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325624, 76.9749691, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9749691 11.0325624)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325634, 76.9749726, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9749726 11.0325634)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325401, 76.9748918, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9748918 11.0325401)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0325614, 76.9749656, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9749656 11.0325614)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323688, 76.9749253, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9749253 11.0323688)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324178, 76.9750918, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9750918 11.0324178)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324168, 76.9750883, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9750883 11.0324168)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323735, 76.974941, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.974941 11.0323735)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0322792, 76.9752347, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9752347 11.0322792)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0322302, 76.9750682, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9750682 11.0322302)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0322312, 76.9750717, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9750717 11.0322312)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0322745, 76.975219, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.975219 11.0322745)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0391159, 76.9723052, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9723052 11.0391159)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0392239, 76.9721701, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9721701 11.0392239)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0392216, 76.972173, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972173 11.0392216)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0391261, 76.9722925, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9722925 11.0391261)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0395041, 76.9722747, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9722747 11.0395041)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393961, 76.9724099, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9724099 11.0393961)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0393984, 76.972407, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.972407 11.0393984)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0394939, 76.9722875, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9722875 11.0394939)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0395624, 76.9726571, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9726571 11.0395624)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0396639, 76.9725301, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9725301 11.0396639)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0396616, 76.972533, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972533 11.0396616)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0395661, 76.9726525, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9726525 11.0395661)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0397759, 76.9728452, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9728452 11.0397759)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0398361, 76.9727699, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9727699 11.0398361)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0398384, 76.972767, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.972767 11.0398384)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0397861, 76.9728325, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9728325 11.0397861)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0401641, 76.9728147, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9728147 11.0401641)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0401039, 76.9728901, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9728901 11.0401039)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0401016, 76.972893, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.972893 11.0401016)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0401539, 76.9728275, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9728275 11.0401539)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0402224, 76.9731971, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9731971 11.0402224)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0402761, 76.9731299, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9731299 11.0402761)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0402784, 76.973127, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.973127 11.0402784)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0402261, 76.9731925, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9731925 11.0402261)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0310201, 76.9786208, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9786208 11.0310201)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0310726, 76.9784554, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9784554 11.0310726)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0310715, 76.9784589, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9784589 11.0310715)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.031025, 76.9786053, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9786053 11.031025)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0315539, 76.9785101, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9785101 11.0315539)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0315014, 76.9786756, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9786756 11.0315014)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0315025, 76.9786721, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9786721 11.0315025)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.031549, 76.9785257, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9785257 11.031549)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.031927, 76.9789048, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9789048 11.031927)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0319767, 76.9787494, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9787494 11.0319767)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0319756, 76.9787529, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9787529 11.0319756)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0319288, 76.9788992, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9788992 11.0319288)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0319778, 76.9787459, -4.6, 'Left of Roadway', ST_GeomFromText('POINT(76.9787459 11.0319778)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323762, 76.9790629, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9790629 11.0323762)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324054, 76.9789706, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9789706 11.0324054)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0324065, 76.9789671, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9789671 11.0324065)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0323811, 76.9790473, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9790473 11.0323811)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0329109, 76.9789521, -14.79, 'Left of Roadway', ST_GeomFromText('POINT(76.9789521 11.0329109)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328816, 76.9790444, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9790444 11.0328816)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0328805, 76.9790479, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9790479 11.0328805)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.032906, 76.9789677, -13.0, 'Left of Roadway', ST_GeomFromText('POINT(76.9789677 11.032906)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0332842, 76.9793469, 13.65, 'Right of Roadway', ST_GeomFromText('POINT(76.9793469 11.0332842)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333104, 76.9792646, 4.2, 'Right of Roadway', ST_GeomFromText('POINT(76.9792646 11.0333104)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333115, 76.9792611, 3.8, 'Right of Roadway', ST_GeomFromText('POINT(76.9792611 11.0333115)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.033286, 76.9793413, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9793413 11.033286)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0333093, 76.9792681, 4.6, 'Right of Roadway', ST_GeomFromText('POINT(76.9792681 11.0333093)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337331, 76.9795039, 14.79, 'Right of Roadway', ST_GeomFromText('POINT(76.9795039 11.0337331)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337856, 76.9793384, -4.2, 'Left of Roadway', ST_GeomFromText('POINT(76.9793384 11.0337856)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.0337845, 76.9793419, -3.8, 'Left of Roadway', ST_GeomFromText('POINT(76.9793419 11.0337845)', 4326))
ON CONFLICT (asset_id) DO NOTHING;
INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('None', '', 'None', '', '', '', '', 11.033738, 76.9794883, 13.0, 'Right of Roadway', ST_GeomFromText('POINT(76.9794883 11.033738)', 4326))
ON CONFLICT (asset_id) DO NOTHING;