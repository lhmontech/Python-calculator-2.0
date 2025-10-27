from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import routes
import os

frontend_build_path = os.path.join(os.path.dirname(__file__), "../Calculator-frontend/build")

app = Flask(__name__, static_folder=frontend_build_path, static_url_path="/")
CORS(app)

app.register_blueprint(routes)

@app.route("/")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")

@app.errorhandler(404)
def not_found(e):
    if not str(e).startswith("404 Not Found: /api"):
        return send_from_directory(app.static_folder, "index.html")
    return "Not Found", 404

if __name__ == "__main__":
    app.run(debug=True)
