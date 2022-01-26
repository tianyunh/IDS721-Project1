from fastapi import FastAPI
import uvicorn

import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 


cid ="427c7e94df2b4d1f89ad703f2d83d005" 
secret = "02a04d31f6a64e3ca79f8d16b7dfa51e" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Enter an artist name to get the artist's top 10 tracks!"
    }
    
    
@app.get("/getTopTracks/{name}")

async def getTopTracks(name: str):
    results = sp.search(q='artist: '+name , type='artist')
    items = results['artists']['items']
    
    if len(items) == 0:
        return {"Top 10 tracks: ": "Oops! Cannot find the artist you are looking for. Please enter a valid artist name."}
    else:
        uri = items[0]['uri']
        result2 = sp.artist_top_tracks(uri)
        i = 1
        toptracks = ''
        for track in result2['tracks'][:10]:
            ithtrack = str(i)+". " + track['name'] + " "
            toptracks = toptracks + ithtrack
            i += 1
            
        return {"Top 10 tracks: ": toptracks}

    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
