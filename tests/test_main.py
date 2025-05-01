import os
import sys
import pytest
from fastapi.testclient import TestClient
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_get_details_by_regon_valid():
    response = client.get("/regon/123456789")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_details_by_regon_invalid():
    response = client.get("/regon/123456781")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid REGON number"}

def test_get_details_by_nip_valid():
    response = client.get("/nip/1234567890")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_details_by_nip_invalid():
    response = client.get("/nip/12345678901")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid NIP number"}
    
def test_get_details_by_krs_valid():
    response = client.get("/krs/1234567890")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_details_by_krs_invalid():
    response = client.get("/krs/123456789")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid KRS number length, should be 10 digits"}
