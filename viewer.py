import matplotlib
matplotlib.use('Agg')
import mpi4py
mpi4py.rc.initialize = False
from pycbc.waveform import get_td_waveform
from matplotlib.pyplot import *
import numpy as np
import h5py
import pickle as pkl
from tqdm import tqdm
from time import time
from matplotlib import transforms
from scipy import ndimage
N=50176



"""
print("Opening file")
figure(figsize=(12,8))
with h5py.File('truncated_waveforms_hp.h5','r') as f:
	plot(f['hp'][1234])
	title("My truncated waveform with \n params={}".format(f['params'][1234]))
	ylabel("Strain")
	xlabel("Time")
	savefig("truncated_waveforms_eg.png")
with h5py.File('waveforms_hp.h5','r') as f:
	plot(f['hp'][1234])
	title("My truncated waveform + regular waveformwith \n params={}".format(f['params'][1234]))
	ylabel("Strain")
	xlabel("Time")
	savefig("waveforms_eg.png")
"""
"""
figure(figsize=(8,8))
with h5py.File('truncated_waveforms_hp.h5','r') as f:
	pick_range=32
	merger = np.argmax(np.absolute(f['hp'][1234]))
	subplot(211)
	plot(f['hp'][1234][-16384*(pick_range + 2):])
	title("Slice till end length = {}\n params={}".format(f['hp'][1234][-16384*(pick_range + 2):].shape,f['params'][1234]))
	ylabel("Strain")
	xlabel("Time")
	subplot(212)
	plot(f['hp'][1234][merger -16384*(pick_range + 2):])
	title("Slice with merger length = {} \n params={}".format(f['hp'][1234][merger -16384*(pick_range + 2):].shape,f['params'][1234]))
	ylabel("Strain")
	xlabel("Time")
	tight_layout()
	savefig("truncated_waveforms_slices_eg.png")
	print(f['params'][1233],f['params'][1234],f['params'][1235])
"""
"""
with h5py.File('test_im_32.h5','r') as f:
	i = np.random.randint(len(f['im']))
	im = f['im'][i]
	p = f['params'][i]
	print("im.shape:",im.shape)
	figure(figsize=(12,12))
	rotated_img1 = ndimage.rotate(im[0], 270)
	rotated_img2 = ndimage.rotate(im[1], 270)
	rotated_img3 = ndimage.rotate(im[2], 270)
	base = gca().transData
	rot = transforms.Affine2D().rotate_deg(270)
	subplot(311)
	imshow(rotated_img1)
	title("spectrogram with params = {} \n channel 1".format(p))
	subplot(312)
	imshow(rotated_img2)
	title("spectrogram with params = {} \n channel 2".format(p))
	subplot(313)
	imshow(rotated_img3)
	title("spectrogram with params = {} \n channel 3".format(p))
	tight_layout()
	savefig("random_spec.png")
"""
with h5py.File('test_im_32.h5','r') as f:
	print(len(f['im']))
	print(f['target'][:])
	print(np.count_nonzero(f['target']))






