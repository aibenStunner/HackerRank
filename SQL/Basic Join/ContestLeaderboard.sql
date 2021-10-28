/*
Enter your query here.
*/
SET sql_mode = '';

SELECT H.HACKER_ID, H.NAME, SUM(SCORE) AS TOTAL_SCORE FROM HACKERS H   
    INNER JOIN 
    -- filter out maximum scores from challenges for each hacker
    (SELECT HACKER_ID, MAX(SCORE) AS SCORE FROM SUBMISSIONS GROUP BY CHALLENGE_ID, HACKER_ID) MAX_SCORE
        ON H.HACKER_ID = MAX_SCORE.HACKER_ID    
    GROUP BY H.HACKER_ID, H.NAME
    
    -- filter out total scores less than 0
    HAVING TOTAL_SCORE > 0
    
    -- order the results
    ORDER BY TOTAL_SCORE DESC, H.HACKER_ID;