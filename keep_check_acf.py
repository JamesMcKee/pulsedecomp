from optparse import OptionParser
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import anderson
from scipy.stats import shapiro

#Getting the options you define when calling the script.
usage="usage: check_acf.py -f file" 
parser=OptionParser()
parser.add_option("-f", "--file-name", type="string", help="file from paas fit", dest='input_file')
(opts, args) = parser.parse_args()

file=np.loadtxt(opts.input_file,skiprows=1)
bins=np.array(file[:,0])
data=np.array(file[:,1])
model=np.array(file[:,2])

resid = np.subtract(data,model)

auto_corr=np.correlate(resid,resid,mode='full')

# Anderson-Darling normality test
print("Anderson-Darling:")
result = anderson(resid)
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))

print( " ")
print( "Shapiro-Wilk:")

# Shapiro-Wilk normality test
stat, p = shapiro(resid)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

print( " ")

plt.plot(bins,data)
plt.plot(bins,model)
plt.show()
plt.close()
plt.plot(bins,resid)
plt.show()
plt.close()
#plt.plot(np.divide(auto_corr,auto_corr[np.argmax(auto_corr)]))
#plt.show()
#plt.close()
