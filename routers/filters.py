from fastapi import APIRouter, HTTPException

from routers.utils import get_collection

router = APIRouter()


def get_offers_collection():
    OFFERS_COLLECTION_NAME = 'offers'
    return get_collection(OFFERS_COLLECTION_NAME)


@router.get("/positionFilters")
def filter_by_position():
    try:
        # @TODO
        # tasks = [doc.to_dict() for doc in collection.stream()]
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/cityFilters")
def filter_by_city():
    try:
        # @TODO
        # tasks = [doc.to_dict() for doc in collection.stream()]
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))