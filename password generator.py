import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    if length < 4:
        return "Password length should be at least 4 to include all character types."

    # Create a random password
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the remaining length with random characters from all sets
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the resulting password list
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def main():
    print("........................Password Generator.........................")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")
        
        
if __name__ == "__main__":
    main()

