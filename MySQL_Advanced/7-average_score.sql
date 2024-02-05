-- TASK7. SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE number_of_corrections INT;
    DECLARE avge_score FLOAT;

    -- Calculate total Score for the user
    SELECT AVG(score) INTO number_of_corrections FROM corrections WHERE user_id = corrections.user_id.user_id;
    -- Calculate the number of corrections for the user
    UPDATE users SET average_score = avge_score WHERE id = user_id;
END;
//
delimiter;

