-- stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SET avg_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
	IF avg_score IS NULL THEN
		SET avg_score = 0;
	END IF;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;