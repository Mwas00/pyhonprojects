#file hadlind

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Write the modified content to the new file

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = "input.txt"  # Make sure this file exists or create it
output_file = "output.txt"

read_and_modify_file(input_file, output_file)


# error handling

def handle_file_errors():
    try:
        # Ask user for the filename
        filename = input("Please enter the filename to read: ")

        # Try to open the file
        with open(filename, 'r') as file:
            content = file.read()  # Read the content
            print(f"Content of {filename}:")
            print(content)  # Display the content

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
handle_file_errors()
