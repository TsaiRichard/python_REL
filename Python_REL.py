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
#plt.show() # show the plot 