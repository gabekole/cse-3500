def calculate_nucleotide_frequency(file_path):
    result = {"C": 0, "T": 0, "G": 0, "A": 0}
    total = 0.0

    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            else:
                total += 1.0
                result[char] += 1

    for key in result:
        result[key] /= total

    return result


# ONLY VALID FOR 4 Symbols
def huffman_coding(frequencies):
    # Freqs example: {'C': 0.11, 'T': 0.29, 'G': 0.11, 'A': 0.47}

    freqs = frequencies.copy()


    codebook = {"C": [], "T": [], "G": [], "A": []}

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


if __name__ == "__main__":
    freqs = calculate_nucleotide_frequency('./dna.txt')
    
    codebook = huffman_coding(freqs)
    
    print(freqs)
    print(codebook)