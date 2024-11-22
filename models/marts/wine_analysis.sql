SELECT country, AVG(price) AS avg_price
FROM wine_data
GROUP BY country
