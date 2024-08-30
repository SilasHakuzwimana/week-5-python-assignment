# file_handling_assignment.py

def create_file():
    try:
        # Creating a new file and writing initial lines
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("12345\n")
            file.write("This is the third line.\n")
        print("File created and initial lines written successfully.")
    except Exception as e:
        print(f"An error occurred during file creation: {e}")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        # Reading and displaying the contents of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Reading the contents of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("You do not have permission to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading process completed.")


def append_file():
    try:
        # Opening the file in append mode and adding additional lines
        with open("my_file.txt", "a") as file:
            file.write("Appending the fourth line.\n")
            file.write("67890\n")
            file.write("This is the final line.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("You do not have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  # Read the file again to show the appended content
