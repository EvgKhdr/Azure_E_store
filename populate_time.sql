TRUNCATE TABLE dw.time_d;
WITH 
t10 AS (SELECT n FROM (VALUES (0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) v(n)),
SecondsSequence AS (
    SELECT (a.n + b.n*10 + c.n*100 + d.n*1000 + e.n*10000) AS SecOffset
    FROM t10 a 
    CROSS JOIN t10 b
    CROSS JOIN t10 c
    CROSS JOIN t10 d
    CROSS JOIN t10 e
    WHERE (a.n + b.n*10 + c.n*100 + d.n*1000 + e.n*10000) < 86400
),
TimeBase AS (

    SELECT CAST(DATEADD(second, SecOffset, CAST('00:00:00' AS TIME)) AS TIME) AS CalculatedTime
    FROM SecondsSequence
)

INSERT INTO dw.time_d (full_time, hour, minute, second, time_of_day)
SELECT 
    CalculatedTime AS full_time,
    DATEPART(hour, CalculatedTime) AS hour,
    DATEPART(minute, CalculatedTime) AS minute,
    DATEPART(second, CalculatedTime) AS second,
    CASE 
        WHEN DATEPART(hour, CalculatedTime) BETWEEN 6 AND 11  THEN 'Morning'
        WHEN DATEPART(hour, CalculatedTime) BETWEEN 12 AND 17 THEN 'Afternoon'
        WHEN DATEPART(hour, CalculatedTime) BETWEEN 18 AND 21 THEN 'Evening'
        ELSE 'Night' 
    END AS time_of_day    
FROM TimeBase
ORDER BY full_time;