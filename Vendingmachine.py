menu = {
    'c': {
        1: "Espresso Coffee",
        2: "Cappuccino Coffee",
        3: "Latte Coffee"
    },
    't': {
        1: "Plain Tea",
        2: "Assam Tea",
        3: "Ginger Tea",
        4: "Cardamom Tea",
        5: "Masala Tea",
        6: "Lemon Tea",
        7: "Green Tea",
        8: "Organic Darjeeling Tea"
    },
    's': {
        1: "Hot and Sour Soup",
        2: "Veg Corn Soup",
        3: "Tomato Soup",
        4: "Spicy Tomato Soup"
    },
    'b': {
        1: "Hot Chocolate Drink",
        2: "Badam Drink",
        3: "Badam-Pista Drink"
    }
}

main = input().lower()
sub = int(input())

if main not in menu:
    print("INVALID INPUT!")
elif sub not in menu[main]:
    print("INVALID OPTION!")
else:
    print("Welcome to CCD!")
    print("Enjoy your", menu[main][sub] + "!")