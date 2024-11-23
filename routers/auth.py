# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from firebase_admin import auth, firestore
#
# router = APIRouter()
#
#
# db = firestore.client()
# # @TODO CREATE COLLECTION
# # collection = db.collection('auth')
#
# class User(BaseModel):
#     email: str
#     password: str
#
#
# @router.post("/register")
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
#
# @router.post("/login")
# def login(user: User):
#     try:
#         # Implement token generation or email/password verification logic
#         return {"message": "Login successful for user", "email": user.email}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
