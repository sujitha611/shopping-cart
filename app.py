from flask import Flask, jsonify, request, send_from_directory
import sqlite3

app = Flask(__name__, static_folder=".", static_url_path="")

def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            quantity INTEGER
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/products", methods=["GET"])
def get_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                   (data["name"], data["price"], data["quantity"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added!"})

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product deleted!"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)