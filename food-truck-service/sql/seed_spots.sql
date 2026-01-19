INSERT INTO spots (name, lat, lon, radius)
VALUES
    ('Downtown Lunch', 37.774900, -122.419400, 250),
    ('Waterfront Dinner', 37.799300, -122.397700, 300)
ON CONFLICT DO NOTHING;
