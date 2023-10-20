import struct

# Basically just calculates letter frequency
def calculate_nucleotide_frequency(file_path):
    result = {}
    total = 0.0

    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            else:
                total += 1.0
                if char not in result:
                    result[char] = 1
                else:
                    result[char] += 1

    for key in result:
        result[key] /= total

    return result


def huffman_coding(frequencies):
    # Freqs example: {'C': 0.11, 'T': 0.29, 'G': 0.11, 'A': 0.47}

    freqs = frequencies.copy()


    codebook = {letter: [] for letter in freqs}

    while(len(freqs) > 1):
        in_order = sorted(freqs, key=lambda key: freqs[key])
        min_1 = in_order.pop(0)
        min_2 = in_order.pop(0)

        total_freq = freqs[min_1] + freqs[min_2]

        del freqs[min_1]
        del freqs[min_2]

        freqs[min_1 + min_2] = total_freq


        for letter in min_1:
            codebook[letter].insert(0, 0) # lower freq gets 0
        
        for letter in min_2:
            codebook[letter].insert(0, 1) # higher freq gets 1
        
    return codebook

def encode_and_save_compressed(input_filepath, output_filepath):
    freqs = calculate_nucleotide_frequency(input_filepath)
    codebook = huffman_coding(freqs)

    string_codebook = {letter : ''.join(map(str, code)) for letter, code in codebook.items()}

    binary_data = []

    with open(input_filepath, 'r') as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break
            
            binary_data.extend(codebook[char])

    with open(output_filepath, "wb") as output_file:
        # Pack the list of integers as binary data
        binary_data_bytes = struct.pack("B" * len(binary_data), *binary_data) 
        # The struct module is used to convert the integer
        # 1s and 0s into bytes which can be written to the file
    
        # Write the binary data to the file
        output_file.write(binary_data_bytes)

    print(binary_data)


if __name__ == "__main__":
    encode_and_save_compressed('./dna.txt', 'compressed.txt')