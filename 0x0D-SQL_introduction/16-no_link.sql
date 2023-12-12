-- List all records from the 'second_table' in the 'hbtn_0c_0' database on your MySQL server, excluding those with a NULL name
SELECT score,
    name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
