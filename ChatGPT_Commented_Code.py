def save_data_curve(feature):
    # Check if the given feature is present in the loaded data_dict_folds
    hasFeature = False
    inputs = []
    for data_dict_fold in data_dict_folds:
        if feature in data_dict_fold:
            # Store the inputs of the feature
            inputs = data_dict_fold[feature]["inputs"]
            hasFeature = True
            break

    # If the feature is not found in any of the data_dict_folds, print a message and save an empty data curve
    if not hasFeature:
        print(f"skip '{feature} because it's not available in data_dict_folds")
        save_empty_data_curve(feature)
        return

    importance = {}
    importance_nums = []
    # Compute the importance of the feature in each fold and store it in the importance dictionary
    for i in [1, 2, 3, 4, 5]:
        if feature in data_dict_folds[i-1]:
            importance_metric = data_dict_folds[i-1][feature]["importance"]
            importance[f"importance_fold_{i}"] = importance_metric
            importance_nums.append(importance_metric)

    # Compute the average importance of the feature across all folds
    importance["importance_fold_average"] = sum(importance_nums) / len(importance_nums)

    # Compute the standard deviation of the feature's importance across all folds
    importance["importance_fold_std"] = statistics.stdev(importance_nums)

    results = []

    # Compute the results for each input
    for i in range(len(inputs)):
        result = {
            "input": inputs[i],
        }

        fold_outputs = []
        # Compute the output of the feature for each fold
        for i in [1, 2, 3, 4, 5]:
            if feature in data_dict_folds[i-1]:
                output = data_dict_folds[i-1][feature]["outputs"][i]
                result[f"output_fold_{i}"] = output
                fold_outputs.append(output)
          
        # Compute the average output of the feature for the current input
        result["output_fold_average"] = sum(fold_outputs) / len(fold_outputs)

        # Compute the standard deviation of the output of the feature for the current input
        result["output_fold_std"] = statistics.stdev(fold_outputs)

        results.append(result)

    # Save the computed results and importance to a file in JSON format
    with open(f"/Users/yunsong/Documents/zhuo/data_curve_output/{feature}.json", "w") as write_file:
        json.dump({"results": results, "importance": importance}, write_file, indent=4, sort_keys=True)
