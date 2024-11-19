-- Trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$
CREATE TRIGGER ins_sum AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET items.quantity = items.quantity - NEW.number
WHERE items.name = NEW.item_name$$
DELIMITER ;

