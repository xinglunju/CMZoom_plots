
# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as ticker

from matplotlib import rc, rcParams
from matplotlib.font_manager import fontManager, FontProperties
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text',usetex=True)
rcParams['text.latex.preamble'] = [ r'\usepackage{siunitx}', r'\sisetup{detect-all}', r'\usepackage{helvet}', r'\usepackage{sansmath}', r'\sansmath']
rcParams.update({'font.size': 64})
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = 'on'
rcParams['ytick.right'] = 'on'
rcParams['axes.xmargin'] = 0
rcParams['xtick.major.size'] = 25
rcParams['xtick.minor.size'] = 15
rcParams['ytick.major.size'] = 25
rcParams['ytick.minor.size'] = 15

## Pick colors for the three compact tracks
# Forgive my bad taste for colors
c1 = 'deepskyblue'
c2 = 'navy'
#c2 = 'cornflowerblue'
#c3 = 'navy'

## Read in uv data
uwave1, vwave1 = np.loadtxt('sgrb2_20140610_com_uvwave_15ptgs.txt', usecols = (0,1), unpack = True)
uwave2, vwave2 = np.loadtxt('sgrb2_20140327_subcom_uvwave_15ptgs.txt', usecols = (0,1), unpack = True)

uwave3, vwave3 = np.loadtxt('20150511_com_uvwave_20ptgs.txt', usecols = (0,1), unpack = True)
uwave4, vwave4 = np.loadtxt('20160504_com_uvwave_20ptgs.txt', usecols = (0,1), unpack = True)
uwave5, vwave5 = np.loadtxt('20150607_subcom_uvwave_20ptgs.txt', usecols = (0,1), unpack = True)

# From meter to unit wavelength (1.33 mm)
#uwave3 /= 1.33e-3; vwave3 /= 1.33e-3
#uwave4 /= 1.33e-3; vwave4 /= 1.33e-3
#uwave5 /= 1.33e-3; vwave5 /= 1.33e-3

##
fig = plt.figure(511, figsize=(60,14))
fig.text(0.005,0.55,r'$v$ (k$\lambda$)',rotation='vertical')
fig.text(0.50,0.03,r'$u$ (k$\lambda$)')


####### First target, G0.699-0.028
## compact, 8 ant
p1 = fig.add_subplot(511, position=[0.05,0.15,0.186,0.84])

p1.scatter(uwave1/1e3, vwave1/1e3, s=1, marker='.', color=c2)
p1.scatter(-uwave1/1e3, -vwave1/1e3, s=1, marker='.', color=c2)
p1.text(-100,100,r'Compact (8 ant)', color=c2, size='medium', weight='black')
p1.text(-100,-100,r'G0.699-0.028', color='black', size='large', weight='black')

## compact + subcom
p2 = fig.add_subplot(521, position=[0.236,0.15,0.186,0.84])
p2.set_yticklabels(())

p2.scatter(uwave1/1e3, vwave1/1e3, s=1, marker='.', color=c2)
p2.scatter(-uwave1/1e3, -vwave1/1e3, s=1, marker='.', color=c2)
p2.scatter(uwave2/1e3, vwave2/1e3, s=1, marker='.', color='red', zorder=10)
p2.scatter(-uwave2/1e3, -vwave2/1e3, s=1, marker='.', color='red', zorder=10)
p2.text(-100,100,r'Compact (8 ant) +', color=c2, size='medium', weight='black')
p2.text(-100,83,r'Subcompact (7 ant)', color='red', size='medium', weight='black')
p2.text(-100,-100,r'G0.699-0.028', color='black', size='large', weight='black')



####### Next target, G0.891-0.048
## compact, 6 ant
p3 = fig.add_subplot(531, position=[0.432,0.15,0.186,0.84])
p3.set_yticklabels(())

p3.scatter(uwave3/1e3, vwave3/1e3, s=1, marker='.', color=c1)
p3.scatter(-uwave3/1e3, -vwave3/1e3, s=1, marker='.', color=c1)
p3.text(-100,100,r'Compact (6 ant)', color=c1, size='medium', weight='black')
p3.text(-100,-100,r'G0.891-0.048', color='black', size='large', weight='black', zorder=10)

## compact, repeated, 7 ant
p4 = fig.add_subplot(541, position=[0.618,0.15,0.186,0.84])
p4.set_yticklabels(())

p4.scatter(uwave3/1e3, vwave3/1e3, s=1, marker='.', color=c1)
p4.scatter(uwave4/1e3, vwave4/1e3, s=1, marker='.', color=c2,zorder=6)
p4.scatter(-uwave3/1e3, -vwave3/1e3, s=1, marker='.', color=c1)
p4.scatter(-uwave4/1e3, -vwave4/1e3, s=1, marker='.', color=c2,zorder=6)
p4.text(-100,100,r'Compact (6 ant) +', color=c1, size='medium', weight='black')
p4.text(-100,83,r'Compact (7 ant)', color=c2, size='medium', weight='black')
p4.text(-100,-100,r'G0.891-0.048', color='black', size='large', weight='black', zorder=10)

## compact + subcompact
p5 = fig.add_subplot(551, position=[0.804,0.15,0.186,0.84])
p5.set_yticklabels(())

p5.scatter(uwave3/1e3, vwave3/1e3, s=1, marker='.', color=c1)
p5.scatter(uwave4/1e3, vwave4/1e3, s=1, marker='.', color=c2,zorder=6)
p5.scatter(uwave5/1e3, vwave5/1e3, s=1, marker='.', color='red', zorder=9)
p5.scatter(-uwave3/1e3, -vwave3/1e3, s=1, marker='.', color=c1)
p5.scatter(-uwave4/1e3, -vwave4/1e3, s=1, marker='.', color=c2,zorder=6)
p5.scatter(-uwave5/1e3, -vwave5/1e3, s=1, marker='.', color='red', zorder=9)
p5.text(-100,100,r'Compact (6 ant) +', color=c1, size='medium', weight='black', zorder=10)
p5.text(-100,83,r'Compact (7 ant) +', color=c2, size='medium', weight='black', zorder=10)
p5.text(-100,66,r'Subcompact (7 ant)', color='red', size='medium', weight='black', zorder=10)
p5.text(-100,-100,r'G0.891-0.048', color='black', size='large', weight='black', zorder=10)

for pp in [p1,p2,p3,p4,p5]:
	pp.set_xlim(-120,120)
	pp.set_ylim(-120,120)
	pp.xaxis.set_minor_locator(ticker.MultipleLocator(10))
	pp.xaxis.set_major_locator(ticker.MultipleLocator(50))
	pp.yaxis.set_minor_locator(ticker.MultipleLocator(10))
	pp.yaxis.set_major_locator(ticker.MultipleLocator(50))

##############################
plt.draw()

# Save figure
fig.set_rasterized(True)
#fig.savefig('CMZoom_uv_coverage.eps')
fig.savefig('CMZoom_uv_coverage_5panels_v4_rasterized.pdf')
