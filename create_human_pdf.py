from xhtml2pdf import pisa
import pandas as pd

def space(n):
    return "&nbsp;" * n


def parse_stylo_metrics(data):
    return f"""
        <b>Tokens</b>:{data['n_tokens']}{space(4)}<b>Types</b>:{data['n_words']}{space(4)}<b>Caratteri</b>:{data['n_chars']}{space(4)}<b>Frasi</b>:{data['n_sentences']}{space(4)}</br>
        <b>Nomi</b>:{data[f'n_nouns']}{space(4)}<b>Avverbi</b>:{data[f'n_adverbs']}{space(4)}<b>Pronomi</b>:{data[f'n_pronouns']}{space(4)}<b>Articoli</b>:{data[f'n_articles']}{space(4)}<b>Aggettivi</b>:{data[f'n_adjectives']}<br/>
        <b>Verbi</b>:{data['n_verbs']}{space(4)}<b>Verbi attivi</b>:{data['n_active_verbs']}{space(4)}<b>Verbi passivi</b>:{data['n_passive_verbs']}
    """


def parse_readability_metrics(data):
    return f"""
        <b>Passivi</b>:{round(data['n_passive_verbs'] / data['n_verbs'] * 100, 2)}{space(4)}<b>VdB</b>: {round(data['n_vdb'] / data['n_tokens'] * 100, 2)}%<br/>
        <b>Gulpease</b>: {round(data['gulpease'], 2)}{space(4)}<b>Flesch Vacca</b>: {round(data['flesch_vacca'], 2)}<br/>
        <b>readit_base</b>: {round(data['gulpease'], 2)}{space(4)}<b>readit_lexical</b>: {round(data['readit_lexical'], 2)}{space(4)}<b>readit_syntactic</b>: {round(data['readit_syntactic'], 2)}{space(4)}<b>readit_global</b>: {round(data['readit_global'], 2)}<br/>
    """


def parse_diff_metrics(data):
    return f"""
        <b>Similarity</b>: {round(data['semantic_similarity'], 2)} %{space(4)}<b>Edit Distance</b>: {data['editdistance']} ({round(data['editdistance'] / data['n_chars'] * 100, 2)}%)<br/>
        <b>Added Tokens</b>: {round(data['n_added_tokens'], 2)}{space(4)}<b>Added VdB Tokens</b>: {data['n_added_vdb_tokens']}<br/>
        <b>Deleted Tokens</b>: {data['n_deleted_tokens']}{space(4)}<b>Deleted Not VdB Tokens</b>: {data['n_deleted_vdb_tokens']}
    """


def html_template(original_articles, basic_articles, chain_articles):
    html = """
    <html>
    <head>
        <title>PDF</title>
        <style>
            @page {
                size: a4 landscape;
                margin-left: 0.35cm;
                margin-right: 0.35cm;
                margin-top: 0.25cm;
                margin-bottom: 0.25cm;
            }
            .page-content {
                width: 29cm;
                height: 20.5cm;
            }
            h1 {
                width: 29cm;
                height: 0.35cm;
                margin: 0cm;
                padding 0cm;
                line-height: 1;
                font-size: 10px;
                text-align: center;
            }
            table {
                width: 29cm;
                height: 20cm;
            }
            td, th {
                margin: 0;
                border: 0;
                padding-top: 0;
                padding-bottom: 0;
                padding-left: 0.1cm;
                padding-right: 0.1cm;
            }
            tr {
                margin: 0;
                border: 0;
                padding: 0;
            }
            .text-th {
                text-align: center;
                width: 9.65cm;
                height: 0.35cm;
                line-height: 1;
                font-size: 10px;
                vertical-align: middle;
            }
            .text-td {
                text-align: justify;
                width: 9.65cm;
                height: 15.8cm;
                line-height: 1.2;
                font-size: 9px;
                vertical-align: top;
            }
            .stylo-td {
                text-align: left;
                width: 9.65cm;
                height: 1.5cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
            .readability-td {
                text-align: left;
                width: 9.6cm;
                height: 1.5cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
            .diff-td {
                text-align: left;
                width: 9.6cm;
                height: 1cm;
                vertical-align: top;
                font-size: 8px;
                line-height: 1.1;
            }
        </style>
    </head>
    """

    html += "<body>"

    for i in range(len(original_articles)):
        original_article = original_articles[i]
        basic_article = basic_articles[i]
        chain_article = chain_articles[i]

        original_article['text'] = original_article['text'].replace('\n\r', '<br>').replace('\n', '<br>')
        basic_article['text'] = basic_article['text'].replace('\n\r', '<br>').replace('\n', '<br>')
        chain_article['text'] = chain_article['text'].replace('\n\r', '<br>').replace('\n', '<br>')

        html += f"""
        <div class="page-content">
            <h1>{original_article['title']}</h1>
            <table>
                <tr>
                    <th class="text-th">Original</th>
                    <th class="text-th">Basic</th>
                    <th class="text-th">Chain</th>
                </tr>
                <tr>
                    <td class="text-td">{original_article['text']}</td>
                    <td class="text-td">{basic_article['text']}</td>
                    <td class="text-td">{chain_article['text']}</td>
                </tr>
                <tr>
                    <td class="stylo-td">{parse_stylo_metrics(original_article)}</td>
                    <td class="stylo-td">{parse_stylo_metrics(basic_article)}</td>
                    <td class="stylo-td">{parse_stylo_metrics(chain_article)}</td>
                </tr>
                <tr>
                    <td class="readability-td">{parse_readability_metrics(original_article)}</td>
                    <td class="readability-td">{parse_readability_metrics(basic_article)}</td>
                    <td class="readability-td">{parse_readability_metrics(chain_article)}</td>
                </tr>
                <tr>
                    <td class="diff-td"></td>
                    <td class="diff-td">{parse_diff_metrics(basic_article)}</td>
                    <td class="diff-td">{parse_diff_metrics(chain_article)}</td>
                </tr>
            </table>
        </div>
        """
    html += "</body>"
    html += "</html>"
    return html


if __name__ == "__main__":
    original_corpus = pd.read_csv('corpora_with_metrics/original.csv')

    ## Process gpt-4o-mini
    basic_corpus = pd.read_csv('corpora_with_metrics/mini_basic.csv')
    chain_corpus = pd.read_csv('corpora_with_metrics/mini_chain6.csv')

    basic_corpus = basic_corpus.drop(columns=['text']).rename(columns={'simplified_text': 'text'})
    chain_corpus = chain_corpus.drop(columns=['text']).rename(columns={'simplified_text': 'text'})

    for topic in original_corpus['topic'].unique():
        original_articles = original_corpus[original_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')
        basic_articles = basic_corpus[basic_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')
        chain_articles = chain_corpus[chain_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')

        html = html_template(original_articles, basic_articles, chain_articles)
        with open(f'human_pdf/gpt-4o-mini/{topic[0:60]}.pdf', 'w+b') as f:
            pisa.CreatePDF(html, dest=f)

    ## Process gpt-4o
    basic_corpus = pd.read_csv('corpora_with_metrics/basic.csv')
    chain_corpus = pd.read_csv('corpora_with_metrics/chain6.csv')

    basic_corpus = basic_corpus.drop(columns=['text']).rename(columns={'simplified_text': 'text'})
    chain_corpus = chain_corpus.drop(columns=['text']).rename(columns={'simplified_text': 'text'})

    for topic in original_corpus['topic'].unique():
        original_articles = original_corpus[original_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')
        basic_articles = basic_corpus[basic_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')
        chain_articles = chain_corpus[chain_corpus['topic'] == topic].sort_values(by='progress').to_dict(orient='records')

        html = html_template(original_articles, basic_articles, chain_articles)
        with open(f'human_pdf/gpt-4o/{topic[0:60]}.pdf', 'w+b') as f:
            pisa.CreatePDF(html, dest=f)
