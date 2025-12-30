import argparse

from app.config import load_settings
from app.db import init_db
from app.repo import SequenceRepo


def main():
    parser = argparse.ArgumentParser(description="StartupSequence CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init-db", help="maak de data base en tabellen aan")

    parser_add = subparsers.add_parser("sequence-add", help="voeg een sequence toe")
    parser_add.add_argument("naam", type=str)
    parser_add.add_argument("beschrijving", type=str)

    subparsers.add_parser("sequence-list", help="toon alle sequences")

    args = parser.parse_args()

    settings = load_settings()
    db_path = settings["db_path"]

    if args.command == "init-db":
        init_db(db_path)
        print("Database is geinitialiseerd:", db_path)

    elif args.command == "sequence-add":
        repo = SequenceRepo(db_path)
        repo.toevoegen(args.naam, args.beschrijving)
        print("Sequence toegevoegd.")

    elif args.command == "sequence-list":
        repo = SequenceRepo(db_path)
        sequences = repo.alles_ophalen()
        for seq in sequences:
            print(seq.id, seq.naam, "-", seq.beschrijving)


if __name__ == "__main__":
    main()

