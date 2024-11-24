from firebase_admin import firestore


def get_collection(collection_name):
    db = firestore.client()
    return db.collection(collection_name)