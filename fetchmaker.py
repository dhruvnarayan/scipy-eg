#Project 2 - Fetchmaker

import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_std = np.std(rottweiler_tl)
print (rottweiler_tl_mean)
print (rottweiler_tl_std)

whippet_rescue = fetchmaker.get_is_rescue("whippet")
num_whippet_rescues = np.count_nonzero(whippet_rescue)
print (num_whippet_rescues)
num_whippets = np.size(whippet_rescue)
print (num_whippets)
pval = binom_test(num_whippet_rescues,num_whippets,0.08)
print (pval)

a = fetchmaker.get_weight("whippet")
b = fetchmaker.get_weight("terrier")
c = fetchmaker.get_weight("pitbull")
fstat,pval = f_oneway(a,b,c)
print (pval)

v = np.concatenate([a,b,c])
labels = ['whippet']*len(a) + ['terrier']*len(b) + ['pitbull']*len(c)
tukey_results = pairwise_tukeyhsd(v,labels,0.05)
print (tukey_results)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

x11 = np.count_nonzero(poodle_colors == 'black')
x12 = np.count_nonzero(shihtzu_colors == 'black')
x21 = np.count_nonzero(poodle_colors == 'brown')
x22 = np.count_nonzero(shihtzu_colors == 'brown')
x31 = np.count_nonzero(poodle_colors == 'gold')
x32 = np.count_nonzero(shihtzu_colors == 'gold')
x31 = np.count_nonzero(poodle_colors == 'grey')
x32 = np.count_nonzero(shihtzu_colors == 'grey')
x31 = np.count_nonzero(poodle_colors == 'white')
x32 = np.count_nonzero(shihtzu_colors == 'white')
x = [[x11,x12],
    [x21,x22],
    [x31,x32]]
chi2,pval,dof,expf = chi2_contingency(x)
print (pval)

																								