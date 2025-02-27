# Simple Italian and AI: strenghts and weaknesses
Giuliana Fiorentino, Vittorio Ganfi, Marco Russodivito, Alessandro Cioffi and Maria Ausilia Simonelli

## Abstract
The simplification of language - in particular with reference to administrative language - is a topic that has been addressed in Italian linguistics for several decades and that has achieved some important results (consolidated and shared lists of linguistic factors - morphosyntactic and lexical - that affect the simplicity and accessibility of a text; for a summary see Fiorentino, Ganfi 2024), which have allowed the definition of a readability index (Gulpease) as early as the 1980s (Lucisano, Piemontese 1988).

The authors (a research group) are currently realising - with the support of a large language model LLM - an application for the automatic simplification of administrative texts called SEMPL-IT (Fiorentino, Russodivito, in press; Ganfi, Russodivito in press). To develop this objective, ItaIst was set up, a corpus of 208 administrative texts from 8 Italian regions (Basilicata, Calabria, Campania, Latium, Lombardy, Molise, Tuscany, Veneto) and referring to 3 thematic areas: waste, health, public services. For each thematic area, 2 types of texts were considered (service charters and calls for tenders for the first thematic area; general planning acts and accreditations for the second thematic area; service charters and rationalisation of public participations for the third thematic area). 

The corpus was then automatically simplified to create a simplified parallel corpus that was compared with the source corpus. The simplified parallel corpus was then evaluated from the point of view of increased readability and semantic similarity to the source text in order to validate the automatic simplification work.

In this contribution, we intend to apply the same automatic simplification model to another corpus - called Norme - of texts different from those used in the previous studies in order to compare the simplification results with those already obtained. The corpus Norme is smaller in size than ItaIst and consists of rules and regulations. This corpus takes into account legally relevant acts with legal effects, which create, modify or extinguish subjective legal situations. These texts are particularly complex and for which simplification must ensure that the process of linguistic manipulation does not affect the legal effect.

In sum, in this contribution we will discuss the simplification parameters used, the quality of the simplified text, and draw conclusions on the different impact of the various parameters in increasing the readability of an administrative and/or regulatory text.

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