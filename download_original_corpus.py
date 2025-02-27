import pandas as pd
from datasets import load_dataset


# Load the original corpus from huggingface.co
corpus_df = load_dataset('VerbACxSS/ItaRegol')['train'].to_pandas()

# Rename the column
corpus_df = corpus_df.rename(columns={"content": "text"})

# Save the original corpus
corpus_df.to_csv(f"./corpora/original.csv", index=False)