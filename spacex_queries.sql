-- SQL queries to analyze SpaceX launch data
-- Run these queries using the SQLite database (my_data1.db)

-- 1. Success rate by launch site
SELECT LaunchSite,
       COUNT(*) as total_launches,
       SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) as successes,
       ROUND(SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as success_rate_pct
FROM (
    SELECT LaunchSite, Class FROM dataset_part_2
)
GROUP BY LaunchSite
ORDER BY total_launches DESC;

-- 2. Success rate by orbit type
SELECT Orbit,
       COUNT(*) as total_launches,
       SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) as successes,
       ROUND(SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as success_rate_pct
FROM dataset_part_2
GROUP BY Orbit
ORDER BY total_launches DESC;

-- 3. Payload mass analysis by outcome
SELECT 
    CASE WHEN Class = '1' THEN 'Success' ELSE 'Failure' END as outcome,
    COUNT(*) as count,
    ROUND(AVG(PayloadMass), 2) as avg_payload_kg,
    ROUND(MIN(PayloadMass), 2) as min_payload_kg,
    ROUND(MAX(PayloadMass), 2) as max_payload_kg
FROM dataset_part_2
WHERE PayloadMass IS NOT NULL
GROUP BY Class;

-- 4. Launch success trend over years
SELECT strftime('%Y', Date) as launch_year,
       COUNT(*) as total_launches,
       SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) as successes,
       ROUND(SUM(CASE WHEN Class = '1' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as success_rate_pct
FROM dataset_part_2
WHERE Date IS NOT NULL
GROUP BY strftime('%Y', Date)
ORDER BY launch_year;

-- 5. Booster version performance (join with spacex_launch_dash)
SELECT d.BoosterVersion as booster,
       COUNT(*) as total_launches,
       SUM(CASE WHEN d.Class = '1' THEN 1 ELSE 0 END) as successes,
       ROUND(SUM(CASE WHEN d.Class = '1' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as success_rate_pct
FROM dataset_part_2 d
GROUP BY d.BoosterVersion
ORDER BY total_launches DESC
LIMIT 10;
