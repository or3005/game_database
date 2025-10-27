from django.apps import AppConfig
import threading
from django.db import connection

class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'games'

    def ready(self):

        def load_games():
            try:

                if 'games_game' in connection.introspection.table_names():
                    from .models import Game
                    from .fetch_games import fetch_games_from_api

                    if not Game.objects.exists():
                        print("📡 Fetching games from RAWG API (on startup)...")
                        fetch_games_from_api()
                        print("✅ Games fetched and saved successfully!")
                    else:
                        print("🟢 Games already exist in the database. Skipping fetch.")
                else:
                    print("⚠️ Table 'games_game' does not exist yet. Skipping fetch.")
            except Exception as e:
                print(f"❌ Error fetching games: {e}")


        threading.Thread(target=load_games).start()
