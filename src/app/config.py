import json
import os


def load_settings():
    """
    Leest settings.json uit de hoofmap van het project
    en geeft het databasepad terug.
    """
    # Pad naar projectroot (1 map boven src)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    settings_path = os.path.join(project_root, "settings.json")

    with open(settings_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

