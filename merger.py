import h5py
import numpy as np
import time
from tqdm import tqdm

N = 50176
print("Total number of waveforms: ", N)
t1 = time.time()
with h5py.File("waveforms_hp.h5","w") as main_file: 
				
	print("Created main file")
	dset = main_file.create_dataset('hp',(N,),dtype=h5py.vlen_dtype(np.dtype('float32'))) 	
	print("Created waveform dataset with shape:",dset.shape)
	lset = main_file.create_dataset('params',(N,4)) 			
	print("Created params dataset with shape:",lset.shape)
	t2 = time.time()
	print("time taken to open main file:", t2 - t1, "s")
	print("Progress bar for main file:-")
	for i in tqdm(range(32)): 								
		t3 = time.time()
		with h5py.File("waveforms_hp_%d.h5"%(i+1),"r") as f: 		
			print("Opened subfile %d"%(i+1))
			t4 = time.time()
			print("Time taken to open subfile %d:"%(i+1),t4-t3,"s")
			d = f['hp'] #N//32 x some variable number (in the millions)						
			l = f['params'] #N//2 x 4
			t5 = time.time()		 					
			print("Chunk %d before appending:"%(i),dset[(N//32)*i:(N//32)*i+(N//32)])
			print("Progress bar for subfile %d:-"%(i+1))	
			for j in tqdm(range(len(tqdm(d)))):
				dset[(N//32)*i + j] = d[j]				
			lset[(N//32)*i:(N//32)*i  + (N//32)] = l
			print("Chunk %d after appending:"%(i),dset[(N//32)*i:(N//32)*i+(N//32)])
			print("Appended %d th subfile to the mainfile"%(i+1))
			t6 = time.time()
			print("Time taken to append subfile %d:"%(i+1),(t6-t5),"s")


