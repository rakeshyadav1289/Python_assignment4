try:

    user_input = input("Enter some text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
    print("Data written to output.txt successfully.")


    append_input = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(append_input + "\n")
    print("Additional data appended to output.txt successfully.")


    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except PermissionError:
    print("Error: Permission denied while accessing 'output.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")