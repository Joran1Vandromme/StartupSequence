import argparse

from app.config import load_settings
from app.db import init_db


def main():
    parser = argparse.ArgumentParser(description="StartupSequence CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init-db", help="maak de database en tabellen aan")

    args = parser.parse_args()

    settings = load_settings()
    db_path = settings["db_path"]

    if args.command == "init-db":
        init_db(db_path)
        print("Database is geïnitialiseerd:", db_path)


if __name__ == "__main__":
    main()

