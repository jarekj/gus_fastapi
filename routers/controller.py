from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse
from services.gus_service import get_company_details_by_regon, get_company_details_by_nip, get_company_details_by_krs
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


@router.get("/regon2nip/{number}", response_class=PlainTextResponse)
async def get_details_by_regon(number: str):
    if validator.is_regon_valid(number) == False:
        raise HTTPException(status_code=400, detail="Invalid REGON number")
    try:
        company_details = get_company_details_by_regon(number)
        return company_details[0]['Nip']
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


@router.get("/nip2regon/{number}", response_class=PlainTextResponse)
async def get_details_by_nip(number: str):
    if validator.is_nip_valid(number) == False:
        raise HTTPException(status_code=400, detail="Invalid NIP number")
    try:
        company_details = get_company_details_by_nip(number)
        return company_details[0]['Regon']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/krs/{number}", response_model=list)
async def get_details_by_krs(number: str):
    if validator.is_krs_valid_length(number) == False:
        raise HTTPException(status_code=400, detail="Invalid KRS number length, should be 10 digits")
    try:
        company_details = get_company_details_by_krs(number)
        return company_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/krs2regon/{number}", response_class=PlainTextResponse)
async def get_details_by_krs(number: str):
    if validator.is_krs_valid_length(number) == False:
        raise HTTPException(status_code=400, detail="Invalid KRS number length, should be 10 digits")
    try:
        company_details = get_company_details_by_krs(number)
        return company_details[0]['Regon']
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))