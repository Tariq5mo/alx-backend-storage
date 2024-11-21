-- stored procedure that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN

    DECLARE project_id INT;

    IF EXISTS (SELECT 1 FROM projects WHERE projects.name = project_name)
	THEN
        SET project_id = (SELECT id FROM projects WHERE projects.name=project_name);
            INSERT INTO corrections  (user_id, project_id, score) VALUES (user_id, project_id, score);
    ELSE
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = (SELECT id FROM projects WHERE projects.name=project_name);
        INSERT INTO corrections  (user_id, project_id, score) VALUES (user_id, project_id, score);
    END IF;

END$$
DELIMITER ;
