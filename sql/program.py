import datetime as dt
import random
import sqlite3

cxn = sqlite3.connect("database.db3")
cxn.execute("PRAGMA foreign_keys = ON;")


def build_database():
	with open("script.sql", "r", encoding="utf-8") as f:
		cxn.executescript(f.read())

	cxn.commit()


def make_order():
	cxn.execute("INSERT INTO orders (CustomerID, ProductID, Discount) VALUES (?, ?, ?)", (1, 1, 0))
	cxn.commit()


def generate_orders():
	cxn.execute("BEGIN TRANSACTION")

	for i in range(50):
		cxn.execute(
			"INSERT INTO orders (CustomerID, ProductID, Discount, OrderDateTime) VALUES (?, ?, ?, ?)",
			(
				random.randint(1, 5),
				random.randint(1, 5),
				random.choice((0, random.randint(25, 100) * 100)),
				dt.datetime(2018, 1, 1) + dt.timedelta(seconds=random.randint(0, 63071999)),
			)
		)

	cxn.commit()


def display_discounted_orders():
	cur = cxn.execute("SELECT * FROM orders WHERE Discount > 0")
	for row in cur.fetchall():
		print(row)


def display_fridge_orders():
	cur = cxn.execute(
		"SELECT * FROM orders WHERE ProductID = (SELECT ProductID FROM products WHERE ProductName = 'Fridge freezer')"
	)
	for row in cur.fetchall():
		print(row)


def display_ten_most_recent_customers():
	cur = cxn.execute(
		"SELECT c.* FROM customers AS c JOIN orders AS o ON o.CustomerID = c.CustomerID "
		"ORDER BY o.OrderDateTime DESC LIMIT 10"
	)
	for row in cur.fetchall():
		print(row)


def update_discount_records():
	cur = cxn.execute(
		"UPDATE orders SET Discount = 0 WHERE OrderDateTime >= '2019-03-01' AND OrderDateTime < '2019-06-01'"
	)
	cxn.commit()


def delete_xis_records():
	cur = cxn.execute("DELETE FROM customers WHERE CustomerName = 'Xi Wang'")
	print(f"{cur.rowcount:,} record(s) deleted.")
	cxn.commit()


if __name__ == "__main__":
	build_database()
	make_order()
	generate_orders()

	display_discounted_orders()
	display_fridge_orders()
	display_ten_most_recent_customers()
	update_discount_records()
	delete_xis_records()