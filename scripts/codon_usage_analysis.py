import matplotlib.pyplot as plt
import seaborn as sns

def read_dna_sequence(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read().replace('\n', '').upper()
    return sequence

def count_codons(sequence):
    codon_count = {}
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1
    return codon_count

def plot_codon_usage(codon_count):
    codons = list(codon_count.keys())
    counts = list(codon_count.values())

    plt.figure(figsize=(15, 6))
    sns.barplot(x=codons, y=counts, palette="viridis")
    plt.xticks(rotation=90)
    plt.xlabel('Codon')
    plt.ylabel('Frequency')
    plt.title('Codon Usage Frequency')
    plt.show()

def main(file_path):
    sequence = read_dna_sequence(file_path)
    codon_count = count_codons(sequence)
    plot_codon_usage(codon_count)

if __name__ == "__main__":
    file_path = '../data/dna_sequence.txt'  # Update this to your file path if necessary
    main(file_path)
