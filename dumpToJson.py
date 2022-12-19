import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate('../KeysManager/Diffudle/service-account.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


# see how many played and how many won
docs = db.collection(u'users').stream()

final_json = {}

for doc in docs:
    final_json[doc.id] = doc.to_dict()

# Serializing json
json_object = json.dumps(final_json, indent=4)
 
# Writing to sample.json
with open("users20221205.json", "w") as outfile:
    outfile.write(json_object)
