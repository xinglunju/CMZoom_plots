
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.colors as colors
import matplotlib.ticker as ticker

from matplotlib import rc, rcParams
from matplotlib.font_manager import fontManager, FontProperties
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text',usetex=True)
rcParams['text.latex.preamble'] = [
    r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
	r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
	r'\usepackage{helvet}',    # set the normal font here
	r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
	r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]
#rc('font',**{'family':'serif','serif':['Computer Modern']})
rcParams.update({'font.size': 14})
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = 'on'
rcParams['ytick.right'] = 'on'
rcParams['axes.xmargin'] = 0
rcParams['xtick.major.size'] = 6

# Plot spectra
fig = plt.figure(111,figsize=(10, 5))

fig.text(0.42,0.03,r'Sky Frequency (GHz)')

## Define the correlator configurations
# 48 ASIC
corr_asic = np.array([216.909,218.892,218.909,220.892, 228.934,230.917,230.934,232.917])
# 48 ASIC + 2 x 1.66 GHz SWARM
corr_swarm1 = np.array([212.776,214.44,215.411,217.075, 232.776,234.44,235.411,237.075])
# 48 ASIC + 2 x 2.08 GHz SWARM
corr_swarm2 = np.array([212.842,214.922,215.061,217.141, 232.842,234.922,235.061,237.141])
# 40 ASIC + 4 x 2.08 GHz SWARM
corr_asic_minus8 = np.array([216.905,217.905,218.217,218.888,218.905,219.576,219.889,220.888, 228.905,229.905,230.218,230.889,230.906,231.577,231.890,232.889])
corr_swarm3 = np.array([212.748,214.828,216.748,218.828,214.967,217.047,218.967,221.047, 228.748,230.828,232.748,234.828,230.998,233.047,234.998,237.047])
# All SWARM (May 2017 -- Jul 2017)
corr_swarm4 = np.array([211.354,213.642,213.365,215.653,215.354,217.642,217.365,219.653, 227.354,229.642,229.364,231.652,231.354,233.642,233.364,235.652])

# Plot the correlator coverages
spec = fig.add_subplot(111,position=[0.02,0.12,0.96,0.87])
spec.set_ylim(0,10)
spec.set_xlim(211,238)
spec.xaxis.set_minor_locator(ticker.MultipleLocator(1))
spec.xaxis.set_major_locator(ticker.MultipleLocator(5))
spec.set_yticklabels(())

for i in range(0, len(corr_asic), 2):
	spec.plot(corr_asic[i:i+2], np.ones(len(corr_asic))[i:i+2]*9, 'b|-')
spec.text(217,9.2,r'ASIC only (May 2014 -- May 2015)',color='black',size='medium',weight='black')

for i in range(0, len(corr_asic), 2):
	spec.plot(corr_asic[i:i+2], np.ones(len(corr_asic))[i:i+2]*7.5, 'b|-')
for i in range(0, len(corr_swarm1), 2):
	spec.plot(corr_swarm1[i:i+2], np.ones(len(corr_swarm1))[i:i+2]*7.3, 'r|-')
spec.text(217,7.7,r'ASIC + 2$\times$1.66 GHz SWARM (May 2015 -- Aug 2015)',color='black',size='medium',weight='black')

for i in range(0, len(corr_asic), 2):
	spec.plot(corr_asic[i:i+2], np.ones(len(corr_asic))[i:i+2]*6, 'b|-')
for i in range(0, len(corr_swarm2), 2):
	spec.plot(corr_swarm2[i:i+2], np.ones(len(corr_swarm2))[i:i+2]*5.8, 'r|-')
spec.text(217,6.2,r'ASIC + 2$\times$2.08 GHz SWARM (Mar 2016)',color='black',size='medium',weight='black')

for i in range(0, len(corr_asic_minus8), 2):
	spec.plot(corr_asic_minus8[i:i+2], np.ones(len(corr_asic_minus8))[i:i+2]*4.5, 'b|-')
for i in range(0, len(corr_swarm3), 2):
	spec.plot(corr_swarm3[i:i+2], np.ones(len(corr_swarm3))[i:i+2]*4.3, 'r|-')
spec.text(217,4.7,r'ASIC* + 4$\times$2.08 GHz SWARM (Apr 2016 -- Jun 2016)',color='black',size='medium',weight='black')

for i in range(0, len(corr_swarm4), 2):
	spec.plot(corr_swarm4[i:i+2], np.ones(len(corr_swarm4))[i:i+2]*3, 'r|-')
spec.text(217,3.2,r'SWARM only (May 2017 -- Jul 2017)',color='black',size='medium',weight='black')


# Plot several lines
lines = {'SiO 5-4':217.10498,'H$_2$CO 3$_{03}$-2$_{02}$':218.22219,'CH$_3$OH 4$_{22}$-3$_{12}$':218.44005,'C$^{18}$O 2-1':219.56035,'HNCO 10$_{0,10}$-9$_{0,9}$':219.79827,'$^{13}$CO 2-1':220.39868,'CH$_3$CN 12-11':220.74726,'SO 6$_5$-5$_4$':219.94944,'CH$_3$OH 8$_{-1,8}$-7$_{0,7}$':229.75876,'$^{12}$CO 2-1':230.538,'$^{13}$CS 5-4':231.22069}
vlsr = 0 # km/s
for line in lines:
	lines[line] *= (1 - vlsr/3e5)

for line,freq in lines.iteritems():
	#spec.plot([freq,freq],[0,0.3],'k--',linewidth=0.8)
	spec.axvline(x=freq,linestyle='dotted',color='black',linewidth=0.8)
	if line is 'CH$_3$OH 4$_{22}$-3$_{12}$' or line is 'CH$_3$CN 12-11' or line is 'SO 6$_5$-5$_4$' or line is '$^{13}$CO 2-1':
		spec.text(freq,0.3,line,rotation=90,color='black',size='x-small',weight=1000,ha='left',va='bottom',zorder=90)
	elif line is 'C$^{18}$O 2-1':
		spec.text(freq,0.3,line,rotation=90,color='black',size='x-small',weight=1000,ha='right',va='bottom',zorder=90)
	else:
		spec.text(freq,0.3,line,rotation=90,color='black',size='x-small',weight=1000,ha='center',va='bottom',zorder=90)

##################
plt.draw()

#fig.set_rasterized(True)
fig.savefig('CMZoom_spec_coverage.eps')
