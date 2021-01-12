CREATE TABLE customers (
	CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
	CustomerName TEXT,
	CustomerPhone TEXT
);

CREATE TABLE products (
	ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
	ProductName TEXT,
	ProductBasePrice INTEGER
);

CREATE TABLE orders (
	OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
	CustomerID INTEGER,
	ProductID INTEGER,
	Discount INTEGER,
	OrderDateTime NUMERIC DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID) ON DELETE CASCADE,
	FOREIGN KEY (ProductID) REFERENCES products(ProductID) ON DELETE CASCADE
);

ALTER TABLE customers ADD COLUMN CustomerEmail;

INSERT INTO customers (CustomerName, CustomerPhone, CustomerEmail) VALUES
	("Anna Fairweather", "01184960312", "fairweathera@outlook.com"),
	("Sarah McMillan", "07700900452", "mcmillans@gmail.com"),
	("Rod Orwell", "02079460123", "orwellr@ntl.com"),
	("Gregory Ratchet", "01914980521", "ratchetg@hotmail.com"),
	("Xi Wang", "01632960521", "wangx@gmail.com");

INSERT INTO products (ProductName, ProductBasePrice) VALUES
	("Fridge freezer", 21500),
	("Oven cooker", 83000),
	("Tumble dryer", 15000),
	("Vacuum cleaner", 17500),
	("Washine machine", 56000);