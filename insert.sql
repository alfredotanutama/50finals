-- Drop the table if it exists
DROP TABLE IF EXISTS Ingredients;

-- Create the Ingredients table
CREATE TABLE Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    indonesian_name TEXT NOT NULL,
    price REAL NOT NULL  -- Just define the column as price
);

-- Insert data into the Ingredients table
INSERT INTO Ingredients (ingredient, indonesian_name, price) VALUES
('Premium Rice', 'Beras Premium', 15042.50),
('Medium Rice', 'Beras Medium', 13053.75),
('Shallots', 'Bawang Merah', 43788.75),
('Garlic Bulbs', 'Bawang Putih', 41753.75),
('Curly Red Chili', 'Cabe Keriting', 31402.50),
('Chili', 'Cabe Rawit', 43973.75),
('Pure Beef', 'Daging Sapi Murni', 136185.00),
('Broiler Chicken', 'Ayam Broiler', 37676.25),
('Broiler Chicken Eggs', 'Telur Ayam Broiler', 27511.25),
('Simple Packaged Cooking Oil', 'Minyak Goreng Kemasan Sederhana', 18456.25),
('Bulk Cooking Oil', 'Minyak Goreng Curah', 17070.00),
('Mackerel Fish', 'Ikan Makarel', 35245.00),
('Skipjack Tuna', 'Ikan Tuna', 35716.25),
('Milkfish', 'Ikan Bandeng', 41362.50),
('Iodized Fine Salt', 'Garam Halus Iodium', 11753.75);

SELECT 
    id, 
    ingredient, 
    indonesian_name, 
    price AS "Price (IDR)"  -- Use an alias for display purposes
FROM 
    Ingredients;