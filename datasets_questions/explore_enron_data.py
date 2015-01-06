#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
# sys.path.append("../tools/")
# from feature_format import featureFormat, targetFeatureSplit

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# enron_data = pd.DataFrame(enron_data)
# enron_data = enron_data.T



print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


quantified_salary_count = 0
for k in enron_data:
    if enron_data[k]['salary'] != 'NaN':
        quantified_salary_count += 1
print "How many folks in this dataset have a quantified salary? ", \
        quantified_salary_count


email_address_count = 0
for k in enron_data:
    if enron_data[k]['email_address'] != 'NaN':
        email_address_count += 1
print email_address_count




