def xor_decrypt(hex_string, key):
    # Convierte el string hexadecimal a bytes
    data = bytes.fromhex(hex_string)

    key_bytes = key.encode()
    repeated_key = (key_bytes * ((len(data) // len(key_bytes)) + 1))[:len(data)]

    # Aplica XOR entre los datos y la clave repetida
    decrypted = bytes([b ^ k for b, k in zip(data, repeated_key)])

    try:
        return decrypted.decode('utf-8')  # Intenta decodificar a texto legible
    except UnicodeDecodeError:
        return decrypted  # Si no se puede decodificar, devuelve los bytes crudos

# Valores
hex_string = "747d737e6650545308090455040a0e0b55015d0b065254015803020b5c5f570301580e0007"
key = "21299"

resultado = xor_decrypt(hex_string, key)
print("→ Mensaje descifrado:", resultado)
