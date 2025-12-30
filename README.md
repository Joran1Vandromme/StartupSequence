# StartupSequence

--> Door Vandromme Joran 

Het doel van deze applicatie is om een zeer minimalistische versie van een opstart sequentie programma voor te stellen. Waarmee ik bedoel; een programma die je helpt snel alle juiste programmas en web tabladen te openen afhankelijk van welke sequentie een persoon kiest. BV een school sequentie die eerst discord en chrome opent, daarna 10 sec wacht en dan ook spotify opent. 

De sequenties kunnen zelf aangemaakt worden door de gebruiker. De sequenties worden opgeslaan in een sqlite database om zo makelijk bestaande sequenties te callen via de CLI bij het opstarten van je pc.

Wat er is uitgewerkt:
    - Aanmaken van een sqlite database met 2 tabellen, 1 voor alle sequenties en 1 voor alle stappen binnen 1 sequentie

    - Via CLI een nieuwe sequentie toevoegen

    - Overzicht tonen van de reeds gemaakte sequenties

    - toevoegen van stappen aan een sequentie

    - Stappen van een sequentie tonen

    - exporteren van alle sequenties en stappen naar een csv bestand



Hoe het programmma gebruiken:
    1) venv activeren

    2) navigeer naar de src map

    3) database initialiseren: 
        python -m app.main init-db

    4) nieuwe sequentie toevoegen:

        python -m app.main sequence-add School "School startup sequence"

        School is de naam van de nieuwe sequentie en wat tussen " " staat is een korte beschrijving

    5) alle sequenties tonen: 
        python -m app.main sequence-list
    
    6) Een step toevoegen aan de sequentie (in dit geval is het een wacht step)
        python -m app.main step-add-wait School 5

        Dit voegt een wacht stap toe die 5 seconden duurt aan de school sequentie
    
    7) Toon alle stappen van de sequentie
        python -m app.main step-list School
    
    8) exporteer de data van de sequenties en de stappen naar een csv bestand
        python -m app.main export-csv rapport.csv


Extra Notitie:  De enige steps die kunnen toegevoegd worden aan een sequence zijn wacht steps
                omdat ik geen idee heb hoe je daadwerkelijk programmas veilig en correct opstart via python en het me niet perse in de scope van dit project leek te passen. 


