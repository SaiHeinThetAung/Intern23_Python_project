import random
import string


# Define a function to generate a random email address
def generate_email():
    # Generate a random username of length between 6 and 12 characters
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 12)))
    # Generate a random domain name of length between 6 and 10 characters
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 10)))
    # Append a random top-level domain (TLD)
    tld = random.choice(['com', 'net', 'org'])
    # Concatenate the username, domain, and TLD to form the email address
    return f"{username}@{domain}.{tld}"


# Generate 1000 random email addresses
for i in range(20):
    email = generate_email()
    print(email)
