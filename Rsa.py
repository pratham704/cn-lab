import random
from sympy import isprime, mod_inverse, gcd

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Function to generate RSA key pairs using sympy
def generate_key_pair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
            
    d = mod_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)
    
    return public_key, private_key

# Function to encrypt a message
def encrypt(public_key, message):
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]


# Function to decrypt a message
def decrypt(private_key, cipher_text):
    n, d = private_key
    return  ''.join([chr(pow(char, d, n)) for char in cipher_text])

if __name__ == "__main__":
    bits = 8  
    public_key, private_key = generate_key_pair(bits)
    
    print(f" Generated Public Key : {public_key} \n Generated Private Key : {private_key}")
    
    message = input(" Enter the Message to be Encrypted : ")
    print(" Original message:", message)
    
    encrypted_message = encrypt(public_key, message)
    print(" Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(private_key, encrypted_message)
    print(" Decrypted message:", decrypted_message)
