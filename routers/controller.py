from fastapi import APIRouter, HTTPException
from services.gus_service import get_company_details_by_regon, get_company_details_by_nip
from utils import validator

router = APIRouter()

@router.get("/regon/{number}", response_model=list)

async def get_details_by_regon(number: str):
    if validator.is_regon_valid(number) == False:
        raise HTTPException(status_code=400, detail="Invalid REGON number")
    try:
        company_details = get_company_details_by_regon(number)
        return company_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/nip/{number}", response_model=list)

async def get_details_by_nip(number: str):
    if validator.is_nip_valid(number) == False:
        raise HTTPException(status_code=400, detail="Invalid NIP number")
    try:
        company_details = get_company_details_by_nip(number)
        return company_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))