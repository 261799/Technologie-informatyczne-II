SIZE = 10

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    numbers.sort()
    mid1 = numbers[SIZE // 2 - 1]
    mid2 = numbers[SIZE // 2]
    return (mid1 + mid2) / 2


def print_array(numbers):
    for i, num in enumerate(numbers):
        print(f"numbers[{i}] = {num}")


def scan_array(numbers):
    for i in range(SIZE):
        numbers[i] = int(input(f"Podaj liczbe [{i}]: "))

if __name__ == "__main__":
    print("Tablice")
    numbers = [0] * SIZE

    while True:
        print("\nMENU:")
        print("1. Wprowadz dane do tablicy")
        print("2. Wyswietl tablice")
        print("3. Oblicz wartosc maksymalna")
        print("4. Oblicz wartosc minimalna")
        print("5. Oblicz wartosc srednia")
        print("6. Oblicz mediane")
        print("0. Wyjdz z programu")

        option = int(input("Wybor: "))

        if option == 1:
            print(f"Wprowadz {SIZE} liczb do tablicy:")
            scan_array(numbers)
        elif option == 2:
            print_array(numbers)
        elif option == 3:
            print(f"max = {max(numbers)}")
        elif option == 4:
            print(f"min = {min(numbers)}")
        elif option == 5:
            print(f"average = {calculate_average(numbers):.2f}")
        elif option == 6:
            print(f"median = {calculate_median(numbers):.2f}")
        elif option == 0:
            break
        else:
            print("Zla opcja. Prosze wybrac prawidlowa opcje")


# def to_lower(text):
#     return text.lower()


# def to_upper(text):
#     return text.upper()


# def text_size(text):
#     return len(text)

# if __name__ == "__main__":
#     while True:
#         print("Enter new text: ")
#         text = input()

#         if text == "":
#             break

#         print(text)

#         text = to_lower(text)
#         print(text)

#         text = to_upper(text)
#         print(text)

#         print(text_size(text))
