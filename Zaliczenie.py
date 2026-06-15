class Zajecia:
    def __init__(self, nazwa, godzina_start, godzina_koniec, sala, tydzien_start, tydzien_koniec):
        self.nazwa = nazwa
        self.godzina_start = godzina_start
        self.godzina_koniec = godzina_koniec
        self.sala = sala
        self.tydzien_start = tydzien_start
        self.tydzien_koniec = tydzien_koniec

    def czy_odbywaja_sie(self, numer_tygodnia):
        if numer_tygodnia == None or (numer_tygodnia >= self.tydzien_start and numer_tygodnia <= self.tydzien_koniec):
            return True
        return False

    def __str__(self):
        return f"{self.godzina_start} - {self.godzina_koniec} | {self.nazwa} (Sala: {self.sala}) [Tygodnie: {self.tydzien_start}-{self.tydzien_koniec}]"


class PlanZajec:
    def __init__(self):
    
        self.harmonogram = {
            "poniedziałek": [], 
            "wtorek": [], 
            "środa": [], 
            "czwartek": [], 
            "piątek": []
        }

    def dodaj_zajecia(self, dzien, zajecia):
        dzien = dzien.lower()
        if dzien in self.harmonogram:
            self.harmonogram[dzien].append(zajecia)
            self.harmonogram[dzien].sort(key=lambda z: z.godzina_start)
            print(f"Dodano pomyślnie przedmiot: {zajecia.nazwa}")
        else:
            print("Niepoprawny dzień tygodnia")

    def usun_zajecia(self, dzien, indeks):
        dzien = dzien.lower()
        if dzien in self.harmonogram:
            try:
                usuniete = self.harmonogram[dzien].pop(indeks - 1)
                print(f"Pomyślnie usunięto zajęcia: {usuniete.nazwa}")
            except IndexError:
                print("Błąd: Nie ma zajęć o takim numerze na liście!")
        else:
            print("Niepoprawny dzień tygodnia!")

    def wyswietl_plan(self, dzien, numer_tygodnia=None):
        dzien = dzien.lower()
        if dzien not in self.harmonogram:
            print("Niepoprawny dzień tygodnia!")
            return 0

        print(f"\n--- PLAN ZAJĘĆ: {dzien.capitalize()} (Tydzień {numer_tygodnia if numer_tygodnia else 'Wszystkie'}) ---")

        znaleziono = False
        # Poprawione wyświetlanie: pętla wypisze wszystkie przedmioty, a nie tylko pierwszy
        for indeks, zajecia in enumerate(self.harmonogram[dzien], start=1):
            if zajecia.czy_odbywaja_sie(numer_tygodnia):
                print(f"{indeks}. {zajecia}")
                znaleziono = True

        if not znaleziono:
            print("Brak zajęć w tym dniu w wybranym tygodniu.")
            return 0
        return 1


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

    print("Witaj w Twoim osobistym asystencie planu zajęć")

    while True:
        choice = menu()

        match choice:
            case 4:
                print("Zamykam program. Powodzenia na zajęciach!")
                break

            case -1:
                print("Musisz podać poprawną cyfrę")

            case 1:
                dzien = input("Podaj dzień tygodnia (np. poniedziałek): ").strip()
                tydzien_input = input("Podaj numer tygodnia (wciśnij Enter, żeby zobaczyć cały semestr): ").strip()
                
                if tydzien_input == "":
                    moj_plan.wyswietl_plan(dzien)
                else:
                    try:
                        tydzien = int(tydzien_input)
                        moj_plan.wyswietl_plan(dzien, tydzien)
                    except ValueError:
                        print("Numer tygodnia musi być liczbą")

            case 2:
                print("\n--- DODAWANIE NEWYCH ZAJĘĆ ---")
                dzien = input("Podaj dzień tygodnia (np. poniedziałek): ").strip()
                nazwa = input("Nazwa przedmiotu: ").strip()
                godzina_start = input("Godzina rozpoczęcia (np. 08:15): ").strip()
                godzina_koniec = input("Godzina zakończenia (np. 09:45): ").strip()

                try:
                    tydzien_start = int(input("Tydzień rozpoczęcia (np. 1): ").strip())
                    tydzien_koniec = int(input("Tydzień zakończenia (np. 15): ").strip())
                except ValueError:
                    print("Tygodnie muszą być liczbami!")
                    continue

                sala = input("Sala: ").strip()

                nowe_zajecia = Zajecia(nazwa, godzina_start, godzina_koniec, sala, tydzien_start, tydzien_koniec)
                moj_plan.dodaj_zajecia(dzien, nowe_zajecia)

            case 3:
                print("\n--- USUWANIE ZAJĘĆ ---")
                dzien = input("Z którego dnia chcesz usunąć zajęcia?: ").strip()
        
                if moj_plan.wyswietl_plan(dzien) == 1:
                    try:
                        numer_do_usuniecia = int(input("\nPodaj numer zajęć do usunięcia: "))
                        moj_plan.usun_zajecia(dzien, numer_do_usuniecia)
                    except ValueError:
                        print("Błąd: Musisz podać liczbę całkowitą!")
                else:
                    print("Nie ma czego usunąć.")

            case _:
                print("Niepoprawny numer opcji, wybierz od 1 do 4.")


if __name__ == "__main__":
    main()
