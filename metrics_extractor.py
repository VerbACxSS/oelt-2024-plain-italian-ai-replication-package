import json

from tqdm import tqdm
import pandas as pd

from italian_ats_evaluator import TextAnalyzer, SimplificationAnalyzer

from utils import loaders, readit_utils

original_df, simplified_corpora_dfs = loaders.load_corpora_dfs()

print('Processing original corpus...')
original_metrics = []
original_raw_data = []
original_readit_jobs = json.load(open('corpora_with_metrics/original_readit_jobs.json', 'r', encoding='utf-8'))
for row in tqdm(original_df.to_dict(orient='records')):
  result = TextAnalyzer(row['text'])
  readit_jid = next(j['readit_jid'] for j in original_readit_jobs if j['topic'] == row['topic'] and j['progress'] == row['progress'])
  readit_results = readit_utils.readit_job_result(readit_jid)
  original_metrics.append({
    'region': row['region'],
    'topic': row['topic'],
    'progress': row['progress'],
    'title': row['title'],
    'text': row['text'],
    # Basic
    'n_tokens': result.basic.n_tokens,
    'n_tokens_all': result.basic.n_tokens_all,
    'n_chars': result.basic.n_chars,
    'n_chars_all': result.basic.n_chars_all,
    'n_syllables': result.basic.n_syllables,
    'n_words': result.basic.n_words,
    'n_unique_lemmas': result.basic.n_unique_lemmas,
    'n_sentences': result.basic.n_sentences,
    # Pos
    'n_other': result.pos.n_other,
    'n_nouns': result.pos.n_nouns,
    'n_verbs': result.pos.n_verbs,
    'n_number': result.pos.n_number,
    'n_symbols': result.pos.n_symbols,
    'n_adverbs': result.pos.n_adverbs,
    'n_articles': result.pos.n_articles,
    'n_pronouns': result.pos.n_pronouns,
    'n_particles': result.pos.n_particles,
    'n_adjectives': result.pos.n_adjectives,
    'n_prepositions': result.pos.n_prepositions,
    'n_proper_nouns': result.pos.n_proper_nouns,
    'n_punctuations': result.pos.n_punctuations,
    'n_interjections': result.pos.n_interjections,
    'n_coordinating_conjunctions': result.pos.n_coordinating_conjunctions,
    'n_subordinating_conjunctions': result.pos.n_subordinating_conjunctions,
    # Verbs
    'n_active_verbs': result.verbs.n_active_verbs,
    'n_passive_verbs': result.verbs.n_passive_verbs,
    # Readability
    'ttr': result.readability.ttr,
    'gulpease': result.readability.gulpease,
    'flesch_vacca': result.readability.flesch_vacca,
    'lexical_density': result.readability.lexical_density,
    # VdB
    'n_vdb': result.vdb.n_vdb_tokens,
    'n_vdb_fo': result.vdb.n_vdb_fo_tokens,
    'n_vdb_au': result.vdb.n_vdb_au_tokens,
    'n_vdb_ad': result.vdb.n_vdb_ad_tokens,
    # ReadIT
    'readit_base': readit_results[0],
    'readit_lexical': readit_results[1],
    'readit_syntactic': readit_results[2],
    'readit_global': readit_results[3],
  })
  original_raw_data.append({
      'topic': row['topic'],
      'progress': row['progress'],
      'tokens': result.basic.tokens,
      'lemmas': result.basic.lemmas
  })

print('Saving original metrics...')
pd.DataFrame(original_metrics).to_csv('corpora_with_metrics/original.csv', index=False)
json.dump(original_raw_data, open('corpora_with_metrics/original.json', 'w', encoding='utf-8'))


simplified_metrics = {CORPUS_NAME:[] for CORPUS_NAME in simplified_corpora_dfs.keys()}
simplified_raw_data = {CORPUS_NAME:[] for CORPUS_NAME in simplified_corpora_dfs.keys()}
for CORPUS_NAME, simplified_corpus_df in simplified_corpora_dfs.items():
  print('Processing', CORPUS_NAME, 'corpus...')
  simplified_readit_jobs = json.load(open(f'corpora_with_metrics/{CORPUS_NAME}_readit_jobs.json', 'r', encoding='utf-8'))
  
  for row in tqdm(simplified_corpus_df.to_dict(orient='records')):
    result = SimplificationAnalyzer(row['text'], row['simplified_text'])
    readit_jid = next(j['readit_jid'] for j in simplified_readit_jobs if j['topic'] == row['topic'] and j['progress'] == row['progress'])
    readit_results = readit_utils.readit_job_result(readit_jid)
    simplified_metrics[CORPUS_NAME].append({
      'region': row['region'],
      'topic': row['topic'],
      'progress': row['progress'],
      'title': row['title'],
      'text': row['text'],
      'simplified_text': row['simplified_text'],
      # Basic
      'n_tokens': result.simplified.basic.n_tokens,
      'n_tokens_all': result.simplified.basic.n_tokens_all,
      'n_chars': result.simplified.basic.n_chars,
      'n_chars_all': result.simplified.basic.n_chars_all,
      'n_syllables': result.simplified.basic.n_syllables,
      'n_words': result.simplified.basic.n_words,
      'n_unique_lemmas': result.simplified.basic.n_unique_lemmas,
      'n_sentences': result.simplified.basic.n_sentences,
      # Pos
      'n_other': result.simplified.pos.n_other,
      'n_nouns': result.simplified.pos.n_nouns,
      'n_verbs': result.simplified.pos.n_verbs,
      'n_number': result.simplified.pos.n_number,
      'n_symbols': result.simplified.pos.n_symbols,
      'n_adverbs': result.simplified.pos.n_adverbs,
      'n_articles': result.simplified.pos.n_articles,
      'n_pronouns': result.simplified.pos.n_pronouns,
      'n_particles': result.simplified.pos.n_particles,
      'n_adjectives': result.simplified.pos.n_adjectives,
      'n_prepositions': result.simplified.pos.n_prepositions,
      'n_proper_nouns': result.simplified.pos.n_proper_nouns,
      'n_punctuations': result.simplified.pos.n_punctuations,
      'n_interjections': result.simplified.pos.n_interjections,
      'n_coordinating_conjunctions': result.simplified.pos.n_coordinating_conjunctions,
      'n_subordinating_conjunctions': result.simplified.pos.n_subordinating_conjunctions,
      # Verbs
      'n_active_verbs': result.simplified.verbs.n_active_verbs,
      'n_passive_verbs': result.simplified.verbs.n_passive_verbs,
      # Readability
      'ttr': result.simplified.readability.ttr,
      'gulpease': result.simplified.readability.gulpease,
      'flesch_vacca': result.simplified.readability.flesch_vacca,
      'lexical_density': result.simplified.readability.lexical_density,
      # VdB
      'n_vdb': result.simplified.vdb.n_vdb_tokens,
      'n_vdb_fo': result.simplified.vdb.n_vdb_fo_tokens,
      'n_vdb_au': result.simplified.vdb.n_vdb_au_tokens,
      'n_vdb_ad': result.simplified.vdb.n_vdb_ad_tokens,
      # Similariy
      'semantic_similarity': result.similarity.semantic_similarity,
      # Diff
      'editdistance': result.diff.editdistance,
      'n_added_tokens': result.diff.n_added_tokens,
      'n_deleted_tokens': result.diff.n_deleted_tokens,
      'n_added_vdb_tokens': result.diff.n_added_vdb_tokens,
      'n_deleted_vdb_tokens': result.diff.n_deleted_vdb_tokens,
      # ReadIT
      'readit_base': readit_results[0],
      'readit_lexical': readit_results[1],
      'readit_syntactic': readit_results[2],
      'readit_global': readit_results[3],
    })
    simplified_raw_data[CORPUS_NAME].append({
      'topic': row['topic'],
      'progress': row['progress'],
      'tokens': result.simplified.basic.tokens,
      'lemmas': result.simplified.basic.lemmas
    })

for CORPUS_NAME in simplified_corpora_dfs.keys():
  print('Saving', CORPUS_NAME, 'metrics...')
  pd.DataFrame(simplified_metrics[CORPUS_NAME]).to_csv(f'corpora_with_metrics/{CORPUS_NAME}.csv', index=False)
  json.dump(simplified_raw_data[CORPUS_NAME], open(f'corpora_with_metrics/{CORPUS_NAME}.json', 'w', encoding='utf-8'))
