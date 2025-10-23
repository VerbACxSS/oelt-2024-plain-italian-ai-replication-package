# Plain Italian and AI: strenghts and weaknesses
Giuliana Fiorentino, Vittorio Ganfi, Marco Russodivito, Alessandro Cioffi and Maria Ausilia Simonelli


## Abstract
The simplification of language – particularly with regard to administrative discourse – has long been a central concern within Italian linguistics. Over the past few decades, significant progress has been made, including the development of consolidated and widely accepted lists of linguistic features – both morphosyntactic and lexical – that influence textual simplicity and accessibility (cf. Fiorentino/Ganfi 2024). These advances contributed to the early creation of a readability index, the *Gulpease index*, in the 1980s (cf. Lucisano/Piemontese 1988). Within this framework, the authors have developed a software for the automatic simplification of administrative texts, supported by a large language model (LLM), entitled *SEMPL-IT* (cf. Russodivito et al. 2024; Fiorentino/Russodivito 2025; Ganfi/Russodivito 2025; Fiorentino et al. in press; Fiorentino/Russodivito in press). As part of this project, a corpus named *ItaIst* (Fiorentino et al. 2024b) was compiled and subjected to automatic simplification using the *BASIC approach*, resulting in a parallel corpus of simplified texts. This simplified corpus was then compared to the source corpus and evaluated in terms of improved readability and *Semantic similarity* (cf. Chandrasekaran et al. 2021), with the objective of validating the effectiveness of the simplification process. In this contribution, we introduce and validate a new methodology – the *CHAIN approach* – applied to a different corpus, *ItaRegol* (Fiorentino et al. 2024a). Although smaller in size than *ItaIst*, *ItaRegol* comprises rules and regulations, i.e., legally binding texts that create, modify, or extinguish subjective legal positions. Due to the legal nature of these texts, simplification must be carried out with caution to avoid altering their legal effects. This paper compares the two simplification approaches – *BASIC* and *CHAIN* – by evaluating the parameters adopted, assessing the quality of the simplified output, and drawing conclusions regarding the differing impact of these strategies in enhancing the readability of administrative versus regulatory texts.


## Setup
Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Create a `.env` file
```bash
OPENAI_API_KEY=sk-...
```


## Replication Package Content
- `corpora`: folder that contains the `original`, `basic`, `chain`, `mini_basic` and `mini_chain` corpora in .csv format.
- `corpora_with_metrics`: folder that contains the corpora with the metrics extracted in `.csv` and `.json` format.
- `prompt`: folder that contains the prompts in `.md` format to simply the `original` corpus:
  - `basic.md`: a comprehensive prompt to simplify document in zero-shot mode.
  - `corrector.md`: correct grammar, spelling, and punctuation errors.
  - `connectives.md`: replace bureaucratic and formal with simpler alternatives.
  - `expressions.md`: transform bureaucratic and formal expressions into plain language.
  - `sentence_splitter.md`: divide long sentences into shorter.
  - `sentence_reorganizer.md`: adjusts sentence structure to follow a clear subject-verb-object (SVO) order and explicitly stating the subject.
  - `verbs.md`: convert passive voice into active voice and replace indefinite verb forms with finite ones.
  - `nominalizations.md`: replaces noun-based expressions with their verb counterparts.
- `examples`: folder that contains a `.csv` file for each simplification rules, with each file consisting of 13 manual simplification intended for use as few-shot samples.
- `corpus_simplifier.py` and `utils`: the code employed to automatically simplify the ItaRegol corpus. It requires `OPEN_AI_KEY` variable.
- `exec_readit.py`: script to launch read-it jobs (must be executed before `metrics_extractor.py`).
- `metrics_extractor.py`: script to extract metrics from each parallel corpus. It employs [italian-ats-evaluator](https://github.com/RedHitMark/italian-ats-evaluator).
- `metrics_overview.ipynb`: jupyter notebook used to summarize the metrics on parallel corpora.
- `metrics_statistical_analysis.ipynb`: jupyter notebook used to perform the statistical analysis described in the paper.
- `create_human_pdfs.py` and `human_pdf`: script used to create human-readable `.pdf` for each simplified corpus.
- `juridical_evaluation_results`: folder that contains the results of juridical evaluation. 
- `juridical_evaluation_analysis.ipynb`: jupyter notebook used to explore the results of the juridical evaluation.
- `create_juridical_evaluation_pdfs.py` and `juridical_evaluation_pdf`: script used to create human-readable `.pdf` of the juridical evaluation.


## Acknowledgements
This contribution is a result of the research conducted within the framework of the PRIN 2020 (Progetti di Rilevante Interesse Nazionale) "VerbACxSS: on analytic verbs, complexity, synthetic verbs, and simplification. For accessibility" (Prot. 2020BJKB9M), funded by the Italian Ministero dell'Università e della Ricerca.