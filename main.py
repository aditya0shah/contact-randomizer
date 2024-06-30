from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
import random

app = Flask(__name__)

CONTACTS_FILE = 'contacts.json'

def read_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def write_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

@app.route('/')
def index():
    contacts = []
    phone_numbers = []
    things = read_contacts()
    print(things)
    for contact in things:
        print(contact)
        contacts.append([contact["name"]])
        phone_numbers.append(contact["phone"])    

    random.shuffle(phone_numbers)
    for i in range(len(phone_numbers)):
        contacts[i].append(phone_numbers[i])
        


    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    contacts = read_contacts()
    contacts.append({'name': name, 'phone': phone})
    write_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_contact():
    name = request.form['name']
    contacts = read_contacts()
    contacts = [contact for contact in contacts if contact['name'] != name]
    write_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/get_contact', methods=['POST'])
def get_contact():
    list = []
    choices = read_contacts()

    for choice in choices:
        list.append(choice.phone)
    



    

if __name__ == '__main__':
    app.run(debug=True)
