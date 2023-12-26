def main():
    amount = int(input(" What is the order amount? "))
    state = input(" What is the state? ").lower().strip()
    if state == "wi":
        tax, total = output_for_wi(amount)
        print(f"The subtotal is {amount}$.\nThe tax is {tax:.2f}$.\nThe total is {total:.2f}$.")


def output_for_wi(x):
    return x * 0.055, x + x * 0.055

main()