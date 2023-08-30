import sys

# XOR32 Decode
def xor32_decode(data, key):
    decoded_data = bytearray()
    for byte in data:
        # Apply XOR operation with the most significant byte of the key
        decoded_byte = byte ^ ((key >> 24) & 0xFF)
        decoded_data.append(decoded_byte)
        # Circular left shift the key by 1 bit
        key = ((key << 1) | (key >> 31)) & 0xFFFFFFFF 
    return bytes(decoded_data)

if __name__ == "__main__":
	if len(sys .argv) != 3:
		print("Usage: /xor32_decode.py <key> <filename>")
		exit (0)

	key = int(sys.argv[1])
	filename = sys.argv[2]

	with open(filename, 'rb') as f:
		data = f.read()
		
    # Decode the data
	decoded_data = xor32_decode(data, key)

	with open(f"{filename}.decoded", 'wb') as f:
		f.write (decoded_data)

	print(f"Written {filename}.decoded")