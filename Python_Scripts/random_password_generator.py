import random
import string

def generate_password(length):
  """Generate a strong random password of the specified length."""
  # Create a list of all possible characters.
  chars = string.ascii_letters + string.digits + string.punctuation

  # Generate a random password of the specified length.
  password = "".join(random.choice(chars) for character in range(length))

  # Return the password.
  return password

# Prompt the user for the number of characters in the password.
length = int(input("How many characters do you want in your password? "))

# Generate a random password of the specified length.
password = generate_password(length)

# Print the password to the console.
print(password)
