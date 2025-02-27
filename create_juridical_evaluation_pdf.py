from xhtml2pdf import pisa
import pandas as pd


def html_template(_articles):
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
                height: 0.5cm;
                margin: 0cm;
                padding 0cm;
                line-height: 1;
                font-size: 10px;
                text-align: center;
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
            .text-table {
                width: 29cm;
                height: 15cm;
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
                height: 14.5cm;
                line-height: 1.2;
                font-size: 9px;
                vertical-align: top;
            }
            .task-table {
                width: 29cm;
                height: 5cm;
            }
            .task-th {
                text-align: center;
                width: 14.5cm;
                height: 0.5cm;
                line-height: 1;
                font-size: 12px;
                vertical-align: middle;
            }
            .task-td {
                text-align: center;
                width: 14.5cm;
                height: 4.8cm;
                line-height: 1.2;
                font-size: 10px;
                vertical-align: top;
            }
        </style>
    </head>
    """

    html += "<body>"

    for _article in _articles:
        _article['original_text'] = _article['original_text'].replace('\n\r', '<br>').replace('\n', '<br>')
        _article['basic_simplified_text'] = _article['basic_simplified_text'].replace('\n\r', '<br>').replace('\n', '<br>')
        _article['chained_simplified_text'] = _article['chained_simplified_text'].replace('\n\r', '<br>').replace('\n', '<br>')

        _basic_task = [task for task in _article['tasks'] if task['variant'] == 'BASIC'][0]
        _chain_task = [task for task in _article['tasks'] if task['variant'] == 'CHAIN'][0]

        html += f"""
        <div class="page-content">
            <h1>{_article['article_title']}</h1>
            <table class='text-table'>
                <tr>
                    <th class="text-th">Original</th>
                    <th class="text-th">Basic</th>
                    <th class="text-th">Chain</th>
                </tr>
                <tr>
                    <td class="text-td">{_article['original_text']}</td>
                    <td class="text-td">{_article['basic_simplified_text']}</td>
                    <td class="text-td">{_article['chained_simplified_text']}</td>
                </tr>
            </table>
            <table class='task-table'>
                <tr>
                    <th class="task-th">BASIC REVIEW</th>
                    <th class="task-th">CHAIN REVIEW</th>
                </tr>
                <tr>
                    <td class="task-td">
                        <b>Reviewer:</b> {_basic_task['reviewer']}<br>
                        <b>Time:</b> {_basic_task['elapsed_time']}<br>
                        <b>juridically_equivalent:</b> {_basic_task['juridically_equivalent']}<br>
                        <b>preference:</b> {_basic_task['preference']}<br>
                        <b>original_text_comment:</b> <br>
                        {_basic_task['original_text_comment']}<br>
                        <b>simplified_text_comment:</b> <br>
                        {_basic_task['simplified_text_comment']}<br>
                    </td>
                    <td class="task-td">
                        <b>Reviewer:</b> {_chain_task['reviewer']}<br>
                        <b>Time:</b> {_chain_task['elapsed_time']}<br>
                        <b>juridically_equivalent:</b> {_chain_task['juridically_equivalent']}<br>
                        <b>preference:</b> {_chain_task['preference']}<br>
                        <b>original_text_comment:</b> <br>
                        {_chain_task['original_text_comment']}<br>
                        <b>simplified_text_comment:</b> <br>
                        {_chain_task['simplified_text_comment']}<br>
                    </td>
                </tr>
            </table>
        </div>
        """
    html += "</body>"
    html += "</html>"
    return html


if __name__ == "__main__":
    articles = pd.read_csv('juridical_evaluation_results/articles.csv')
    tasks = pd.read_csv('juridical_evaluation_results/task.csv')

    print(articles.columns)

    for topic in articles['document_title'].unique():
        topic_articles = articles[articles['document_title'] == topic].sort_values(by='id').to_dict(orient='records')
        for topic_article in topic_articles:
            topic_article['tasks'] = tasks[tasks['article_id'] == topic_article['id']].to_dict(orient='records')
            print(topic_article)

        with open(f'juridical_evaluation_pdf/{topic[0:60]}.pdf', 'w+b') as f:
            pisa.CreatePDF(html_template(topic_articles), dest=f)

