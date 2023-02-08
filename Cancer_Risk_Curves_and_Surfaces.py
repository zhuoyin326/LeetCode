#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:20:43 2023

@author: zhuo
"""


import json
# import pprint
import statistics

# scenario 1: input path is concentration
concentration_path = "/home/zhuo/Desktop/average_results/concentration/" 

# scenario 2: input path is entropy
entropy_path = "/home/zhuo/Desktop/average_results/entropy/" 

# scenario 3: input path is concentration and entropy
concentration_and_entropy_path = "/home/zhuo/Desktop/average_results/concentration_and_entropy/" 

# select the input path for the folllowing code
data_save_path = concentration_and_entropy_path

# create a data dict folds to store the data from all folds together
data_dict_folds = []


def read_fold(fold_number):
    # read all json files from all folds 
    with open(f"{data_save_path}data_dict_fold_{fold_number}.json") as f:
        # append all files from different folds into one file
        data_dict_folds.append(json.load(f))

# iterate each fold using a for loop
# fold_number can take 1, 2, 3, 4 and 5
for fold_number in range(1,6):
    read_fold(fold_number)

# create empty feature curve json file when feature is not available
def save_empty_data_curve(feature):
    with open(f"{data_save_path}{feature}_results.json", "w") as write_file:
        data = {
            "results": [],
            "importance": {
                "importance_fold_1": None,
                "importance_fold_2": None,
                "importance_fold_3": None,
                "importance_fold_4": None,
                "importance_fold_5": None,
                "importance_fold_average": None,
                "importance_fold_std": None
            }
        }
        json.dump(data, write_file, indent = 4, sort_keys=True)

def save_data_curve(feature):
    # assume inputs are the same for each fold
    
    # the outputs are NOT the same for each fold
    hasFeature = False
    inputs = []
    for data_dict_fold in data_dict_folds:
        if feature in data_dict_fold:
            inputs = data_dict_fold[feature]["inputs"]
            hasFeature = True
            break

    if not hasFeature:
        print(f"skip '{feature} because it's not available in data_dict_folds")
        save_empty_data_curve(feature)
        return
    
    # create an empty dictionary to save importance ratio
    importance = {}
    # create an empty list to save importance ratio for each fold
    importance_nums = []
    
    # fold_number can take 1, 2, 3, 4 and 5
    for fold_number in range(1,6):
        if feature in data_dict_folds[fold_number-1]:
            # obtain importance for specific feature
            importance_metric = data_dict_folds[fold_number-1][feature]["importance"]
            importance[f"importance_fold_{fold_number}"] = importance_metric
            importance_nums.append(importance_metric)

    importance["importance_fold_average"] = sum(importance_nums) / len(importance_nums)

    # check if stdev: https://www.geeksforgeeks.org/python-statistics-stdev/
    importance["importance_fold_std"] = statistics.pstdev(importance_nums)

    # create an empty list to store results
    results = []

    # estimate the length of inputs: 41
    # iterate all input to generate result
    for i in range(len(inputs)):
        # create an dictionary to store result
        result = {
            "input": inputs[i],
        }
        # create an empty list to store fold_outputs 
        fold_outputs = []
        
        # iterate each fold using a for loop
        # fold_number can take 1, 2, 3, 4 and 5
        for fold_number in range(1,6):
            if feature in data_dict_folds[fold_number-1]:
                # obtain one of the specific feature outputs for the ith fold
                output = data_dict_folds[fold_number-1][feature]["outputs"][i]
                # write the specific feature output into the value of result dictionary
                # output_fold_i is the key of result dictionary
                result[f"output_fold_{fold_number}"] = output
                # append output into fold_outputs list for calculating the average of fold_outputs
                fold_outputs.append(output)
                
        # write calculated average of fold_outputs into the value of result dictionary
        result["output_fold_average"] = sum(fold_outputs) / len(fold_outputs)

        # check if stdev: https://www.geeksforgeeks.org/python-statistics-stdev/
        result["output_fold_std"] = statistics.pstdev(fold_outputs)

        # results is a list
        # within results list, each list element, result, is a dictionary
        results.append(result)

    with open(f"{data_save_path}{feature}_results.json", "w") as write_file:
        json.dump({"results": results, "importance": importance}, write_file, indent=4, sort_keys=True)

# save 
def save_data_surface(feature):
    # assume inputs are the same for each fold
    # the outputs are NOT the same for each fold
    hasFeature = False
    inputs = []
    for data_dict_fold in data_dict_folds:
        if feature in data_dict_fold:
            inputs = data_dict_fold[feature]["inputs"]
            hasFeature = True
            break

    if not hasFeature:
        print(f"skip '{feature} because it's not available in data_dict_folds")
        save_empty_data_curve(feature)
        return
    
    # create an empty dictionary to save importance ratio
    importance = {}
    # create an empty list to save importance ratio for each fold
    importance_nums = []
    
    # fold_number can take 1, 2, 3, 4 and 5
    for fold_number in range(1,6):
        if feature in data_dict_folds[fold_number-1]:
            # obtain importance for specific feature
            importance_metric = data_dict_folds[fold_number-1][feature]["importance"]
            importance[f"importance_fold_{fold_number}"] = importance_metric
            importance_nums.append(importance_metric)

    importance["importance_fold_average"] = sum(importance_nums) / len(importance_nums)

    # check if stdev: https://www.geeksforgeeks.org/python-statistics-stdev/
    importance["importance_fold_std"] = statistics.pstdev(importance_nums)

    # create an empty list to store results
    results = []

    # estimate the length of inputs: 41
    # iterate all input to generate result
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            # create an dictionary to store result
            result = {
                "input1": inputs[i],
                "input2": inputs[i],
            }
            # create an empty list to store fold_outputs 
            fold_outputs = []
            
            # iterate each fold using a for loop
            # fold_number can take 1, 2, 3, 4 and 5
            for fold_number in range(1,6):
                if feature in data_dict_folds[fold_number-1]:
                    # obtain one of the specific feature outputs for the ith fold
                    # write the specific feature output into the value of result dictionary
                    # output_fold_i is the key of result dictionary
                    result[f"output_fold_{fold_number}"] = output[j]
                    # append output into fold_outputs list for calculating the average of fold_outputs
                    fold_outputs.append(output[j])
                    
        # write calculated average of fold_outputs into the value of result dictionary
        result["output_fold_average"] = sum(fold_outputs) / len(fold_outputs)

        # check if stdev: https://www.geeksforgeeks.org/python-statistics-stdev/
        result["output_fold_std"] = statistics.pstdev(fold_outputs)

        # results is a list
        # within results list, each list element, result, is a dictionary
        results.append(result)

    with open(f"{data_save_path}{feature}_results.json", "w") as write_file:
        json.dump({"results": results, "importance": importance}, write_file, indent=4, sort_keys=True)



# save_data_curve("XYZ")
# feature_set = set(["XYZ"])

# create an empty set to store all features
feature_set = set()

# for each fold within data dict folks file
for fold in data_dict_folds:
    # each key within fold is a feature
    # iterate over all the keys within each fold
    for key in fold.keys():
        # add each key (feature) into the feature set
        # add is a method within set
        feature_set.add(key)

# iterate feature names over within feature_set
for feature in feature_set:
    # remove the leading and trailing spaces of the feature names 
    # split the feature name into tokens using "vs."
    tokens = feature.strip().split("vs.")
    # if the length of tokens is 1, the individual feature is find
    if len(tokens) == 1:
        # save feature curve if there is the individual feature 
        save_data_curve(feature)
    # if len(tokens) == 2:
    #     save_data_surface(feature)

# import Usage_Biophotonics_Binary_Classification as usage

# for key, value in usage.meta_info.items():
#     # may replace different condition
#     if key != 'Cancer State':
#         save_data_curve(key)



