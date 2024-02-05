-- TASK7. SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avge_score DECIMAL(10, 2);  -- Use DECIMAL for average score

    -- Calculate average score for the user
    SELECT AVG(score) INTO avge_score FROM corrections WHERE user_id = user_id;

    -- Update users table with the calculated average score
    UPDATE users SET average_score = avge_score WHERE id = user_id;
END;
//
delimiter ;


