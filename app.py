import random

name = input("Enter your name: ")
print(f"Welcome {name} to Andy's Todo App")

todos = []

while True:
    print("\nPlease select one of the following options:")
    print("1. Add a todo")
    print("2. View todos")
    print("3. Remove a todo")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        todo = input("Enter a todo: ")
        todos.append(todo)
        print(f"Todo '{todo}' added.")

        with open("todos.txt", "a") as file:
            file.write(todo + "\n")

        if len(todos) > 10:
            print("You have too many todos!")

    elif choice == '2':
        try:
            with open("todos.txt", "r") as file:
                todos = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            todos = []
        if not todos:
            print("No todos found.")
        else:
            print("Your todos:")
            for idx, todo in enumerate(todos, start=1):
                print(f"{idx}. {todo}")

    elif choice == '3':
        try:
            with open("todos.txt", "r") as file:
                todos = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            todos = []
        if not todos:
            print("No todos to remove.")
        else:
            print("Your todos:")
            for idx, todo in enumerate(todos, start=1):
                print(f"{idx}. {todo}")
            try:
                to_remove = int(
                    input("Enter the number of the todo to remove: "))
                if 1 <= to_remove <= len(todos):
                    removed_todo = todos.pop(to_remove - 1)
                    print(f"Todo '{removed_todo}' removed.")
                    with open("todos.txt", "w") as file:
                        for t in todos:
                            file.write(t + "\n")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("EXITING APP...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
