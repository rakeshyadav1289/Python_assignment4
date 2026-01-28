try:
    with open("test.txt", "r") as file:
      for line in file:
            print(line.strip())
except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")