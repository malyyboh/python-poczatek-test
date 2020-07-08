
# Zapytaj uЕјytkownika o ceny trzech produktГіw i wypisz wyniki ich porГіwnania

computer_price = float(input("Ile Е›rednio kosztuje komputer? "))
car_price = float(input("Ile kosztuje typowy samochГіd? "))
bike_price = float(input("Ile kosztuje typowy rower? "))

if computer_price > car_price:
    print("Komputer jest droЕјszy od samochodu")
else:
    print("Komputer jest taЕ„szy od samochodu")

if bike_price < computer_price:
    print("Rower jest taЕ„szy niЕј komputer")
else:
    print("Rower jest droЕјszy niЕј komputer")

if car_price == bike_price:
    print("SamochГіd kosztuje tyle samo co rower")
else:
    print("SamochГіd nie kosztuje tyle samo co rower")


# PoproЕ› uЕјytkownika o wprowadzenie listy zakupГіw,
# rozdzielajД…c poszczegГіlne elementy przecinkiem.
# NastД™pnie powiedz (wypisz), czy jest to wedЕ‚ug Ciebie dЕ‚uga lista czy teЕј nie

shopping_elements = input("WprowadЕє listД™ zakupГіw, rozdzielajД…c poszczegГіlne elementy przecinkiem: ")
shopping_list = shopping_elements.split(",")

if len(shopping_list) > 4:
    print("Ale dЕ‚uga lista zakupГіw!")
else:
    print("Taka zwykЕ‚a lista zakupГіw")
