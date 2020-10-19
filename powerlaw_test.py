# Powerlaw test -  from https://stackoverflow.com/a/63443998

# First, create a degree distribution variable from your network:

degree_sequence = sorted([d for n, d in G.degree()], reverse=True) # used for degree distribution and powerlaw test

# Then fit the data to powerlaw and other distributions:

import powerlaw # Power laws are probability distributions with the form:p(x)∝x−α
fit = powerlaw.Fit(degree_sequence) 

#Take into account that powerlaw automatically find the optimal alpha value of xmin by creating a power law fit 
#starting from each unique value in the dataset, then selecting the one that results in the minimal Kolmogorov-Smirnov distance,D, 
#between the data and the fit. If you want to include all your data, you can define xmin value as follow:

fit = powerlaw.Fit(degree_sequence, xmin=1, discrete=True, 
                   fit_method="KS",)

#Then you can plot:

fig2 = fit.plot_pdf(color='b', linewidth=2)
fit.power_law.plot_pdf(color='g', linestyle='--', ax=fig2)

#On the other hand, it may not be a powerlaw distribution but any other distribution like loglinear, etc, 
# you can also check powerlaw.distribution_compare:

R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print (R, p)

# where R is the likelihood ratio between the two candidate distributions. 
#This number will be positive if the data is more likely in the first distribution, but you should also check p < 0.05

#Finally, once you have chosen a xmin for your distribution you can plot a comparisson 
# between some usual degree distributions for social networks:

plt.figure(figsize=(10, 6))
fit.distribution_compare('power_law', 'lognormal')
fig4 = fit.plot_ccdf(linewidth=3, color='black')
fit.power_law.plot_ccdf(ax=fig4, color='r', linestyle='--') #powerlaw
fit.lognormal.plot_ccdf(ax=fig4, color='g', linestyle='--') #lognormal
fit.stretched_exponential.plot_ccdf(ax=fig4, color='b', linestyle='--') #stretched_exponential


# Finally, take into account that powerlaw distributions in networks are being under discussion now, strongly scale-free networks seem to be empirically rare
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6399239/