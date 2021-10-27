/*
Enter your query here.
*/
SET sql_mode='';
-- columns to output
SELECT H.HACKER_ID, H.NAME, COUNT(H.HACKER_ID) AS TOTAL_CHALLENGES FROM HACKERS H
    -- joining to get the required output
    INNER JOIN CHALLENGES C
        ON H.HACKER_ID = C.HACKER_ID
    -- grouping them by the hacker_id
    GROUP BY H.HACKER_ID
    
    -- selecting which hackers we wish to output
    -- we need to filter the hackers according to the constraints given
    HAVING 
        -- output hackers with challenges count equal to the maximum count
        TOTAL_CHALLENGES = 
                 -- the maximum challenges count that any hacker has had
                 (SELECT MAX(TEMP.CNT) FROM 
                        (SELECT COUNT(*) AS CNT FROM CHALLENGES
                        GROUP BY HACKER_ID) TEMP)
        -- output hackers with challenges count in the specified range              
        OR TOTAL_CHALLENGES IN
                -- the set of counts
                (SELECT TEMP_2.CNT FROM 
                    (SELECT COUNT(*) AS CNT FROM CHALLENGES
                    GROUP BY HACKER_ID) TEMP_2
                 -- group the set of counts
                GROUP BY TEMP_2.CNT
                 -- has only one element
                HAVING COUNT(TEMP_2.CNT) = 1)
    ORDER BY TOTAL_CHALLENGES DESC, C.HACKER_ID;