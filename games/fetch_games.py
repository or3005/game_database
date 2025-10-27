import requests
from django.core.files.base import ContentFile
from .models import Game
import os

API_URL = "https://api.rawg.io/api/games"
API_KEY = "9430df31750d41979d527f01308d3f0e"

def fetch_games_from_api():
    print("📡 Fetching games from RAWG API...")
    params = {"key": API_KEY, "page_size": 20}
    response = requests.get(API_URL, params=params)
    data = response.json()

    for game_data in data["results"]:
        poster_url = game_data.get("background_image")
        poster_file = None

        if poster_url:
            try:
                image_response = requests.get(poster_url)
                image_response.raise_for_status()
                filename = os.path.basename(poster_url)
                poster_file = ContentFile(image_response.content, name=filename)
            except Exception as e:
                print(f"⚠️ Failed to fetch image for {game_data['name']}: {e}")

        Game.objects.update_or_create(
            title=game_data["name"],
            defaults={
                "description": game_data.get("description_raw", "No description available."),
                "release_year": game_data.get("released", "Unknown")[:4] if game_data.get("released") else None,
                "developer": ", ".join([dev["name"] for dev in game_data.get("developers", [])]) if game_data.get("developers") else "Unknown",
                "genre": ", ".join([genre["name"] for genre in game_data.get("genres", [])]) if game_data.get("genres") else "Various",
                "poster": poster_file
            }
        )

    print("Games fetched and saved successfully!")
