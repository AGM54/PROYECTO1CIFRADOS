from Crypto.Cipher import ChaCha20

def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]
    nonce = (user_id.encode() * 8)[:8]
    return key, nonce

def chacha20_decrypt(ciphertext_hex, user_id):
    ciphertext = bytes.fromhex(ciphertext_hex)
    key, nonce = generate_key_nonce(user_id)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode(errors='ignore')

# Cadena obtenida del archivo .flag
cipher_hex = "765d6c96519b340580f1493e3549fe151c33ef4a226a61f51b9265636ea7f64d009a6a0b40"

# Reemplazá con tu número de carné
user_id = "21299"

# Desencriptar
resultado = chacha20_decrypt(cipher_hex, user_id)
print("Mensaje descifrado:", resultado)
