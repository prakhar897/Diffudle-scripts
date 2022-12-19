import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../KeysManager/Diffudle/service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def remove_user(ip):
    doc_ref = db.collection(u'users').document(ip)
    doc_ref.delete()

def find_user(ip):
    doc = db.collection(u'users').document(ip).get()
    print(doc.to_dict())

def find_question(id):
    doc = db.collection(u'questions').document(id).get()
    print(doc.to_dict())

id="2022-12-20--1"


find_question(id)
