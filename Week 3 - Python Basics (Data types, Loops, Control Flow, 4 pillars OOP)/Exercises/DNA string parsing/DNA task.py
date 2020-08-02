
class Dna:
    def dna_counter(self):

        dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

        A = []
        C = []
        G = []
        T = []

        for letter in dna:
            if letter == "A":
                A.append(letter)
            if letter == "C":
                C.append(letter)
            if letter == "G":
                G.append(letter)
            if letter == "T":
                T.append(letter)

        A_count = len(A)
        C_count = len(C)
        G_count = len(G)
        T_count = len(T)

        print(A_count, C_count, G_count, T_count)

dna1 = Dna()
dna1.dna_counter()
