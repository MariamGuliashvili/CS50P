
def main():
    price_to_pay = 50
    coins = [5, 10, 25]
    print(buy_coke(price_to_pay, coins))

def buy_coke (price_to_pay, coins):
    while price_to_pay > 0:
        uzer_input = int(input(f"Amount Due: {price_to_pay}\nInsert Coin: "))
        if uzer_input in coins:
            price_to_pay -= uzer_input
        else:
            uzer_input = int(input(f"Amount Due: {price_to_pay}\nInsert Coin: "))
    change = price_to_pay
    if price_to_pay <=0: change = abs(price_to_pay)
    return f"Change Owed: {change}"
main()