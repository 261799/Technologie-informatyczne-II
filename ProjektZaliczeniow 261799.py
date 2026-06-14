import json
import os

class Zajecia:
    def __init__(self, nazwa, godzina_start, godzina_koniec, sala, tydzien_start, tydzien_koniec):
        self.nazwa = nazwa
        self.godzina_start = godzina_start
        self.godzina_koniec = godzina_koniec
        self.sala = sala
        self.tydzien_start = tydzien_start
        self.tydzien_koniec = tydzien_koniec

    def czy_odbywaja_sie(self, numer_tygodnia):
        if numer_tygodnia==None or numer_tygodnia >= self.tydzien_start and numer_tygodnia <= self.tydzien_koniec:
            return True
        else:
            return False

    def to_dict(self):
        return {
            "nazwa": self.nazwa,
            "godzina_start": self.godzina_start,
            "godzina_koniec": self.godzina_koniec,
            "sala": self.sala,
            "tydzien_start": self.tydzien_start,
            "tydzien_koniec": self.tydzien_koniec
        }

    def __str__(self):
        return f"{self.godzina_start} - {self.godzina_koniec} | {self.nazwa} (Sala: {self.sala}) [Tygodnie: {self.tydzien_start}-{self.tydzien_koniec}]"


class PlanZajec:
    def __init__(self):
        self.harmonogram = {
            "poniedziałek": [], "wtorek": [], "środa": [], "czwartek": [], "piątek": []
        }
        self.nazwa_pliku = "plan.json"
        self.wczytaj_z_pliku()

    def dodaj_zajecia(self, dzien, zajecia):
        dzien = dzien.lower()
        if dzien in self.harmonogram:
            self.harmonogram[dzien].append(zajecia)
            self.harmonogram[dzien].sort(key=lambda z: z.godzina_start)
            print(f"Dodano pomyslnie przedmiot: {zajecia.nazwa}")
            self.zapisz_do_pliku()
        else:
            print("Niepoprawny dzien tygodnia")

    def usun_zajecia(self, dzien, indeks):


        dzien = dzien.lower()
        if dzien in self.harmonogram:
            try:
                usuniete = self.harmonogram[dzien].pop(indeks - 1)
                print(f"Pomyślnie usunięto zajęcia: {usuniete.nazwa}")
                self.zapisz_do_pliku()
            except IndexError:
                print("Błąd: Nie ma zajęć o takim numerze na liście!")
        else:
            print("Niepoprawny dzień tygodnia!")

    def wyswietl_plan(self, dzien, numer_tygodnia=None):
        dzien = dzien.lower()
        if dzien not in self.harmonogram:
            print("Niepoprawny dzień tygodnia!")
            return

        print(f"\n--- PLAN ZAJĘĆ: {dzien.capitalize()} (Tydzień {numer_tygodnia}) ---")

        znaleziono = False
        for zajecia in self.harmonogram[dzien]:
            if zajecia.czy_odbywaja_sie(numer_tygodnia):
                print(zajecia)
                znaleziono = True
                return 1 # Jakies zajecia sie odbywaja w tym dniu, przyda sie do usuwania zajec

        if not znaleziono:
            print("Brak zajęć w tym dniu w wybranym tygodniu.")
            return 0 # Brak zajec w tym dniu, przyda sie do usuwania zajec


    def zapisz_do_pliku(self):
        dane_do_zapisu = {}
        for dzien, lista_zajec in self.harmonogram.items():
            dane_do_zapisu[dzien] = [zajecia.to_dict() for zajecia in lista_zajec]

        with open(self.nazwa_pliku, "w", encoding="utf-8") as f:
            json.dump(dane_do_zapisu, f, ensure_ascii=False, indent=4)

    def wczytaj_z_pliku(self):
        if not os.path.exists(self.nazwa_pliku):
            return

        try:
            with open(self.nazwa_pliku, "r", encoding="utf-8") as f:
                surowe_dane = json.load(f)
                for dzien, lista_slownikow in surowe_dane.items():
                    self.harmonogram[dzien] = []
                    for d in lista_slownikow:
                        obiekt_zajecia = Zajecia(
                            d["nazwa"], d["godzina_start"], d["godzina_koniec"],
                            d["sala"], d["tydzien_start"], d["tydzien_koniec"]
                        )
                        self.harmonogram[dzien].append(obiekt_zajecia)
        except Exception as e:
            print(f"Błąd podczas wczytywania planu: {e}")


def menu():
    print("=" * 40 + "\n")
    print("1. Pokaż plan zajęć")
    print("2. Dodaj zajęcia")
    print("3. Usuń zajęcia")
    print("4. Wyjście")

    try:
        return int(input("Wybierz opcję (1-4): "))
    except ValueError:
        return -1


def main():
    moj_plan = PlanZajec()

    print("Witaj w Twoim osobistym asystencie planu zajęć!")

    while True:
        choice = menu()

        match choice:
            case 4:
                print("Zamykam program. Dane są bezpieczne. Powodzenia!")
                break

            case -1:
                print("Musisz podać poprawną cyfrę")

            case 1:
                try:
                    tydzien = int(input("Podaj numer tygodnia studiów (np. 1, 2): "))
                    dzien = input("Podaj dzień tygodnia (np. poniedziałek): ").strip()
                    moj_plan.wyswietl_plan(dzien, tydzien)
                except ValueError:
                    print("Numer tygodnia musi być liczbą!")

            case 2:
                print("\n--- DODAWANIE NOWYCH ZAJĘĆ ---")
                dzien = input("Podaj dzień tygodnia (np. poniedziałek): ").strip()
                nazwa = input("Nazwa przedmiotu: ").strip()
                godzina_start = input("Godzina rozpoczęcia (np. 08:15): ").strip()
                godzina_koniec = input("Godzina zakończenia (np. 09:45): ").strip()

                try:
                    tydzien_start = int(input("Tydzień rozpoczęcia (np. 1): ").strip())
                    tydzien_koniec = int(input("Tydzień zakończenia (np. 15): ").strip())
                except ValueError:
                    print("Tygodnie must być liczbami! Przerywam dodawanie.")
                    continue

                sala = input("Sala: ").strip()

                nowe_zajecia = Zajecia(nazwa, godzina_start, godzina_koniec, sala, tydzien_start, tydzien_koniec)
                moj_plan.dodaj_zajecia(dzien, nowe_zajecia)

            case 3:
                print("\n--- USUWANIE ZAJĘĆ ---")
                dzien = input("Z którego dnia chcesz usunąć zajęcia?: ").strip()
                if moj_plan.wyswietl_plan(dzien)==1:
                    try:
                        numer_do_usuniecia = int(input("\nPodaj numer zajęć do usunięcia: "))
                        moj_plan.usun_zajecia(dzien, numer_do_usuniecia)
                    except ValueError:
                        print("Błąd: Musisz podać liczbę całkowitą!")
                else:
                    print("Nie ma czego usunac")


            case _:
                print("Niepoprawny numer opcji, wybierz od 1 do 4.")


if __name__ == "__main__":
    main()