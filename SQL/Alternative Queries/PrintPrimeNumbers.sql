/*
Enter your query here.
*/
SET @potential_prime = 1;
SET @divisor = 1;

SELECT GROUP_CONCAT(POTENTIAL_PRIME SEPARATOR '&') FROM
    (SELECT @potential_prime := @potential_prime + 1 AS POTENTIAL_PRIME FROM
    information_schema.tables t1,
    information_schema.tables t2
    LIMIT 1000) list_of_potential_primes
WHERE NOT EXISTS(
    SELECT * FROM
        (SELECT @divisor := @divisor + 1 AS DIVISOR FROM
        information_schema.tables t4,
        information_schema.tables t5
        LIMIT 1000) list_of_divisors
    WHERE MOD(POTENTIAL_PRIME, DIVISOR) = 0 AND POTENTIAL_PRIME <> DIVISOR);