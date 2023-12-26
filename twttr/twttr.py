def main():
    text = input("input: ")
    print(f"output: {shorten(text)}")

def shorten(x):
    for j in x:
        if j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or j == "A" or j == "E" or j == "I" or j == "O" or j == "U":
            x = (x.replace(j, ""))
    return(x)

if __name__ == "__main__":
    main()
