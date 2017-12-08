import pandas as pd

def get_feature_vector(trans_name='',feature_name='TPM'):
	file_name = "./data/" + trans_name + "/bias/quant.sf"
	df = pd.read_csv(file_name,sep='\t')
	tpm = df[feature_name]
	return tpm.tolist()

def 