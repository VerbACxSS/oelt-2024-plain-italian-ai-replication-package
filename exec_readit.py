import json
from tqdm import tqdm

from utils import readit_utils
from utils import loaders

original_corpus_df, simplified_corpora_dfs = loaders.load_corpora_dfs()

print('Starting original readit jobs...')
original_readit_jobs = []
for row in tqdm(original_corpus_df.to_dict(orient='records')):
  original_readit_jobs.append({
    'topic': row['topic'],
    'progress': row['progress'],
    'readit_jid': readit_utils.readit_start_job(row['text'])
  })

print('Saving original readit jobs...')
with open('corpora_with_metrics/original_readit_jobs.json', 'w') as f:
  json.dump(original_readit_jobs, f)

for CORPUS_NAME, corpus_df in simplified_corpora_dfs.items():
    print(f'Starting {CORPUS_NAME} readit jobs...')
    simplified_readit_jobs = []
    for row in tqdm(corpus_df.to_dict(orient='records')):
      simplified_readit_jobs.append({
        'topic': row['topic'],
        'progress': row['progress'],
        'readit_jid': readit_utils.readit_start_job(row['simplified_text'])
      })
    
    print(f'Saving {CORPUS_NAME} readit jobs...')
    with open(f'corpora_with_metrics/{CORPUS_NAME}_readit_jobs.json', 'w') as f:
      json.dump(simplified_readit_jobs, f)
