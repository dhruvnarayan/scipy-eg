#Project 1 - Familiar

import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

vein_pack_lifespans = familiar.lifespans(package = 'vein')
tstat,vein_pack_test = ttest_1samp(vein_pack_lifespans,71)
print(vein_pack_test)

if (vein_pack_test < 0.05):
  print ("The Vein Pack Is Proven To Make You Live Longer!")
else: 
  print ("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package = 'artery')
  
tstat,package_comparison_result = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
print (package_comparison_result)

if(package_comparison_result<0.05):
  print ("The Artey Package guarantees even stronger results!")
else:
  print ("The Artery Package is also a great product!")
  iron_contingency_table = familiar.iron_counts_for_package()
  print (iron_contingency_table)
  chi2,iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
  print (iron_pvalue)

if(iron_pvalue<0.05):
  print ("The Artey Package is Proven To Make You Healthier!")
else:
  print ("While We Can't Say The Artery Package will help you, I bet it's nice!")