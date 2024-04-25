import json

def main():
    
    # Load gold
    try:
        file = open('datasets/golds/curia_es.json', 'r')
        golds_data = json.load(file)
        file.close()
    except FileNotFoundError:
        print("File not found.")
    
    # Load predictions
    try:
        file = open('datasets/preds/llama2/preds_curia_llama2_esp.json', 'r')
        preds_data = json.load(file)
        file.close()
    except FileNotFoundError:
        print("Predictions file not found.")

    
    # Check that the two lists have the same length
    if len(golds_data) != len(preds_data):
        print("The number of predictions and golds is different.")
        print("Number of golds:", len(golds_data))
        print("Number of predictions:", len(preds_data))
    
    # Create a dictionary with the golds. The key is the summary. 
    golds_dict = {}
    for gold in golds_data:
        golds_dict[gold['id']] = gold
    
    # Create a dictionary with the predictions. The key is the summary.
    preds_dict = {}
    for pred in preds_data:
        preds_dict[pred['id']] = pred
    
    # Check that every key in the predictions is in the golds
    not_found = 0
    for key in preds_dict.keys():
        if key not in golds_dict:
            print("Key not found in golds:", key)
            not_found += 1
    print("Not found:", not_found)
      
    # Print the id of the first prediction and gold
    first_pred = preds_data[0]
    first_gold = golds_data[0]
    print("First prediction id:", first_pred['id'])
    print("First gold id:", first_gold['id'])
    
    # Print keys of the first prediction and gold
    print("Keys of the first prediction:")
    print(first_pred.keys())
    print("Keys of the first gold:")
    print(first_gold.keys())

    
    # # Print the first prediction and gold
    print("First gold:")
    print(json.dumps(first_gold, indent=4))
    print("First prediction:")
    print(json.dumps(first_pred, indent=4))

    # print("First gold summary:")
    # print(first_gold['summary'])
    # print("First prediction summary:")
    # print(first_pred['summary'])
   


if __name__ == "__main__":
    main()