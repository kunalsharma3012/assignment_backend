DROP TABLE IF EXISTS campaigns;

CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL,         -- 'Active' or 'Paused'
    clicks INTEGER NOT NULL,
    cost REAL NOT NULL,
    impressions INTEGER NOT NULL
);

INSERT INTO campaigns (id, name, status, clicks, cost, impressions) VALUES
(1, 'Summer Sale',        'Active', 150, 45.99, 1000),
(2, 'Black Friday',       'Paused', 320, 89.50, 2500),
(3, 'Diwali Blast',       'Active', 210, 60.00, 1800),
(4, 'New Year Push',      'Paused', 90,  30.25,  900),
(5, 'Winter Clearance',   'Active', 400, 120.75, 5000),
(6, 'Monsoon Offer',      'Active', 175, 50.10, 2000),
(7, 'Festive Sale',       'Paused', 60,  15.99,  600),
(8, 'App Install Drive',  'Active', 520, 200.00, 8000),
(9, 'Retargeting Test',   'Paused', 45,  10.50,  450),
(10,'Brand Awareness',    'Active', 300, 99.99, 7000);
