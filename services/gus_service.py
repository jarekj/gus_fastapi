import os
from dotenv import load_dotenv

from RegonAPI import RegonAPI
from RegonAPI.exceptions import ApiAuthenticationError
load_dotenv()
gus_api_key = os.getenv("GUS_API_KEY")

api = RegonAPI(
        bir_version="bir1.1", is_production=True, timeout=10, operation_timeout=10
    )

def get_company_details_by_regon(regon_number = None) -> list:
    try:
        api.authenticate(key=gus_api_key)
    except ApiAuthenticationError as e:
        print("[-]", e)
        exit(0)
    except Exception as e:
        raise e
    
    try:
        result = api.searchData(regon=regon_number)
        print(result)
        return result
    except Exception as e:
        raise e

def get_company_details_by_nip(nip_number = None) -> list:
    try:
        api.authenticate(key=gus_api_key)
    except ApiAuthenticationError as e:
        print("[-]", e)
        exit(0)
    except Exception as e:
        raise e
    
    try:
        result = api.searchData(nip=nip_number)
        print(result)
        return result
    except Exception as e:
        raise e

def get_company_details_by_krs(krs_number = None) -> list:
    try:
        api.authenticate(key=gus_api_key)
    except ApiAuthenticationError as e:
        print("[-]", e)
        exit(0)
    except Exception as e:
        raise e
    
    try:
        result = api.searchData(krs=krs_number)
        print(result)
        return result
    except Exception as e:
        raise e    