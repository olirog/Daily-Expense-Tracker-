
print("Welcome to the Daily Expense Tracker!")
print("Choose your language / Wybierz jezyk:")
print("1. English")
print("2. Polski")

language = input()

while language not in ["1", "2"]:
    print("Invalid choice / Nieprawidlowy wybor.")
    language = input()

expenses = []
budget = 0

while True:

    if language == "1":
        print("\nMenu:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Calculate total and average expense")
        print("4. Clear all expenses")
        print("5. Set budget limit")
        print("6. Delete a single expense")
        print("7. Exit")
    else:
        print("\nMenu:")
        print("1. Dodaj nowy wydatek")
        print("2. Wyswietl wszystkie wydatki")
        print("3. Oblicz sume i srednia wydatkow")
        print("4. Usun wszystkie wydatki")
        print("5. Ustaw limit budzetu")
        print("6. Usun pojedynczy wydatek")
        print("7. Wyjdz")

    choice = input()

    if choice == "1":
        if language == "1":
            amount = float(input("Enter expense amount: "))
        else:
            amount = float(input("Podaj kwote wydatku: "))

        expenses.append(amount)

        if language == "1":
            print("Expense added successfully!")
        else:
            print("Wydatek zostal dodany!")

        if budget > 0 and sum(expenses) > budget:
            if language == "1":
                print("Warning! You have exceeded your budget!")
            else:
                print("Uwaga! Przekroczono limit budzetu!")

    elif choice == "2":
        if len(expenses) == 0:
            if language == "1":
                print("No expenses recorded yet.")
            else:
                print("Nie zapisano jeszcze zadnych wydatkow.")
        else:
            if language == "1":
                print("Your expenses:")
            else:
                print("Twoje wydatki:")

            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    elif choice == "3":
        if len(expenses) == 0:
            if language == "1":
                print("No expenses recorded yet.")
            else:
                print("Nie zapisano jeszcze zadnych wydatkow.")
        else:
            total = sum(expenses)
            average = total / len(expenses)

            if language == "1":
                print(f"Total expense: {total}")
                print(f"Average expense: {average}")
            else:
                print(f"Suma wydatkow: {total}")
                print(f"Srednia wydatkow: {average}")

    elif choice == "4":
        expenses = []

        if language == "1":
            print("All expenses cleared.")
        else:
            print("Wszystkie wydatki zostaly usuniete.")

    elif choice == "5":
        if language == "1":
            budget = float(input("Enter your budget limit: "))
            print(f"Budget limit set to: {budget}")
        else:
            budget = float(input("Podaj limit budzetu: "))
            print(f"Ustawiono limit budzetu na: {budget}")

    elif choice == "6":
        if len(expenses) == 0:
            if language == "1":
                print("No expenses to delete.")
            else:
                print("Nie ma wydatkow do usuniecia.")
        else:
            if language == "1":
                print("Your expenses:")
            else:
                print("Twoje wydatki:")

            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

            if language == "1":
                number = int(input("Enter expense number to delete: "))
            else:
                number = int(input("Podaj numer wydatku do usuniecia: "))

            if 1 <= number <= len(expenses):
                removed = expenses.pop(number - 1)

                if language == "1":
                    print(f"Expense {removed} deleted successfully!")
                else:
                    print(f"Wydatek {removed} zostal usuniety!")
            else:
                if language == "1":
                    print("Invalid expense number.")
                else:
                    print("Nieprawidlowy numer wydatku.")

    elif choice == "7":
        if language == "1":
            print("Exiting the Daily Expense Tracker. Goodbye!")
        else:
            print("Zamykanie programu. Do widzenia!")
        break

    else:
        if language == "1":
            print("Invalid choice. Please try again.")
        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")
