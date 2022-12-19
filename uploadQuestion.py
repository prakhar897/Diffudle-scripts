import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
import base64

cred = credentials.Certificate('../KeysManager/Diffudle/service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


directory = '../diffudle-extra/pics'
name = 'vegetable/guns'
i=1
date = '2022-12-21'

for filename in os.listdir(directory):
    print(i)
    f = os.path.join(directory, filename)
    style = filename.split(".")[0]
    print(style)
    with open(f, "rb") as img_file:
        image = "data:image/png;base64," + base64.b64encode(img_file.read()).decode('utf-8')
        doc_ref = db.collection(u'questions').document(date + "--"+ str(i))
        doc_ref.set({
            u'image': image,
            u'name':name,
            u'style':filename
        })
    i += 1

    if i== 7:
        doc_ref2 = db.collection(u'questions').document(date + "--"+ str(i))
        doc_ref2.set({
            u'image': image,
            u'name':name,
            u'style':filename
        })