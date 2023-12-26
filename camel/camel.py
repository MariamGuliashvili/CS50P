def camel_to_snake(variable_name):
    snake_name = ""
    for characters in variable_name:
        if characters.upper():
            snake_name += "_" + characters.lower()
        else:
            snake_name += characters

    if snake_name.startswith("_"):
        snake_name = snake_name[1:]
    return snake_name

def main():
    camel_case_name = input("Enter a variable name in camel case: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print(f"first_name is: {snake_case_name}" )
   
if __name__ == "__main__":
    main()
