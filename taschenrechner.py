# Taschenrechner in Python

import math

def show_menü():
    print("\nWählen Sie eine Operation:")
    print("1: Addition (+)")
    print("2: Subraktion (-)")
    print("3: Multiplikation (*)")
    print("4: Division (/)")
    print("5: Potenzieren (x^y)")
    print("6: Quadratwurzel (√x)")
    print("7: Beenden (Beenden)")

def main():
    print("Wilkommen beim erweiterten Taschenrechner.")

    while True:
        show_menü()
        choice = input("Wählen Sie eine Operation (1-7): ").strip()

        #Beenden
        if choice == "7":
            print("\nVielen Dank für die Nutzung.")
            break

       # Ungültige Auswahl
        if choice not in ["1","2","3","4","5","6","7"]:
            print("\nFehler: Ungiltige Auswahl.Bitte erneut versuchen.")

        # Quadratwurzel braucht nur eine Zahl
        if choice == "6":
            num = float(input("Geben Sie die erste Zahl ein: "))
            if num < 0:
                print("\nFehler: Quadratwurzel auw einer negativen Zahl ist nicht möglich.")
            else: 
                result = math.sqrt(num)
                print(f"Ergebnis: √{num} = {result}")
            continue

        # Für andere Operationen werden zwie Zahlen benötigt.
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))

        if choice == "1":
            result = num1 + num2
            print(f"\nErgebnis: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nErgebnis: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nErgebnis: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"\nErgebnis: {num1} / {num2} = {result}")
            else:
                print("\nFehler: Division durch Null ist nicht erlaubt.")

        elif choice == "5":
            result = num1 ** num2
            print("\nErgebnis: {num1} ^ {num2} = {result} ")

# Start
if __name__ == "__main__":
    main()

  

 

