
from backend.database import get_connection


def add_scheme():

    connection = get_connection()

    # Check whether the scheme already exists
    existing = connection.execute(
        "SELECT id FROM schemes WHERE name = ?",
        ("Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",)
    ).fetchone()

    if existing:
        print("PM-KISAN is already in the database.")
        connection.close()
        return

    connection.execute("""
        INSERT INTO schemes (
            name,
            state,
            category,
            description,
            eligibility,
            benefits,
            documents,
            application_process,
            official_url,
            source,
            last_verified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        "All India",
        "Agriculture",
        "A Central Government scheme providing income support to eligible landholding farmer families.",
        "Landholding farmer families with cultivable land in their names, subject to official exclusion criteria.",
        "₹6,000 per year in three equal instalments of ₹2,000 each.",
        "Check the official portal for the current document and verification requirements.",
        "Visit the official PM-KISAN portal and follow its farmer registration process.",
        "https://pmkisan.gov.in/",
        "Government of India - Department of Agriculture and Farmers Welfare",
        "2026-11-26"
    ))

    connection.commit()
    connection.close()

    print("PM-KISAN added successfully!")


@app.route("/api/schemes/<int:scheme_id>", methods=["GET"])
def get_scheme_details(scheme_id):
    from backend.database import get_connection

    connection = get_connection()
    connection.row_factory = __import__("sqlite3").Row

    scheme = connection.execute(
        "SELECT * FROM schemes WHERE id = ?",
        (scheme_id,)
    ).fetchone()

    connection.close()

    if scheme is None:
        return jsonify({
            "error": "Scheme not found"
        }), 404

    return jsonify(dict(scheme))

if __name__ == "__main__":
    add_scheme()
