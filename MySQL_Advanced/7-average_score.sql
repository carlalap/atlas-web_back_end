-- TASK7. SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score INT;
    DECLARE number_of_corrections INT;
    DECLARE avge_score FLOAT;

    -- Calculate total Score for the user
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
    -- Calculate the number of corrections for the user
    SELECT COUNT(*) INTO number_of_corrections FROM corrections where user_id =  user_id;

    IF number_of_corrections > 0 THEN
        -- cALculate average score
        SET avge_score = total_score / number_of_corrections;

        -- Update user average score in the users table
        UPDATE users SET average_score = avge_score WHERE id = user_id;
    END IF;
END;
//
delimiter;

