import matplotlib
matplotlib.use('Agg')
import mpi4py
mpi4py.rc.initialize = False
from pycbc.waveform import get_td_waveform
from matplotlib.pyplot import *
import numpy as np
import pickle as pkl
import lal
from itertools import product, filterfalse
from joblib import Parallel, delayed
import multiprocessing
from tqdm import tqdm
from pycbc.waveform import td_approximants, fd_approximants

#mass range
mass_ll = 1.0
mass_ul = 2.7
n_m = np.ceil((mass_ul - mass_ll)/0.2)
m1 = np.linspace(mass_ll,mass_ul,n_m, endpoint=True)
m2 = np.linspace(mass_ll,mass_ul,n_m, endpoint=True)

#spin range
spin_ll = -0.7
spin_ul = 0.7
n_s = np.floor((spin_ul - spin_ll) / 0.05)
s1 = np.linspace(spin_ll,spin_ul,n_s, endpoint=True)
s2 = np.linspace(spin_ll,spin_ul,n_s, endpoint=True)


#dataspace = list(product(m1,m2,s1,s2))
dataspace = [(m1,m2,s1,s2) for m1,m2,s1,s2 in product(m1,m2,s1,s2) if m1>=m2]
print(len(dataspace))
'''
apx = 'SEOBNRv4_ROM_NRTidalv2'
apxs = ['SEOBNRv4_opt','SEOBNRv2_opt','SEOBNRv4_ROM_NRTidalv2','SEOBNRv4_ROM']
apxs = ['SEOBNRv4_ROM_NRTidalv2_NSBH','IMRPhenomD_NRTidalv2','IMRPhenomPv2_NRTidalv2']
sample_f = 4*4096.0
print(td_approximants())
f_low = 30
figure(figsize=(12,12))
clf()

for i,apx in enumerate(apxs):
	hp,hc = get_td_waveform(approximant=apx, mass1=dataspace[1000][0],mass2=dataspace[1000][1],spin1z=dataspace[1000][2],spin2z=dataspace[1000][3],inclination=0,coa_phase=0,delta_t=1.0/sample_f,f_lower=f_low)
	subplot(311+i)
	title("apx={},params={}\nsample_f={},f_low={}".format(apxs[i],dataspace[1000],sample_f,f_low))
	plot(hp, label="hp",c='b')
	#plot(hc, label="hc",alpha=0.4, c='r')
	#xlim([len(hp) - 5000, len(hp) + 5000])
	legend()
	tight_layout()
savefig('figs/wave_{}_masses{}.png'.format(apxs,[dataspace[1000][0],dataspace[1000][1]]))
#SEOBNRv4T_surrogate
'''
figure()
sample_f = 4*4096.0
f_low = 20
apx = 'SEOBNRv4_ROM_NRTidalv2'
hp,hc = get_td_waveform(approximant=apx, mass1=1.0,mass2=1.0,spin1z=-0.7,spin2z=0.7,inclination=0,coa_phase=0,delta_t=1.0/sample_f,f_lower=f_low)
plot(hp.get_sample_times(),hp)
xlim([-0.007, 0.003])
savefig('figs/wave.png')







