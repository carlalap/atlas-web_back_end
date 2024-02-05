-- TASK7. SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    -- Calculate average score for the user
    UPDATE users 
    SET average_score=(SELECT AVG(score) FROM corrections AS user WHERE user.user_id=user_id)
    WHERE id=user_id;
END;
//
DELIMITER;


