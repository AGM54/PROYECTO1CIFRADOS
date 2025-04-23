import random

def generate_keystream(seed, length):
    random.seed(seed)  # PRNG débil
    return bytes([random.randint(0, 255) for _ in range(length)])

def decrypt(ciphertext_hex):
    cipherbytes = bytes.fromhex(ciphertext_hex)
    for seed in range(100000):  # Rango amplio de posibles semillas
        keystream = generate_keystream(seed, len(cipherbytes))        
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])
        if plaintext.startswith(b"FLAG_"):
            print(f"✅ Semilla encontrada: {seed}")
            print(f"🔓 Texto descifrado: {plaintext.decode()}")
            break

cipher = "a77742694e4e53d3403e3b3dd4c3d5291d3e59669b4918dc454c71e910f9c380b91a02df3c"
decrypt(cipher)
