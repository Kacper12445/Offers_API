from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from firebase_admin import firestore

from config import get_firebase_user_from_token

router = APIRouter()

def get_firebase_collection(name):
    db = firestore.client()
    collection = db.collection(name)
    return collection


@router.get("/userid")
async def get_userid(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    """gets the firebase connected user"""
    return {"id": user["uid"]}


@router.get("/offers/{offer_id}")
def get_offer_by_id(offer_id: str):
    try:
        collection = get_firebase_collection('oferty')
        doc = collection.document(offer_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Offer not found")
        return doc.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/offers/{offer_id}")
def delete_task(offer_id: str):
    try:
        collection = get_firebase_collection('ofery')
        doc_ref = collection.document(offer_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="Offer not found")
        doc_ref.delete()
        return {"message": "Offer deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/offers")
def create_offer(offer: dict):
    try:
        collection = get_firebase_collection('oferty')
        doc_ref = collection.document()
        doc_ref.set(offer)
        return {"message": "Offer created successfully", "id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/offers")
def list_offers():
    try:
        collection = get_firebase_collection('oferty')
        tasks = [doc.to_dict() for doc in collection.stream()]
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# # User model for registration and login
# class User(BaseModel):
#     email: str
#     password: str
#
# @app.post("/register/")
# def register(user: User):
#     try:
#         user_record = auth.create_user(
#             email=user.email,
#             password=user.password
#         )
#         return {"message": "User registered successfully", "uid": user_record.uid}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#
# @app.post("/login/")
# def login(user: User):
#     try:
#         # Firebase Authentication doesn't natively support login; validate using a custom method
#         # For this example, it's assumed that an external method is used to verify the email/password.
#         # Implement token generation logic here if necessary.
#         return {"message": "Login successful for user", "email": user.email}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

