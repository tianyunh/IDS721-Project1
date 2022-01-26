# IDS721 Project1: Fast API Microservice

[![Python 3.8](https://github.com/tianyunh/IDS721-Project1/actions/workflows/main.yml/badge.svg)](https://github.com/tianyunh/IDS721-Project1/actions/workflows/main.yml)

This is Project 1 for IDS 721 - Cloud Continuous Delivery of Microservice.
## Get Top Tracks from an Artist on Spotify
This is a microservice that can search for an artist on Spotify and return the artist's top 10 tracks as the output.

### Instructions 
- Go to http://18.224.179.111:8080/docs, which is a webpage UI for FastAPI
- Click on `getTopTracks` function and click **Try it out**
- Enter the name of the artist that you would like to search in the blank, then click **Execute**
- You will see the top 10 tracks in Responses
- If the name of the artist you entered is not valid or does not exist on Spotify database, you will see a message saying "Oops! Cannot find the artist you are looking for. Please enter a valid artist name."
