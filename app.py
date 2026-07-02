reports = []

from ai.gemini_service import analyze_issue
from flask import request, jsonify
from flask import Flask, request, jsonify


from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "message": "FixMyCity AI Backend Running 🚀",
        "status": "success"
    }

@app.route("/api/test")
def test():
    return {
        "success": True,
        "message": "Frontend connected successfully! 🎉"
    }

@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    description = data.get("description", "")

    result = analyze_issue(description)

    return {
        "result": result
    }

@app.route("/api/analyze-image", methods=["POST"])
def analyze_image():

    image = request.files.get("image")
    description = request.form.get("description")

    if image is None:
        return jsonify({
            "success": False,
            "message": "No image uploaded"
        }), 400

    ai_result = analyze_issue(description)

    return jsonify({
        "success": True,
        "result": ai_result
    })

@app.route("/api/report", methods=["POST"])
def submit_report():

    data = request.json

    reports.append(data)

    return jsonify({
        "success": True,
        "message": "Report submitted successfully"
    })

@app.route("/api/reports")
def get_reports():
    return jsonify(reports)



@app.route("/api/report/<int:index>", methods=["DELETE"])
def delete_report(index):

    if index >= len(reports):
        return jsonify({
            "success": False
        }), 404

    reports.pop(index)

    return jsonify({
        "success": True
    })

if __name__ == "__main__":
    app.run(debug=True)