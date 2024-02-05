-- Create a trigger that decreases the quantity of an item
-- after inserting a new order
DELIMITER //
CREATE TRIGGER decrease_quantity_item
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update quantity in the items table
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER;