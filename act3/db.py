import sqlite3


def conectar():
    return sqlite3.connect("database.db")


def inicializar_db():
    conn = conectar()
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio REAL,
        stock INTEGER
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        total REAL,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )
    """
    )

    # Insertar datos SOLO si está vacío
    cursor.execute("SELECT COUNT(*) FROM clientes")
    if cursor.fetchone()[0] == 0:

        cursor.executemany(
            "INSERT INTO clientes (nombre, edad) VALUES (?, ?)",
            [("Juan", 25), ("Ana", 35), ("Luis", 40)],
        )

        cursor.executemany(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            [("Laptop", 15000, 5), ("Mouse", 200, 50), ("Teclado", 500, 8)],
        )

        cursor.executemany(
            "INSERT INTO pedidos (cliente_id, total) VALUES (?, ?)",
            [(1, 1200), (2, 3000), (3, 800)],
        )

    conn.commit()
    conn.close()


def obtener_consulta(num):
    conn = conectar()
    cursor = conn.cursor()

    consultas = {
        1: "SELECT * FROM clientes",
        2: "SELECT nombre FROM clientes WHERE edad > 30",
        3: "SELECT COUNT(*) FROM pedidos",
        4: "SELECT * FROM productos ORDER BY precio DESC",
        5: "SELECT clientes.nombre, pedidos.total FROM clientes JOIN pedidos ON clientes.id = pedidos.cliente_id",
        6: "SELECT AVG(precio) FROM productos",
        7: "SELECT * FROM pedidos WHERE total > 1000",
        8: "SELECT nombre FROM productos WHERE stock < 10",
        9: "SELECT MAX(precio) FROM productos",
        10: "SELECT MIN(precio) FROM productos",
    }

    resultado = cursor.execute(consultas[num]).fetchall()
    conn.close()
    return resultado
