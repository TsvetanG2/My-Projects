def softuni_parking(cars):

    car_dict = dict()

    for i in range(cars):
        car = input().split(" ")
        command = car[0]
        name = car[1]

        if command == 'register':
            if name not in car_dict:
                car_dict[name] = car[2]
                print(f"{name} registered {car[2]} successfully")
            else:
                print(f"ERROR: already registered with plate number {car[2]}")
        elif command == "unregister":
            if name not in car_dict:
                print(f"ERROR: user {name} not found")
            else:
                print(f"{name} unregistered successfully")
                del car_dict[name]

    for k, v in car_dict.items():
        print(f"{k} => {v}")


number_of_cars = int(input())
softuni_parking(number_of_cars)