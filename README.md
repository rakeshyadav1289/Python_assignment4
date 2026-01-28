# Python_assignment4
******************************task 1******************************
-> This task 1 . In this program I create a program where a test.txt file and I read
this file 
try:
    with open("test.txt", "r") as file:
      for line in file:
            print(line.strip())
-> I use exception handling for if any error come to read this file
except FileNotFoundError:
        print("Error: The file 'test.txt' was not found.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")

**********************************taks 2**********************************
-> In this program, I write a program that take input from user and append this
input inside a txt file which name is output.txt
-> This program handle by exception handling , I take a input by user and append 
inside ouput.txt

user_input = input("Enter some text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")
    print("Data written to output.txt successfully.")
-> now again show prompt to user please enter again some text inside output.txt

append_input = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(append_input + "\n")
    print("Additional data appended to output.txt successfully.")
-> And show final output which user input before 

    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        for line in file:
            print(line.strip())
-> this part is error handling if some change this file name which is set by default
then error come output.txt not found or file access issue related
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
except PermissionError:
    print("Error: Permission denied while accessing 'output.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
