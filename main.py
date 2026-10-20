import json

def main() : 
    try :
        with open("bewerbungen.json", "r", encoding="utf-8") as datei:
            bewerbungen = json.load(datei)
    except FileNotFoundError: 
        bewerbungen = []        

    while True:
        print("\n=== Ausbildung Tracker ===")
        print("1 - Bewerbung hinzufügen")
        print("2 - Bewerbungen anzeigen")
        print("3 - Status ändern")
        print("4 - Bewerbung suchen")
        print("5 - Bewerbung löschen")
        print("6 - Programm beenden")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            unternehmen = input("Name des Unternehmens: ")
            stadt = input("Stadt: ")
            beruf = input("Ausbildungsberuf: ")

            bewerbung = {
                "unternehmen": unternehmen,
                "stadt": stadt,
                "beruf": beruf
            }

            bewerbungen.append(bewerbung)
            with open("bewerbungen.json", "w", encoding="utf-8") as datei:
                json.dump(bewerbungen, datei, ensure_ascii=False, indent=4)
            print("Bewerbung erfolgreich hinzugefügt!")

        elif auswahl == "2":
            if len(bewerbungen) == 0:
                print("Noch keine Bewerbungen vorhanden.")
            else:
                for bewerbung in bewerbungen:
                    print("\nUnternehmen:", bewerbung["unternehmen"])
                    print("Stadt:", bewerbung["stadt"])
                    print("Ausbildungsberuf:", bewerbung["beruf"])
                    print("Status:", bewerbung.get("status", "Beworben"))

        elif auswahl == "3":
            if len(bewerbungen) == 0:
                print("Noch keine Bewerbungen vorhanden.")
            else:
                for nummer, bewerbung in enumerate(bewerbungen, start=1):
                    print(nummer, "-", bewerbung["unternehmen"],
                          "| Status:", bewerbung.get("status", "Beworben"))

                try:
                    nummer = int(input("Welche Bewerbung möchtest du ändern? "))
                except ValueError:
                    print("Bitte gib eine gültige Nummer ein.")
                    continue

                if nummer >= 1 and nummer <= len(bewerbungen):
                    print("1 - Beworben")
                    print("2 - Vorstellungsgespräch")
                    print("3 - Absage")
                    print("4 - Zusage")

                    status_auswahl = input("Neuer Status: ")

                    status_optionen = {
                        "1": "Beworben",
                        "2": "Vorstellungsgespräch",
                        "3": "Absage",
                        "4": "Zusage"
                    }

                    if status_auswahl in status_optionen:
                        bewerbungen[nummer - 1]["status"] = status_optionen[status_auswahl]

                        with open("bewerbungen.json", "w", encoding="utf-8") as datei:
                            json.dump(bewerbungen, datei, ensure_ascii=False, indent=4)

                        print("Status erfolgreich geändert!")
                    else:
                        print("Ungültige Auswahl!")
                else:
                    print("Ungültige Bewerbungsnummer!")

        elif auswahl == "4":
            suchbegriff = input("Unternehmensname eingeben: ").strip().casefold()

            if not suchbegriff:
                print("Bitte einen Suchbegriff eingeben.")
            else:
                treffer = [
                    bewerbung for bewerbung in bewerbungen
                    if suchbegriff in bewerbung.get("unternehmen", "").casefold()
                ]

                if not treffer:
                    print("Keine passende Bewerbung gefunden.")
                else:
                    for bewerbung in treffer:
                        print("\nUnternehmen:", bewerbung.get("unternehmen", ""))
                        print("Stadt:", bewerbung.get("stadt", ""))
                        print("Ausbildungsberuf:", bewerbung.get("beruf", ""))
                        print("Status:", bewerbung.get("status", "Beworben"))
    
        elif auswahl == "5":
            if len(bewerbungen) == 0:
                print("Noch keine Bewerbungen vorhanden.")
            else:
                for nummer, bewerbung in enumerate(bewerbungen, start=1):
                    print(nummer, "-", bewerbung["unternehmen"],
                          "| Status:", bewerbung.get("status", "Beworben"))

                try:
                    nummer = int(input("Welche Bewerbung möchtest du löschen? "))
                except ValueError:
                    print("Bitte gib eine gültige Nummer ein.")
                    continue

                if 1 <= nummer <= len(bewerbungen):
                    bestaetigung = input(
                        "Möchtest du diese Bewerbung wirklich löschen? (ja/nein): "
                    ).strip().casefold()

                    if bestaetigung == "ja":
                        geloescht = bewerbungen.pop(nummer - 1)

                        with open("bewerbungen.json", "w", encoding="utf-8") as datei:
                            json.dump(bewerbungen, datei, ensure_ascii=False, indent=4)

                        print(geloescht["unternehmen"], "wurde gelöscht.")
                    else:
                        print("Löschen abgebrochen.")
                else:
                     print("Ungültige Bewerbungsnummer!")

        elif auswahl == "6":
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Auswahl!")

if __name__ == "__main__" : 
    main()
