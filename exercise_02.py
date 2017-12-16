import sys


if __name__ == "__main__":
    number = raw_input("Please put the number: ")

    # sprawdz, czy wartosc jest liczba, jesli nie jest to wyswietl komunikat i przerwij program

    if not number.isdigit():
        print("This is not a number")
        sys.exit()

    # sprawdz czy wartosc jest liczba parzysta i wyswietl odpowiedni komunikat
    even = int(number) % 2
    if even == 0:
        print("This is even")
    else:
        print("This is odd")
