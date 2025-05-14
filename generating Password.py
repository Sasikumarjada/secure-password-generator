import random
import string
def generate_password(length=13):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters
    remaining_length = length - len(password)
    all_chars = lowercase + uppercase + digits + special_chars
    password.extend(random.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the password characters
    random.shuffle(password)
    
    # Join the characters into a string
    return ''.join(password)

if __name__ == "__main__":
    # Example usage
    password = generate_password()
    print(f"Generated password: {password}")
    # Let's explain how this password generator works:
    
    # 1. First, we import the required modules:
    #    - random: For generating random choices
    #    - string: For accessing predefined character sets
    
    # 2. We define a function that takes an optional length parameter (default is 12)
    #    def generate_password(length=12)
    
    # 3. We set up our character sets using string module:
    #    - lowercase letters (a-z)
    #    - uppercase letters (A-Z)
    #    - digits (0-9)
    #    - special characters (!@#$% etc.)
    
    # 4. We ensure password complexity by forcing at least one character from each set:
    #    - One lowercase letter
    #    - One uppercase letter
    #    - One digit
    #    - One special character
    #    This creates an initial list of 4 characters
    
    # 5. Calculate remaining length needed (total length - 4 initial characters)
    
    # 6. Create a pool of all possible characters by combining all character sets
    
    # 7. Fill the remaining length with random characters from the combined pool
    
    # 8. Shuffle the entire password list to randomize character positions
    
    # 9. Join all characters into a final string
    
    # 10. When run directly (not imported), generate and print a sample password
    
    print("\nThis code ensures strong passwords by:")
    print("- Including at least one character from each required set")
    print("- Randomizing character positions")
    print("- Allowing customizable length (default 12 characters)")
