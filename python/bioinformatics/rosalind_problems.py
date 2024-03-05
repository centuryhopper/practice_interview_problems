#!/usr/bin/python
from collections import Counter

dna_comp_map = {"A": "T", "T": "A", "C": "G", "G": "C"}


def count_dna_nucleotides(dna):
    dna = dna.upper()
    output = {}
    for c in dna:
        output[c] = output.get(c, 0) + 1
    # print(output)
    print(output["A"], output["C"], output["G"], output["T"])


def transcription(dna) -> str:
    dna = dna.upper()
    return dna.replace("T", "U")


def reverse_complement(dna) -> str:
    dna = dna.upper()
    dna = dna[::-1]
    output = []
    for ch in dna:
        output.append(dna_comp_map[ch])
    return "".join(output)


def gc_content(dna) -> float:
    dna = dna.upper()
    counts = Counter(dna)
    g_proportion = counts["G"] / len(dna)
    c_proportion = counts["C"] / len(dna)
    return (g_proportion + c_proportion) * 100


def hamming_distance(a, b) -> int:
    if len(a) != len(b):
        return -1
    return sum(1 for ch1, ch2 in zip(a, b) if ch1 != ch2)


print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

# print(
#    gc_content(
#        "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
#    )
# )

# count_dna_nucleotides(
#    "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# )


# print(transcription("GATGGAACTTGACTACGTAAATT"))
