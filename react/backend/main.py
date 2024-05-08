from flask import request, jsonify
from config import app, db
from models import Contact
# sup
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = [contact.to_json() for contact in contacts]
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "First name, last name, and email are required."}), 400

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "New contact created."}), 201
    except Exception as e:
        return jsonify({"message": "Failed to create contact. Please try again."}), 400

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "Contact not found."}), 404

    data = request.json
    if "firstName" in data:
        contact.first_name = data["firstName"]
    if "lastName" in data:
        contact.last_name = data["lastName"]
    if "email" in data:
        contact.email = data["email"]

    db.session.commit()
    return jsonify({"message": "Contact updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "Contact not found."}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted."}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)  
