import numpy as np
import h5py
from sklearn.model_selection import train_test_split
from tqdm import tqdm



file_path = 'waveforms_hp.h5'
def split_data(file_path, test_size):
	"""
	Take in a file and return a train and test file

	"""
	with h5py.File(file_path,"r") as f:
		hlen = (f['hp'].shape[0])
		hidx = np.arange(hlen)
		plen = (f['params'].shape[0])
		pidx = np.arange(plen)
		print(hidx, pidx)
		#quit()
		h_train_idx, h_test_idx, p_train_idx, p_test_idx=train_test_split(hidx,pidx, test_size=test_size, random_state=1998)


		h_train_idx = np.sort(h_train_idx)
		p_train_idx = np.sort(p_train_idx)
		h_test_idx = np.sort(h_test_idx)
		p_test_idx = np.sort(p_test_idx)
		
		print(h_train_idx, len(h_train_idx))
		print(h_test_idx, len(h_test_idx))
		print(p_train_idx, len(p_train_idx))
		print(p_test_idx, len(p_test_idx))

		
		with h5py.File("train_"+file_path,"w") as f_train:
			dset1 = f_train.create_dataset('hp',(len(h_train_idx),),dtype=h5py.vlen_dtype(np.dtype('float32')))
			lset1 = f_train.create_dataset('params',(len(p_train_idx),f['params'].shape[1]))

			with h5py.File("test_"+file_path,"w") as f_test:
				dset2 = f_test.create_dataset('hp',(len(h_test_idx),),dtype=h5py.vlen_dtype(np.dtype('float32')))
				lset2 = f_test.create_dataset('params',(len(p_test_idx),f['params'].shape[1]))
				print("Appending training data:")
				for i in tqdm(range(len(h_train_idx))):
					dset1[i] = f['hp'][h_train_idx[i]]
					lset1[i] = f['params'][p_train_idx[i]]
				print("Appending testing data:")
				for i in tqdm(range(len(p_test_idx))):
					dset2[i] = f['hp'][h_test_idx[i]]
					lset2[i] = f['params'][p_test_idx[i]]
				print("Closing test file")
			print("Closing train file")
		print("Closing main file")
	return

split_data(file_path, 0.2)	
