from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Enter an artist name to get the artist's top 10 tracks!"}

def test_read_getTopTracks():
    response = client.get("/getTopTracks/Radiohead")
    assert response.status_code == 200
    assert response.json() == {"Top 10 tracks: ":"1. Creep 2. Karma Police 3. No Surprises 4. High and Dry 5. Fake Plastic Trees 6. Exit Music (For A Film) 7. Weird Fishes/ Arpeggi 8. Paranoid Android 9. Nude 10. Just "}