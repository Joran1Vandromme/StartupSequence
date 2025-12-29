from dataclasses import dataclass


@dataclass
class Sequence:
    id: int
    naam: str
    beschrijving: str


@dataclass
class Step:
    id: int
    reeks_id: int
    volgorde: int
    actie: str       
    commando: str
    argumenten: str
    seconden: int
    actief: bool
