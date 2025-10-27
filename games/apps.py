from django.apps import AppConfig
import threading


class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'games'

    def ready(self):
        from .models import Game
        from .fetch_games import fetch_games_from_api

        def load_games():
            try:
                if not Game.objects.exists():
                    print("📡 Fetching games from RAWG API (on startup)...")
                    fetch_games_from_api()
                    print("✅ Games fetched and saved successfully!")
                else:
                    print("🟢 Games already exist in the database. Skipping fetch.")
            except Exception as e:
                print(f"❌ Error fetching games: {e}")

        # נשתמש ב-thread כדי לא לחסום את עליית השרת
        threading.Thread(target=load_games).start()
