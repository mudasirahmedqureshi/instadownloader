from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from models import db, Download
from downloader import get_video_info

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/api/download", methods=["POST"])
def download():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        video_url = get_video_info(url)
        new_download = Download(url=url)
        db.session.add(new_download)
        db.session.commit()

        return jsonify({"video": video_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

