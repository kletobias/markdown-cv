# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# # !pip install ipyparallel
# # !pip install markdown2
# # !pip install spacy
# # !python -m spacy download en_core_web_sm
# !ipcluster start -n 9

# %%
from ipyparallel import Client
rc = Client()
rc.ids
# %px
import os
print(f"Process: {os.getpid():d}.")
import itertools
import re
from markdown2 import Markdown
import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm

# %%
nlp = en_core_web_sm.load()


# %%
dir='/Users/tobias/all_code/projects/portfolio-website-2022/_projects/'
files = os.listdir(dir)
host = 'https://deep-learning-mastery.com/projects/'
# for f in files:
#     print(f)
#     print(f'is .md: {f[-3:] == ".md"}')

# %%
def cl(files,host):
    md_files = []
    link = {}
    for f in files:
        if f[-3:] == '.md':
            md_files.append(f[:-3])
            link[f[:-3]] = host + f'{f[:-3]}' + '/'
        else:
            continue
    linkf = []
    for k,v in link.items():
        linkf.append(f'[{k}]({v})')


    return linkf

# %%
mdf = cl(files,host)
print(mdf)

# %%
# %px
def get_title_description(dir,files):
    patt = re.compile('^title:\s[\'\"](.+)[\'\"]$',re.IGNORECASE)
    patd = re.compile('^description:\s[\'\"](.+)[\'\"]$',re.IGNORECASE)
    patc = re.compile('^category:\s\[[\'\"](.+)[\'\"]\]$',re.IGNORECASE)
    patta = re.compile('^tags:\s(\[.+\])$',re.IGNORECASE)
    patsub = re.compile('<br>')
    pat_html = re.compile(r'<[^>]+>|\\n',re.MULTILINE)
    md_files = []
    cv_text_all = []
    td = {}
    link = {}
    linkf = []
    for f in files:
        if f[-3:] == '.md':
            td[f[:-3]] = {}
            md_files.append(f[:-3])
            td[f[:-3]]['url'] = f'[Full Article]({host}{f[:-3]}/)'
            with open(os.path.join(dir,f),'r') as a:
                article = a.readlines()
                doc = nlp(pat_html.sub('',str(article)))
                words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
                td[f[:-3]]['word_count'] = len(words)
            with open(os.path.join(dir,f),'r') as ff:
                for line in itertools.islice(ff,2,8):
                    ttl = patt.search(line)
                    ddl = patd.search(line)
                    ccl = patc.search(line)
                    tal = patta.search(line)
                    if ttl != None:
                        ttls = patsub.sub(' ',ttl[1])
                        td[f[:-3]]["title"] = ttls
                    elif ddl != None:
                        ddls = patsub.sub(' ',ddl[1])
                        td[f[:-3]]["description"] = ddls
                    elif ccl != None:
                        ccls = patsub.sub(' ',ccl[1])
                        td[f[:-3]]["category"] = ccls
                    elif tal != None:
                        tals = patsub.sub(' ',tal[1])
                        td[f[:-3]]["tags"] = tals
                    else:
                        continue
    for k,v in link.items():
        linkf.append(f'[{k}]({v})')
    for k in sorted(td.keys()):
        print(td[k].items())
        cv_text = f'\
<br>\
<H4>{td[k]["title"]}</H4>\
**Description:** {td[k]["description"]}\
<br>\
                **Tags:**  {td[k]["tags"]}<br>\
                **Category:** *{td[k]["category"]}* | **Word Count:**\
                {td[k]["word_count"]} | **{td[k]["url"]}**<br>\
                <br><br>'
        md = Markdown()
#        print(f'CONVERTED: {md.convert(cv_text)}')
        cv_text_all.append(md.convert(cv_text))

    with open('cv_articles.md','w+') as f:
        for item in cv_text_all:
            f.write(item)
    return cv_text_all

# %%
td = get_title_description(dir,files)
for item in td:
    print()
    print(item)
    print()
