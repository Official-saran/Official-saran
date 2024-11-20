#Database Model:
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

#API Implementation: 

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models import db, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

class ItemList(Resource):
    def get(self):
        items = Item.query.all()
        return [item.to_dict() for item in items]

    def post(self):
        data = request.get_json()
        new_item = Item(name=data['name'], description=data['description'])
        db.session.add(new_item)
        db.session.commit()
        return {"message": "Item added successfully!"}, 201

class ItemDetail(Resource):
    def put(self, id):
        item = Item.query.get(id)
        if not item:
            return {"message": "Item not found"}, 404
        data = request.get_json()
        item.name = data['name']
        item.description = data['description']
        db.session.commit()
        return item.to_dict()

    def delete(self, id):
        item = Item.query.get(id)
        if not item:
            return {"message": "Item not found"}, 404
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully!"}

api.add_resource(ItemList, '/items')
api.add_resource(ItemDetail, '/items/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)

#Email Sending via SMTP:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, content):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(content, "plain"))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        return "Email sent successfully!"
#Spam Filtering:
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def is_spam(content):
    spam_words = ["win", "free", "offer", "click"]
    words = word_tokenize(content.lower())
    for word in words:
        if word in spam_words:
            return True
    return False

