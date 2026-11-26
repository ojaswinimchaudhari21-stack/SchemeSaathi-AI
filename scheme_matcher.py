
from backend.database import get_connection


def find_schemes(category=None, state=None):

    connection = get_connection()
    connection.row_factory = __import__("sqlite3").Row

    query = "SELECT * FROM schemes WHERE 1=1"
    values = []

    if category:
        query += " AND category LIKE ?"
        values.append(f"%{category}%")

    if state:
        query += " AND (state = ? OR state = 'All India')"
        values.append(state)

    results = connection.execute(query, values).fetchall()

    connection.close()

    return [dict(row) for row in results]
