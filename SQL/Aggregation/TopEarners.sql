/*
Enter your query here.
*/
SELECT (months*salary) AS earnings, COUNT(*) FROM Employee GROUP BY earnings ORDER BY earnings DESC LIMIT 1;