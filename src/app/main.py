import argparse

from app.config import load_settings
from app.db import init_db
from app.repo import SequenceRepo, StepRepo


def main():
    parser = argparse.ArgumentParser(description="StartupSequence CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init-db", help="maak de data base en tabellen aan")

    parser_add = subparsers.add_parser("sequence-add", help="voeg een sequence toe")
    parser_add.add_argument("naam", type=str)
    parser_add.add_argument("beschrijving", type=str)

    subparsers.add_parser("sequence-list", help="toon alle sequences")
    
    parser_step = subparsers.add_parser("step-add-wait", help="voeg een wacht moment toe")
    parser_step.add_argument("sequence_naam", type=str)
    parser_step.add_argument("seconden", type=int)

    parser_list_steps = subparsers.add_parser("step-list", help="toon de stappen van een opstartingssequence")
    parser_list_steps.add_argument("sequence_naam", type=str)
    
    parser_export = subparsers.add_parser("export-csv", help="exporteer rapport naar CSV")
    parser_export.add_argument("pad", type=str, help="pad naar csv bestand, bv rapport.csv")



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
            
    elif args.command == "step-add-wait":
        seq_repo = SequenceRepo(db_path)
        step_repo = StepRepo(db_path)

        seq = seq_repo.zoek_op_naam(args.sequence_naam)
        if seq is None:
            print("Sequence niet gevonden.")
            return

        step_repo.voeg_wait_toe(seq.id, args.seconden)
        print("Wacht periode toegevoegd.")

    elif args.command == "step-list":
        seq_repo = SequenceRepo(db_path)
        step_repo = StepRepo(db_path)

        seq = seq_repo.zoek_op_naam(args.sequence_naam)
        if seq is None:
            print("Sequence niet gevonden.")
            return

        stappen = step_repo.stappen_van_sequence(seq.id)
        for st in stappen:
            print(st.volgorde, st.actie, st.seconden, "sec")
    elif args.command == "export-csv":
        step_repo = StepRepo(db_path)
        rows = step_repo.rapport_rows()

        import csv
        with open(args.pad, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["sequence_naam", "volgorde", "actie", "seconden", "actief"])
            for r in rows:
                writer.writerow(r)

        print("CSV gemaakt:", args.pad)




if __name__ == "__main__":
    main()

