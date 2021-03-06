rna_to_protein = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
    "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

inp = '''>Rosalind_9461
ATGAGAAAGACTAGGCCCCGGCCGCCCACTGATTCAGAATATTGTTCACGCCTTATCAGG
AAAGCCTTGTATGCAAGAGGTGGTACACCTCCAGTTTTCGTACGCAACAGTTGCTCGCTT
TCAATTCTAACTCAGTGTATTCGTACAGCTCGGAGAACAAACTGTTGGACACACTCCCAT
GGTGCCCTCACACAACCTGTGTCTATGAACCGAAGACCTGGCCATATTCCTTCTAGGGTA
GTGAGGATGCGGTAACGAGATAGTAGCGCCTCTGTGTGTTCCCGGTGCCACGCAAGTTTC
TCTAAAATTCCGACGATTACAGAGTCAGTCTGCGCCGCTTCACAACCTGAGAAATAGAAA
TGCCCATTTAAATCTGTATGCTACGTTTAGGACATCAGGGAGTGGGAAATCACCTCGAGA
TCAATGCATTTGGGGGAAACACATGGCCTATCATTTTTGCGCCCCGCAAACGTGGGTGTT
AGAGGGCGAGGAAATGGCTACCCTATACCGAGAGATCGCACGTGAGAACCCATGTAAGGT
CAGAGAGACTGGGTCTCTTCGAACAGACCTTCAGAGATTGTAAGAACGGTCCCTTTTGCC
TGACAGGAAACCCGGCAGAGTCACCAGAGACCCTGATCCACCGCCTGCGATAAATCATTG
CCCTAGATTTCCAGCTATGTATTGTCCGTAATAATCAGGTCACGTCTAGTCTGCACTTCC
CTTTTACTGTTCAGCGCTATGGGAATGTCGTGTGAATGGGCTGGCTCTTCACAATCAGGG
CACCATATGTCGTTTGGGCTACTATTTCAGCGGTAATAGCAAGCTCCGATGCTGAAGTTG
GGCAAAACTGCCGAGAGCGTCACTAGCCAAGTAGGTCAACCAACGTCACTTAATACCGGT
ACAGCAGCGCGGAACGCGGGACTCCCTGAATATGCAAGGCGTGGGGGCCGAGCCTCCTAC
TCCCTCTATGACACTGTATCTAAACATGGCTGA
>Rosalind_4698
GCCGCTTCACAACCTGAGAAATAGA
>Rosalind_8932
AGACCTGGCCATATTCCTTCTAGGGTAGTGA
>Rosalind_5871
GAGCGTCACTAGCCAAGTAGGTCAACCAACGTCACTTAATA
>Rosalind_1856
GACCTTCAGAGATTGTAAGAA
>Rosalind_4076
ACGTTTAGGACATCAGGGAGTGGGAAATCACC
>Rosalind_3055
ATAGTAGCGCCTCTGTGTGTTCCCGG
>Rosalind_8587
GGAACGCGGGACTCCCTGAATATGCA
>Rosalind_3655
AGAGACCCTGATCCACCGCCTGCGATAAATCATTGCCCTAGATTTC
>Rosalind_4956
GCCTTGTATGCAAGA
>Rosalind_0397
GGGGAAACACATGGCCTATCA
>Rosalind_8349
CAGCGCTATGGGAATGTCGTGTGAATGGGCTGGCTCTTCACAAT
>Rosalind_6116
AGCAAGCTCCGATGCT
>Rosalind_5268
GGTGTTAGAGGGCGAGGAAATGGCTACCCTATACCGAGAGATCGCACGT
>Rosalind_6102
CAGTGTATTCGTACAGCTCGGAGAACAAACTGTTGGACA
'''

inp = inp[1:].split('>') ## separate every entry in the dataset


inp = [i.split('\n',1)[1] for i in inp] ## remove header and only store the string value
dna = inp[0].replace('\n','')

introns = inp[1:]

for i in introns:
	dna = dna.replace(i.replace('\n',''),"")

dna = dna.replace('T','U')
rna = [dna[i:i + 3] for i in xrange(0, len(dna), 3)]


print "Protien string is",''.join([rna_to_protein[r] for r in rna])