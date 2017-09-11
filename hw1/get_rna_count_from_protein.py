

p_to_count = {'A': 4, 'R': 6, 'N': 2, 'D':2, 'C':2, 'Q':2, 'E':2, 'G':4, 'H':2, 'I':3, 'L':6, 'K':2, 'M':1, 'F':2, 'P':4, 'S':6, 'T':4, 'W':1, 'Y':2, 'V':4, 'STOP':3}

inp = "MKPSCVEFTKFPVNWNVFDWMRVQVHGDMPHISRVNLDERVELDGPCFDESLQADFAYIKHMDEHVLIVGMPMIAKTNGADVWSCTGEDFLHHFWCEEDLWHRKVGITFYCIYQASAMFMITMEHIMAEIRSNGPTYPWSPKSQWGAIMPVHDEKYTMGFSGVQEPFFPRPTRVLEGQERFVGNSKYGWLHWRVANPEKYQEGLYWKFHKWYPKARLTNLRYPGWRDGRLHIAHYIYEEWNKMCQSGNRLLKRYLASCVLLNRSRFSYTILDRCGNGLLFVHYIVHWHWNGDMIMKYGACIKQWSQMFDLFFCRATGKWWRAEETEWLVDQTECLEGQMYAVNTLVFMDDDSPWSLEWNGKSLFRMVHHHYNLNVGLTEWEYAPFDLIPGTGHWATVMFNMFYCKPFGDQDSAVWFMDCCHAEDFCVICYFFFDGFIIYVNGQHMMYVAERKMKPEDYCDGYWARQHATICDTFDTMRHCHQSFCFEWKMMSCRQSRWANKDAIEPWRQSTMLPDIQPSEEPYDCCGMMGYSANYLFLILGKLYWRNDLEIVRFSELGQDCLNLTQDDFNFEQCYFNFVYLPGPVPHAGKYFVELGRQKCKRCIPNFKWKDAGCARMHEKTSAEPARWGPRAFRTGIDLCDLEDFQEVQKHKPRETNSNCWIWVCKHYQRECANPRYRHWDEGFFGCWHLHHMRTKDVRYTRPTTCFFFYLQIRGMGLFKCKVLTQWHHLAHFHQFGCQIRSCTYWSSDGRVNHSMDVQQQWVAAHHMIEAEYDEVVIYDPSHLQHICAKTALGNKPYIETKRTGRSFTEERAYCDAVIHWTIGEQFRDTHVPHKEKPNGIPCQFRVVTKQCMMNFYVKTHQMDNGCLMQHIMRNVSWKCNIYMECCRQPEKCLHEWHNICMNEVNAIQWTFDPVQWRRIMPVLQCAWVRTRMYTFLTEMMDYTWRRKLTNDALSSHNVMIIDGIRTDHERYWNQNCVHDRLHQRPLILYKQYQTMKSQT"

limit = 1000000

total = long(3) #minimum it has to be 3 because we use 1 for START and 3 for STOP RNAs and 1*3 = 3

for i in inp:
	if total > limit:
		total %=limit
	total*=p_to_count[i]

total %=limit
print "The total possible RNA combinations are: " + str(total)