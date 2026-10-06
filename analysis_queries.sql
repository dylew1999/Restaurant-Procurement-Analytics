SELECT * FROM purchases LIMIT 5;
SELECT COUNT(*) FROM purchases;

-- Q1: Top 10 items, with share of total spend
SELECT item, SUM(total_price) AS spend, ROUND(100.0 * SUM(total_price) / (SELECT SUM(total_price) FROM purchases),1) AS pct
FROM purchases
GROUP BY item
ORDER BY spend DESC
LIMIT 10;

-- q2 supplier concentration
SELECT supplier, SUM(total_price) AS spend, ROUND(100.0 * SUM(total_price) / (SELECT SUM(total_price) FROM purchases),1) AS pct
FROM purchases
GROUP BY supplier
ORDER BY spend DESC
LIMIT 10;

-- q3 monthly chicken price(weighted)
SELECT strftime('%m', date) AS month,
				ROUND(SUM(total_price)/ SUM(quantity),2) as  price_per_kg
FROM purchases
WHERE item = 'Ayam'
GROUP BY month
ORDER BY month;