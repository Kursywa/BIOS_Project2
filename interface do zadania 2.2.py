import argparse

def main(argument, file_path):
    # Your main code here

    # Example of an if statement based on the value of 'argument'
    if argument == 'rna':
        print("shoving rna angels")
        #daj funkcję z rna
    elif argument == 'protein':
        print("shoving protein angels")
        #tu z proteinami
    else:
        print("choose correct argument (rna/protein)")

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add the argument and file path parameters
    parser.add_argument('argument', type=str)
    parser.add_argument('file_path', type=str)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args.argument, args.file_path)
