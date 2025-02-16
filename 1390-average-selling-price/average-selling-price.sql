WITH Sales AS (
    SELECT 
        u.product_id, 
        u.units, 
        p.price
    FROM UnitsSold u
    JOIN Prices p 
    ON u.product_id = p.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
),
Aggregated AS (
    SELECT 
        s.product_id,
        SUM(s.units * s.price) AS total_revenue,
        SUM(s.units) AS total_units
    FROM Sales s
    GROUP BY s.product_id
)
SELECT 
    p.product_id,
    COALESCE(ROUND(total_revenue / NULLIF(total_units, 0), 2), 0) AS average_price
FROM Prices p
LEFT JOIN Aggregated a
ON p.product_id = a.product_id
GROUP BY p.product_id;
