import sys

def rc4_decrypt(data, key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    decrypted_data = bytearray()

    # Key-scheduling algorithm
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm
    i = j = 0
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        decrypted_byte = byte ^ S[(S[i] + S[j]) % 256]
        decrypted_data.append(decrypted_byte)

    return decrypted_data

if __name__ == "__main__":
	if len(sys .argv) != 3:
		print("Usage: /rc4_decrypt.py <key> <filename>")
		exit (0)

	key = sys.argv[1]
	filename = sys.argv[2]

	with open(filename, 'rb') as f:
		data = f.read()

	decrypted_data = rc4_decrypt(data, key.encode())

	with open(f"{filename}.decrypt", 'wb') as f:
		f.write(decrypted_data)

	print(f"Written {filename}.decrypt")
	
