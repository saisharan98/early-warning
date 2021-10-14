import h5py
import numpy as np
from tqdm import tqdm
import pickle as pkl
import os

def truncate(file,length, sample_rate):
	"""
	truncates a waveform file to equal length snippets
	
	Parameters:
	--------------------------------------------------
	file: string
	File or path to file as string that needs to be truncated

	length: int or float
	Number of secs that the waveforms need to be truncated to

	sample_rate: int or float
	Sample rate of the waveforms during it's generation	


	Returns: None
	---------------------------------------------------
	A file with truncated waveforms is created
	Note: it is useful to note the lengths of all waveforms beforehand
	"""
	mask = length * sample_rate #90 secs
	if os.path.exists("lengths.pkl"): #check if lengths file exists
		with open('lengths.pkl','rb') as l:
			lens = pkl.load(l)
	else:
		with open('lengths.pkl','wb') as l:
			lens = []
			with h5py.File('waveforms_hp.h5','r') as f:
				for i in range(len(f['hp']))):
					lens.append(len(f['hp']))
			pkl.dump(lens,l)
	idx = np.where(lens < mask)[0]
	with h5py.File(file,'r') as f:
		hp = f['hp']
		N = len(hp) - len(idx)
		params = f['params']
		with h5py.File('truncated_waveforms_hp.h5','w') as f_new:
			d = f_new.create_dataset('hp', (N,mask))
			p = f_new.create_dataset('params',(N,4))
			for i in tqdm(range(len(d))):
				if len(hp[i]) >= mask:
					d[i] = hp[i][-mask:]
					p[i] = params[i]
			print("After truncating, waveforms:",np.array(f['hp']))
			print("Truncated waveforms shape:",f['hp'].shape)
					
	return 
truncate('waveforms_hp.h5',90,16384) 
		