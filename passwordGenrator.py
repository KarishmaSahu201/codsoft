import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets for password complexity
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters based on complexity
    pool = lower_letters + upper_letters + digits + special_characters

    # Check if the requested length is valid
    if length < 1:
        return "Password length must be at least 1 character."

    # Generate the password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

# Main function
def main():
    print("Welcome to the Password Generator!")

    # Prompt the user for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
