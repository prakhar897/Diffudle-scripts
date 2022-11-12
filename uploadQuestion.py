import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../KeysManager/Diffudle/service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'questions').document(u'2022-11-14--1')
doc_ref.set({
    u'attemptNumber': u'1',
    u'date': u'2022-11-14',
    u'image': u'',
    u'name':u'testing/hypo',
    u'style':u'testing/style'
})