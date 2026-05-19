def calculate_total(price, quantity, percentageTax=0, percentageDiscount):
    total = price * quantity
    total -= total * percentageDiscount / 100
    total += total * percentageTax / 100
    return total

def main():
    price = 100
    quantity = 2

    total = calculate_total(price, quantity, 5, 10)
    print(f"Total amount: {total}")


main()
