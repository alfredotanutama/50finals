import sqlite3

connection = sqlite3.connect('ingredients.db')
cursor = connection.cursor