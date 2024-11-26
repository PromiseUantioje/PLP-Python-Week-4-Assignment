def read_file():
    # Ask the user for the filename
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            # Read and print the content of the file
            content = file.read()
            print("File content:\n", content)

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        # Handle the case where the file cannot be read due to permissions
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IOError as e:
        # Handle other IO errors (e.g., disk errors)
        print(f"Error: An unexpected error occurred while reading the file '{filename}': {e}")

# Run the function
read_file()