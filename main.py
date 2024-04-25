import evaluate
import pandas as pd

def evaluate_rouge(texts, summaries, lang='en'):
    results = evaluate.load('rouge', trust_remote_code=True).compute(references=texts, 
                                                                   predictions=summaries)
    return results

# def evaluate_bert_score(texts, summaries, lang='en'):
#     bert_score = load_metric('bertscore')
#     results = bert_score.compute(predictions=summaries, references=texts, lang=lang)  # specify 'en' or 'es' based on your dataset
#     return results


def main():
    # Load gold
    try:
        golds_data = pd.read_json('datasets/golds/curia_es.json')
    except FileNotFoundError:
        print("File not found.")

    # Load predictions
    try:
        preds_data = pd.read_json('datasets/preds/llama2/preds_curia_llama2_esp.json')
    except FileNotFoundError:
        print("Predictions file not found.")

    # Check that the two dataframes have the same length
    if len(golds_data) != len(preds_data):
        print("The number of predictions and golds is different.")
        print("Number of golds:", len(golds_data))
        print("Number of predictions:", len(preds_data))

    # Compute Rouge
    golds = golds_data['summary'].tolist()
    texts = golds_data['text'].tolist()
    summaries = preds_data['summary'].tolist()

    gold_rouge = evaluate_rouge(golds, texts, lang='es')
    # pred_rouge = evaluate_rouge(summaries, texts, lang='es')
    
    # print("Pred Rouge:", pred_rouge)
    print("Gold Rouge:", gold_rouge)
    



if __name__ == "__main__":
    main()