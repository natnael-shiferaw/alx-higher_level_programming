-- List records with a score >= 10 from the 'second_table' in the 'hbtn_0c_0' database on your MySQL server
SELECT score,
    name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
