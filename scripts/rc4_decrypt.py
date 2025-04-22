def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    # KSA (Key-scheduling algorithm)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-random generation algorithm)
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return bytes(out)

# Valores
hex_cipher = "19bf4e600ec75e3df6123429ae0b5daad40d8699f1274edccf5541aaef9fd10cbd813745d0"
key = "21299"

# Convertir a bytes
cipher_bytes = bytes.fromhex(hex_cipher)
key_bytes = key.encode()

# Desencriptar
plaintext = rc4(key_bytes, cipher_bytes)

try:
    print("→ Mensaje descifrado:", plaintext.decode('utf-8'))
except UnicodeDecodeError:
    print("→ Mensaje descifrado (raw):", plaintext)
