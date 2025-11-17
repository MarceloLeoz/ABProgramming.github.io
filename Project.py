# APP Deportiva de Matrículas

def register_athlete(list):
    name = input("Insert the name of the athlete: ")
    age = int(input("Inserte the age of the athlete: "))
    sport = input("Inserte the sport of the athlete: ")
    fee = float(input("Inserte the mensal fee of the athlete: "))
    athlete = {
        "name": name,
        "age": age,
        "sport": sport,
        "fee": fee
    }
    list.append(athlete)
    print("✅ athlete successfully registered.\n")

def show_athlete(list):
    if not list:
        print("There is no athlete registered yet.\n")
    else:
        print("\n--- ATHLETES LIST ---")
        for d in list:
            print(f"Name: {d['name']}, Age: {d['age']}, Sport: {d['sport']}, Fee: €{d['fee']:.2f}")
        print()

def calculate_total(list):
    total = sum(d["fee"] for d in list)
    print(f"💶 Total profit: €{total:.2f}\n")

def sportive_app():
    athlete_list = []
    while True:
        print("===== SPORTS REGISTRATION APP =====")
        print("1. Register athlete ")
        print("2. Show athlete list")
        print("3. Calcular total profit")
        print("4. Exit")
        option = input("Select one option: ")

        if option == "1":
            register_athlete(athlete_list)
        elif option == "2":
            show_athlete(athlete_list)
        elif option == "3":
            calculate_total(athlete_list)
        elif option == "4":
            print("👋 Thanks for using the app.")
            break
        else:
            print("Invalid option, try again.\n")

sportive_app()
            

