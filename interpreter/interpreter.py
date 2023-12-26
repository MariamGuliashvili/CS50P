exp = input("Expression:    ").split(" ")

x,y,z = exp

n1 = float(x)
n2 = float(z)

if y == "+":
    print(f"{n1+n2}")
elif y == "-":
    print(f"{n1-n2}")
elif y == "*":
    print(f"{n1*n2}")
elif y == "/":
    print(f"{n1/n2}")

