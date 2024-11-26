def modify_and_copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src_file:
            content = src_file.read()  # Read the entire content of the source file

        # Modify the content (for example, convert the text to uppercase)
        modified_content = content.upper()  # Modify the content

        # Open the destination file in write mode
        with open(destination_file, 'w') as dest_file:
            dest_file.write(modified_content)  # Write the modified content to the destination file

        print(f"Content has been modified and saved to '{destination_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except IOError as e:
        print(f"Error: An IOError occurred: {e}")

# Call the function with your source and destination file paths
source = 'source.txt'  # Replace with the path to your source file
destination = 'modified_file.txt'  # Replace with the path for the new file

modify_and_copy_file(source, destination)