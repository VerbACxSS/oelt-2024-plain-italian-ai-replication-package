import requests

readit_session = requests.Session()
readit_session.post('https://www.ilc.cnr.it/dylanlab/apps/texttools/?tt_lang=it', data={'tt_cmd': 'cmd_login', 'tt_login': 'guest', 'tt_pwd': ''})


def readit_start_job(text):
  response = readit_session.post('https://www.ilc.cnr.it/dylanlab/apps/texttools/?tt_lang=it&tt_tmid=tm_source', data={'tt_text': text, 'tt_textlang': 'it', 'tt_settext': 'Avvia l\'analisi del testo...'})
  si = response.text.index('tt_jid=') + 7
  ei = response.text.index('"', si)
  jid = response.text[si:ei]
  return jid


def readit_job_result(jid):
  response = readit_session.post(f'https://www.ilc.cnr.it/dylanlab/apps/texttools/?tt_lang=it&tt_tmid=tm_readability&tt_jid={jid}&tt_re_show1=1&tt_re_show2=1&tt_re_show3=1')

  si = response.text.index('READ-IT Base</td><td bgcolor="#cccccc" valign="middle" align="right">') + 69
  ei = response.text.index('%</td>', si)
  _base = float(response.text[si:ei].replace(',', '.')) / 100.0

  si = response.text.index('READ-IT Lessicale</td><td bgcolor="#dddddd" valign="middle" align="right">') + 74
  ei = response.text.index('%</td>', si)
  _lexical = float(response.text[si:ei].replace(',', '.')) / 100.0

  si = response.text.index('READ-IT Sintattico</td><td bgcolor="#cccccc" valign="middle" align="right">') + 75
  ei = response.text.index('%</td>', si)
  _syntactic = float(response.text[si:ei].replace(',', '.')) / 100.0

  si = response.text.index('READ-IT Globale</td><td bgcolor="#dddddd" valign="middle" align="right">') + 72
  ei = response.text.index('%</td>', si)
  _global = float(response.text[si:ei].replace(',', '.')) / 100.0
  return _base, _lexical, _syntactic, _global