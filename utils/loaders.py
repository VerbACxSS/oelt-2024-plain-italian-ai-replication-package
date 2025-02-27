import json
import os
from random import sample
from typing import List, Tuple
import editdistance

import pandas as pd


def load_corpora_dfs():
  print('Loading corpora...')

  chain_cols = ['corrected_text', 'simplified_connectives_text', 'simplified_expressions_text', 'simplified_sentence_splitter_text', 'simplified_sentence_reorganizer_text', 'simplified_verbs_text', 'simplified_nominalizations_text']

  original_df = pd.read_csv('corpora/original.csv', encoding='utf-8').sort_values(by=['topic', 'progress'])

  # gpt-4o-mini basic corpus
  mini_basic_df = pd.read_csv('corpora/mini_basic.csv', encoding='utf-8').sort_values(by=['topic', 'progress'])

  # gpt-4o-mini chain corpus
  mini_chain_df = pd.read_csv('corpora/mini_chain.csv', encoding='utf-8').sort_values(by=['topic', 'progress'])

  mini_chain0_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[0]])
  mini_chain0_df = mini_chain0_df.rename(columns={chain_cols[0]: 'simplified_text'})

  mini_chain1_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[1]])
  mini_chain1_df = mini_chain1_df.rename(columns={chain_cols[1]: 'simplified_text'})

  mini_chain2_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[2]])
  mini_chain2_df = mini_chain2_df.rename(columns={chain_cols[2]: 'simplified_text'})

  mini_chain3_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[3]])
  mini_chain3_df = mini_chain3_df.rename(columns={chain_cols[3]: 'simplified_text'})

  mini_chain4_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[4]])
  mini_chain4_df = mini_chain4_df.rename(columns={chain_cols[4]: 'simplified_text'})

  mini_chain5_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[5]])
  mini_chain5_df = mini_chain5_df.rename(columns={chain_cols[5]: 'simplified_text'})

  mini_chain6_df = mini_chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[6]])
  mini_chain6_df = mini_chain6_df.rename(columns={chain_cols[6]: 'simplified_text'})

  # gpt-4o basic corpus
  basic_df = pd.read_csv('corpora/basic.csv', encoding='utf-8').sort_values(by=['topic', 'progress'])

  # gpt-4o chain corpus
  chain_df = pd.read_csv('corpora/chain.csv', encoding='utf-8').sort_values(by=['topic', 'progress'])

  chain0_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[0]])
  chain0_df = chain0_df.rename(columns={chain_cols[0]: 'simplified_text'})

  chain1_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[1]])
  chain1_df = chain1_df.rename(columns={chain_cols[1]: 'simplified_text'})

  chain2_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[2]])
  chain2_df = chain2_df.rename(columns={chain_cols[2]: 'simplified_text'})

  chain3_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[3]])
  chain3_df = chain3_df.rename(columns={chain_cols[3]: 'simplified_text'})

  chain4_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[4]])
  chain4_df = chain4_df.rename(columns={chain_cols[4]: 'simplified_text'})

  chain5_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[5]])
  chain5_df = chain5_df.rename(columns={chain_cols[5]: 'simplified_text'})

  chain6_df = chain_df.drop(columns=[e for e in chain_cols if e != chain_cols[6]])
  chain6_df = chain6_df.rename(columns={chain_cols[6]: 'simplified_text'})


  simplified_corpora_dfs = {
    'mini_basic': mini_basic_df,
    'mini_chain0': mini_chain0_df,
    'mini_chain1': mini_chain1_df,
    'mini_chain2': mini_chain2_df,
    'mini_chain3': mini_chain3_df,
    'mini_chain4': mini_chain4_df,
    'mini_chain5': mini_chain5_df,
    'mini_chain6': mini_chain6_df,
    'basic': basic_df,
    'chain0': chain0_df,
    'chain1': chain1_df,
    'chain2': chain2_df,
    'chain3': chain3_df,
    'chain4': chain4_df,
    'chain5': chain5_df,
    'chain6': chain6_df
  }
  
  return original_df, simplified_corpora_dfs

def load_metrics_dfs():
  print('Loading metrics...')
  dfs_maps = dict()
  jsons_maps = dict()
  for name in ['original', \
               'basic', 'mini_basic', \
               'mini_chain0', 'mini_chain1', 'mini_chain2', 'mini_chain3', 'mini_chain4', 'mini_chain5', 'mini_chain6', \
               'chain0', 'chain1', 'chain2', 'chain3', 'chain4', 'chain5', 'chain6']:
    tmp_df = pd.read_csv(f'corpora_with_metrics/{name}.csv', encoding='utf-8')
    tmp_df = tmp_df.sort_values(by=['topic', 'progress'])

    tmp_json = json.load(open(f'corpora_with_metrics/{name}.json', 'r', encoding='utf-8'))

    dfs_maps[name] = tmp_df
    jsons_maps[name] = tmp_json
  return dfs_maps, jsons_maps

def read_file(file_path: str) -> str:
  with open(file_path, 'r', encoding='utf-8') as f:
    return f.read()

def load_prompt(name: str) -> str:
  return read_file(f'prompts/{name}.md')

def load_examples(name: str, k: int = 5) -> List[Tuple[str, str]]:
  examples_df = pd.read_csv(f'./examples/{name}.csv')

  examples = []
  for row in examples_df.to_records():
    examples.append((row['input'], row['output']))

  examples = sample(examples, k)
  examples = sorted(examples, key=lambda x: editdistance.eval(x[0], x[1]))
  
  return examples