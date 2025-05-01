from file_manager import read, append

def add():
    num1 = int(input("Enter your num1->(type: int): "))
    num2 = int(input("Enter your num2->(type: int): "))
    result = num1 + num2
    print("Result:", result)
    append("calculator.csv", {
        "num1": num1,
        "num2": num2,
        "operation": "+",
        "result": result
    })

def subtract():
    num1 = int(input("Enter your num1->(type: int): "))
    num2 = int(input("Enter your num2->(type: int): "))
    result = num1 - num2
    print("Result:", result)
    append("calculator.csv", {
        "num1": num1,
        "num2": num2,
        "operation": "-",
        "result": result
    })

def divide():
    num1 = int(input("Enter your num1->(type: int): "))
    num2 = int(input("Enter your num2->(type: int): "))
    if num2 == 0:
        print("Sonni 0 ga bo'lib bo'lmaydi")
        return
    result = num1 / num2
    print("Result:", result)
    append("calculator.csv", {
        "num1": num1,
        "num2": num2,
        "operation": "/",
        "result": result
    })

def multiply():
    num1 = int(input("Enter your num1->(type: int): "))
    num2 = int(input("Enter your num2->(type: int): "))
    result = num1 * num2
    print("Result:", result)
    append("calculator.csv", {
        "num1": num1,
        "num2": num2,
        "operation": "*",
        "result": result
    })

def show_all_res():
    results = read("calculator.csv")
    if not results:
        print("Hozircha hech qanday natija mavjud emas.")
        return
    print("---- Barcha natijalar ----")
    for row in results:
        print(f"{row['num1']} {row['operation']} {row['num2']} = {row['result']}")
    print("---------------------------")

def main():
    while True:
        print("""
    Menu:
        1. Add
        2. Subtract
        3. Divide
        4. Multiply
        5. Show all result
        6. Log out
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            divide()
        elif choice == "4":
            multiply()
        elif choice == "5":
            show_all_res()
        elif choice == "6":
            print("Good bye!")
            break
        else:
            print("Invalid choice!!!")

if __name__ == "__main__":
    main()
