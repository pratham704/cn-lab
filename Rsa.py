from sympy import randprime, mod_inverse

def generate_key_pair(bits):
    p = randprime(2**(bits-1), 2**bits)
    q = randprime(2**(bits-1), 2**bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randprime(2, phi - 1)
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Function to encrypt a message
def encrypt(public_key, message):
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(private_key, cipher_text):
    n, d = private_key
    return ''.join(chr(pow(char, d, n)) for char in cipher_text)


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
