# run 'pip3 install spotipy' and generate your key at https://developer.spotify.com/dashboard/

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = ''
secret = ''

while True:
	name = input("Enter Artist Name: ")
	client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	artist = sp.search(q=name, type='artist', limit=1, offset=0)

	if artist['artists']['items']:
		print(artist['artists']['items'][0]['name'] + ": " + str(artist['artists']['items'][0]['popularity']))
	else:
		print("No artist found")
