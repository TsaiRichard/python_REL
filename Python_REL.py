#<<< To install the library>>>
#pip install reliabiliy
#<<<To upgrade the library>>> 
#pip install --upgrade reliability
#<<<quick example >>>
from reliability.Distributions import Weibull_Distribution
from reliability.Fitters import Fit_Weibull_2P
from reliability.Probability_plotting import plot_points
import matplotlib.pyplot as plt

dist = Weibull_Distribution(alpha=30, beta=2)  # creates the distribution object
data = dist.random_samples(20, seed=42)  # draws 20 samples from the distribution. Seeded for repeatability
plt.subplot(121) # which means row 1 column 2 index 1 plot empty frame 
fit = Fit_Weibull_2P(failures=data)  # fits a Weibull distribution to the data and generates the probability plot
plt.subplot(122)
fit.distribution.SF(label='fitted distribution')  # uses the distribution object from Fit_Weibull_2P and plots the survival function
dist.SF(label='original distribution', linestyle='--') # plots the survival function of the original distribution
plot_points(failures=data, func='SF')  # overlays the original data on the survival function
plt.legend() # to display the legned 
plt.show() # show the plot 

### this portion of code is to figure out the purpose of "seed"
#data1 = dist.random_samples(20) 
#plt.subplot(122)
#fit = Fit_Weibull_2P(failures=data1)
#plt.show()