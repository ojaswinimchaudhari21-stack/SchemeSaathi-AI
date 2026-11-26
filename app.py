
from flask import Flask, jsonify, request
from backend.database import init_db
from backend.scheme_matcher import find_schemes

# Create Flask application
app = Flask(__name__)


# Home API
@app.route("/")
def home():
    return jsonify({
        "project": "SchemeSaathi AI",
        "message": "Backend is running successfully!",
        "status": "success"
    })


# Health API
@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "SchemeSaathi AI Backend"
    })


# Government Scheme Search API
@app.route("/api/schemes", methods=["GET"])
def get_schemes():
    category = request.args.get("category")
    state = request.args.get("state")

    results = find_schemes(category, state)

    return jsonify({
        "count": len(results),
        "schemes": results
    })


# Start application
if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
    app.run(debug=True)
