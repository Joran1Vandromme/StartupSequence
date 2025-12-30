import sqlite3
from app.models import Sequence, Step


class SequenceRepo:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def toevoegen(self, naam: str, beschrijving: str) -> None:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = "INSERT INTO sequences (name, description) VALUES (?, ?)"
        cur.execute(sql, (naam, beschrijving))

        conn.commit()
        cur.close()
        conn.close()

    def alles_ophalen(self) -> list[Sequence]:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = "SELECT id, name, description FROM sequences ORDER BY name"
        cur.execute(sql)
        rows = cur.fetchall()

        cur.close()
        conn.close()

        resultaten = []
        for row in rows:
            seq = Sequence(id=row[0], naam=row[1], beschrijving=row[2])
            resultaten.append(seq)

        return resultaten

    def zoek_op_naam(self, naam: str) -> Sequence | None:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = "SELECT id, name, description FROM sequences WHERE name = ?"
        cur.execute(sql, (naam,))
        row = cur.fetchone()

        cur.close()
        conn.close()

        if row is None:
            return None

        return Sequence(id=row[0], naam=row[1], beschrijving=row[2])

class StepRepo:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def volgende_volgorde(self, sequence_id: int) -> int:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = "SELECT COALESCE(MAX(step_order), 0) FROM steps WHERE sequence_id = ?"
        cur.execute(sql, (sequence_id,))
        row = cur.fetchone()

        cur.close()
        conn.close()

        return int(row[0]) + 1

    def voeg_wait_toe(self, sequence_id: int, seconden: int) -> None:
        volgorde = self.volgende_volgorde(sequence_id)

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = """
        INSERT INTO steps (sequence_id, step_order, action_type, seconds, enabled)
        VALUES (?, ?, 'WAIT', ?, 1)
        """
        cur.execute(sql, (sequence_id, volgorde, seconden))

        conn.commit()
        cur.close()
        conn.close()

    def stappen_van_sequence(self, sequence_id: int) -> list[Step]:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sql = """
        SELECT id, sequence_id, step_order, action_type, command, args, seconds, enabled
        FROM steps
        WHERE sequence_id = ?
        ORDER BY step_order
        """
        cur.execute(sql, (sequence_id,))
        rows = cur.fetchall()

        cur.close()
        conn.close()

        stappen = []
        for row in rows:
            st = Step(
                id=row[0],
                reeks_id=row[1],
                volgorde=row[2],
                actie_type=row[3],
                commando=row[4],
                argumenten=row[5],
                seconden=row[6],
                actief=bool(row[7]),
            )
            stappen.append(st)

        return stappen

