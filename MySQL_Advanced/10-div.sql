--task10. Safe divide
-- SQL script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER //

CREATE function SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result INT;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END
//
DELIMITER;