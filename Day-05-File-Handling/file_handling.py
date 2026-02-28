
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    with open("PYTHON BACK END/Day-05-File-Handling/notes.txt", "a") as file:
        file.write(f"\n{title}\n{content}")
        print("Note added successfully!")

def view_notes():
    with open("PYTHON BACK END/Day-05-File-Handling/notes.txt", "r") as file:
        data = file.read()
        print(data)

def main():
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()