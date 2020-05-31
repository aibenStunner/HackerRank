/*
Enter your query here.
*/
SET sql_mode = '';
SELECT H.hacker_id, H.name FROM submissions S
    JOIN challenges C
        ON S.challenge_id = C.challenge_id
    JOIN difficulty D
        ON C.difficulty_level = D.difficulty_level
    JOIN hackers H
        ON S.hacker_id = H.hacker_id
    WHERE S.score = D.score
        AND C.difficulty_level = D.difficulty_level
    GROUP BY H.hacker_id
        HAVING COUNT(S.hacker_id) > 1
    ORDER BY COUNT(S.hacker_id) DESC, S.hacker_id ASC;
