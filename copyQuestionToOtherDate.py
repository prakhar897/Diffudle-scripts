import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../KeysManager/Diffudle/service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

source_date = '2022-11-11'
dest_date = '2022-12-18'

for i in range(1,8):
    source_key = source_date + "--" + str(i)
    dest_key = dest_date + "--" + str(i)
    temp_doc = db.collection(u'questions').document(source_key).get().to_dict()
    if temp_doc['attemptNumber']:
        del temp_doc['attemptNumber']
    if temp_doc['date']:
        del temp_doc['date']
    temp_doc['name'] = 'cavemen/selfie'
    print(i)
    db.collection(u'questions').document(dest_key).set(temp_doc)