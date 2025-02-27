import pandas as pd

from utils.ZeroShotSimplifier import ZeroShotSimplifier
from utils.FewShotSimplifier import FewShotSimplifier
from utils import loaders

if __name__ == "__main__":
    # Load the original corpus
    corpus_df = pd.read_csv("./corpora/original.csv")

    ### BASIC SIMPLIFIER ###
    basic_simplifier = ZeroShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('basic'))
    
    basic_corpus_df = corpus_df.copy()
    basic_corpus_df['simplified_text'] = basic_corpus_df['text'].apply(basic_simplifier.simplify)
    basic_corpus_df.to_csv(f"./corpora/basic.csv", index=False)


    ## MINI BASIC SIMPLIFIER ##
    mini_basic_simplifier = ZeroShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('basic'))

    mini_basic_corpus_df = corpus_df.copy()
    mini_basic_corpus_df['simplified_text'] = mini_basic_corpus_df['text'].apply(mini_basic_simplifier.simplify)
    mini_basic_corpus_df.to_csv(f"./corpora/mini_basic.csv", index=False)
    

    ### MINI CHAIN SIMPLIFIER ###
    mini_corrector = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('corrector'), loaders.load_examples('corrector', k=8))
    mini_connectives = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('connectives'), loaders.load_examples('connectives', k=8))
    mini_expressions = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('expressions'), loaders.load_examples('expressions', k=8))
    mini_sentence_splitter = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('sentence_splitter'), loaders.load_examples('sentence_splitter', k=8))
    mini_sentence_reorganizer = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('sentence_reorganizer'), loaders.load_examples('sentence_reorganizer', k=8))
    mini_verbs = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('verbs'), loaders.load_examples('verbs', k=8))
    mini_nominalizations = FewShotSimplifier('gpt-4o-mini-2024-07-18', loaders.load_prompt('nominalizations'), loaders.load_examples('nominalizations', k=8))

    mini_chain_corpus_df = corpus_df.copy()
    mini_chain_corpus_df['corrected_text'] = mini_chain_corpus_df['text'].apply(mini_corrector.simplify)
    mini_chain_corpus_df['simplified_connectives_text'] = mini_chain_corpus_df['corrected_text'].apply(mini_connectives.simplify)
    mini_chain_corpus_df['simplified_expressions_text'] = mini_chain_corpus_df['simplified_connectives_text'].apply(mini_expressions.simplify)
    mini_chain_corpus_df['simplified_sentence_splitter_text'] = mini_chain_corpus_df['simplified_expressions_text'].apply(mini_sentence_splitter.simplify)
    mini_chain_corpus_df['simplified_sentence_reorganizer_text'] = mini_chain_corpus_df['simplified_sentence_splitter_text'].apply(mini_sentence_reorganizer.simplify)
    mini_chain_corpus_df['simplified_verbs_text'] = mini_chain_corpus_df['simplified_sentence_reorganizer_text'].apply(mini_verbs.simplify)
    mini_chain_corpus_df['simplified_nominalizations_text'] = mini_chain_corpus_df['simplified_verbs_text'].apply(mini_nominalizations.simplify)
    mini_chain_corpus_df.to_csv(f"./corpora/mini_chain.csv", index=False)


    ### CHAIN SIMPLIFIER ###
    corrector = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('corrector'), loaders.load_examples('corrector', k=8))
    connectives = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('connectives'), loaders.load_examples('connectives', k=8))
    expressions = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('expressions'), loaders.load_examples('expressions', k=8))
    sentence_splitter = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('sentence_splitter'), loaders.load_examples('sentence_splitter', k=8))
    sentence_reorganizer = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('sentence_reorganizer'), loaders.load_examples('sentence_reorganizer', k=8))
    verbs = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('verbs'), loaders.load_examples('verbs', k=8))
    nominalizations = FewShotSimplifier('gpt-4o-2024-11-20', loaders.load_prompt('nominalizations'), loaders.load_examples('nominalizations', k=8))

    chain_corpus_df = corpus_df.copy()
    chain_corpus_df['corrected_text'] = chain_corpus_df['text'].apply(corrector.simplify)
    chain_corpus_df['simplified_connectives_text'] = chain_corpus_df['corrected_text'].apply(connectives.simplify)
    chain_corpus_df['simplified_expressions_text'] = chain_corpus_df['simplified_connectives_text'].apply(expressions.simplify)
    chain_corpus_df['simplified_sentence_splitter_text'] = chain_corpus_df['simplified_expressions_text'].apply(sentence_splitter.simplify)
    chain_corpus_df['simplified_sentence_reorganizer_text'] = chain_corpus_df['simplified_sentence_splitter_text'].apply(sentence_reorganizer.simplify)
    chain_corpus_df['simplified_verbs_text'] = chain_corpus_df['simplified_sentence_reorganizer_text'].apply(verbs.simplify)
    chain_corpus_df['simplified_nominalizations_text'] = chain_corpus_df['simplified_verbs_text'].apply(nominalizations.simplify)
    chain_corpus_df.to_csv(f"./corpora/chain.csv", index=False)
