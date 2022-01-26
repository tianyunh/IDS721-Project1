import asyncio
from main import getTopTracks

def test_getTopTracks():
    assert asyncio.run(getTopTracks("Radiohead")) == {"Top 10 tracks: ":"1. Creep 2. Karma Police 3. No Surprises 4. High and Dry 5. Fake Plastic Trees 6. Exit Music (For A Film) 7. Weird Fishes/ Arpeggi 8. Paranoid Android 9. Nude 10. Just "}
    assert asyncio.run(getTopTracks("somerandomartist")) == {"Top 10 tracks: ":"Oops! Cannot find the artist you are looking for. Please enter a valid artist name."}