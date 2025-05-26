from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql://postgres:Cse%4040668@localhost:5432/rsvp_db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Rsvp(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "status": self.status}

with app.app_context():
    db.create_all()

@app.route("/api/rsvp", methods=["POST"])
def add_or_update_rsvp():
    data = request.get_json()
    player_id = data.get("id")
    name = data.get("name")
    status = data.get("status")

    if status not in ["Yes", "No", "Maybe"]:
        return jsonify({"error": "Invalid RSVP status."}), 400

    rsvp = Rsvp.query.get(player_id)
    if rsvp:
        rsvp.name = name
        rsvp.status = status
    else:
        rsvp = Rsvp(id=player_id, name=name, status=status)
        db.session.add(rsvp)

    db.session.commit()
    return jsonify({"message": "RSVP saved.", "data": rsvp.as_dict()}), 200

@app.route('/api/rsvp/bulk', methods=['POST'])
def add_bulk_rsvps():
    data = request.get_json()
    entries = data.get('entries', [])

    for entry in entries:
        if 'name' not in entry or 'status' not in entry or 'id' not in entry:
            return jsonify({'error': 'Missing fields in bulk entry'}), 400
        new_rsvp = Rsvp(id=entry['id'], name=entry['name'], status=entry['status'])
        db.session.add(new_rsvp)

    db.session.commit()
    return jsonify({'message': 'Bulk RSVPs added'}), 201

@app.route("/api/rsvp/confirmed", methods=["GET"])
def get_confirmed():
    confirmed = Rsvp.query.filter_by(status="Yes").all()
    return jsonify([r.as_dict() for r in confirmed]), 200

@app.route("/api/rsvp/counts", methods=["GET"])
def get_counts():
    total = Rsvp.query.count()
    confirmed = Rsvp.query.filter_by(status="Yes").count()
    declined = Rsvp.query.filter_by(status="No").count()
    return jsonify({"total": total, "confirmed": confirmed, "declined": declined}), 200

@app.route("/api/rsvp", methods=["GET"])
def get_all_rsvps():
    rsvps = Rsvp.query.all()
    return jsonify([r.as_dict() for r in rsvps]), 200

@app.route("/api/rsvp/<player_id>", methods=["DELETE"])
def delete_rsvp(player_id):
    rsvp = Rsvp.query.get(player_id)
    if rsvp:
        db.session.delete(rsvp)
        db.session.commit()
        return jsonify({"message": "RSVP deleted."}), 200
    return jsonify({"error": "Player not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
