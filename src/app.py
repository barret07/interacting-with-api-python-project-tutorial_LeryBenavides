#FUNCION PARA CONECTAR CON WEB API SPOTIFY

import os
import seaborn as sns
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# CONECTANDO SPOTIPY CON SERVER SPOTIFY

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

conex = spotipy.Spotify (auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))

# BUSCANDO ARTISTA "OASIS" E IMPORTANDO SU TOP 10 + TIEMPO + POPULARIDAD

import pandas as pd

my_favorite_artist = "2DaxqgrOhkeH0fpeiQq2f4"

response = conex.artist_top_tracks ("2DaxqgrOhkeH0fpeiQq2f4")

if response:
    top_songs = response["tracks"]
    top_songs = [{k: (format(v/(1000*60),".2f")) if k == "duration_ms" else v for k, v in 
               track.items() if k in ["name", "popularity", "duration_ms"]} for track in top_songs]
    
top_songs_df = pd.DataFrame.from_records(top_songs)
top_songs_df.sort_values (["popularity"], inplace = True)

print (top_songs_df.head)

# PLOTEANDO GRAFICO "POPULARITY vs. DURATION" PARA ANALISIS

compare_plot = sns.scatterplot(data = top_songs_df, x = "popularity", y = "duration_ms")
figure = compare_plot.get_figure()
figure.savefig("scatter_plot.png")