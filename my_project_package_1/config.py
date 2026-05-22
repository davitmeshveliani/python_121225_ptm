from pymongo import MongoClient

MONGO_URI = (
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

def get_db():
    client = MongoClient(MONGO_URI)
    return client["ich_edit"]