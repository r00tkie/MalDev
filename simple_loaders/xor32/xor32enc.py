import sys
import time

# XOR32 Encode 
def xor32_encode(data, key):
    encoded_data = bytearray()
    for byte in data:
	    # Apply XOR operation with the most significant byte of the key
        encoded_byte = byte ^ ((key >> 24) & 0xFF)
        encoded_data.append(encoded_byte)
        # Circular left shift the key by 1 bit
        key = ((key << 1) | (key >> 31)) & 0xFFFFFFFF  
    return bytes(encoded_data)

if __name__ == "__main__":
	if len(sys .argv) != 3:
		print("Usage: /xor32_encode.py <key> <filename>")
		exit (0)

	key = int(sys.argv[1])
	filename = sys.argv[2]

	with open(filename, 'rb') as f:
		data = f.read()

	# XOR32 Encode the data
	encoded_data = xor32_encode(data, key)


	# Write data to file
	with open(f"{filename}.enc", 'wb') as f:
		f.write (encoded_data)

	print(f"Data Written: \n")
	print(f"##### XOR32 Encoded Data Starter ##### \n")
	
	time.sleep(1)

	#print(f"{encoded_data}" + f"\n")
	print(f"##### XOR32 Encoded Data Ends ##### \n")
	print(f"+++++ Data is written at {filename}.enc +++++ \n")