#Project 3 - Nosh Mish Mosh

import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
total_visitor_count = len(all_visitors)
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)
baseline_percent = paying_visitor_count * 100 / total_visitor_count
print (baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240/average_payment)
percentage_point_increase = new_customers_needed * 100 / total_visitor_count
print (percentage_point_increase) 

minimum_detectable_effect = percentage_point_increase * 100 / baseline_percent
print (minimum_detectable_effect)
ab_sample_size = 280

#statistical_significance = 90%