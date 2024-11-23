# from fastapi import APIRouter, HTTPException
# from firebase_admin import firestore
#
#
# router = APIRouter()
#
# db = firestore.client()
#
# # @TODO CREATE COLLECTION
# # collection = db.collection('offers')
#
#
# @router.get("/positionFilters")
# def filter_by_position():
#     try:
#         # @TODO
#         # tasks = [doc.to_dict() for doc in collection.stream()]
#         return tasks
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#
#
# @router.get("/cityFilters")
# def filter_by_city():
#     try:
#         # @TODO
#         # tasks = [doc.to_dict() for doc in collection.stream()]
#         return tasks
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))