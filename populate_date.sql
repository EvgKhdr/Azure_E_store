DECLARE @StartDate DATE = '2022-01-01';
DECLARE @EndDate DATE = '2027-01-01';

TRUNCATE TABLE dw.date_d;

WITH DateSequence AS (
    SELECT @StartDate AS CurrentDate
    UNION ALL
    SELECT DATEADD(day, 1, CurrentDate)
    FROM DateSequence
    WHERE CurrentDate < @EndDate
)
INSERT INTO dw.date (full_date, [year], [month], [date], time_of_year, [weekday], is_weekend)
SELECT 
    CurrentDate AS full_date,
    YEAR(CurrentDate) AS [year],
    MONTH(CurrentDate) AS [month],
    DAY(CurrentDate) AS [date],

    CASE 
        WHEN MONTH(CurrentDate) IN (12, 1, 2) THEN 'Winter'
        WHEN MONTH(CurrentDate) IN (3, 4, 5) THEN 'Spring'
        WHEN MONTH(CurrentDate) IN (6, 7, 8) THEN 'Summer'
        ELSE 'Autumn' 
    END AS time_of_year,
    DATENAME(weekday, CurrentDate) AS [weekday],
    CASE WHEN DATEPART(weekday, CurrentDate) IN (1, 7) THEN 1 ELSE 0 END AS is_weekend
FROM DateSequence
OPTION (MAXRECURSION 0);