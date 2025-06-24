#Shopping cart

# This a shopping cart programme will continuously ask the user for a food products and the price of that product
# It have an exit clause if the user wish to stop adding more things to their cart
# At the end show the food items and the total cost to the user


# shopping_cart.py

def add_to_cart(food, price, cart):
    cart['foods'].append(food)
    cart['prices'].append(price)
    return cart

def calculate_total(prices):
    return sum(prices)

def main():
    foods = []
    prices = []
    total = 0

    while True:
        food = input("Enter a food to buy or press q to quit: ")
        if food.lower() == 'q':
            break
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)

    print("-----------YOUR CART------------")
    for food in foods:
        print(food)
    total = calculate_total(prices)
    print(f"Your total is: R{total}")

if __name__ == "__main__":
    main()
