-- Drop the table if it exists
DROP TABLE IF EXISTS Ingredients;

-- Create the Ingredients table
CREATE TABLE Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    indonesian_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL 
);

-- Insert data
INSERT INTO Ingredients (ingredient, indonesian_name, category, price) VALUES
('Premium Rice', 'Beras Premium', 'Rice', 15042.50),
('Medium Rice', 'Beras Medium', 'Rice', 13053.75),
('Shallots', 'Bawang Merah', 'Vegetable', 43788.75),
('Garlic Bulbs', 'Bawang Putih', 'Vegetable', 41753.75),
('Curly Red Chili', 'Cabe Keriting', 'Vegetable', 31402.50),
('Chili', 'Cabe Rawit', 'Vegetable', 43973.75),
('Pure Beef', 'Daging Sapi Murni', 'Protein', 136185.00),
('Broiler Chicken', 'Ayam Broiler', 'Protein', 37676.25),
('Broiler Chicken Eggs', 'Telur Ayam Broiler', 'Protein', 27511.25),
('Simple Packaged Cooking Oil', 'Minyak Goreng Kemasan Sederhana', 'Other', 18456.25),
('Bulk Cooking Oil', 'Minyak Goreng Curah', 'Other', 17070.00),
('Mackerel Fish', 'Ikan Makarel', 'Protein', 35245.00),
('Skipjack Tuna', 'Ikan Tuna', 'Protein', 35716.25),
('Milkfish', 'Ikan Bandeng', 'Protein', 41362.50),
('Iodized Fine Salt', 'Garam Halus Iodium', 'Other', 11753.75);


SELECT 
    id, 
    ingredient, 
    indonesian_name AS "Bahan Pokok", 
    price AS "Price (IDR)",
    category  
FROM 
    Ingredients;