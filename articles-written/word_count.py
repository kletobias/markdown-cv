#!python -m spacy download en_core_web_sm
import re
import itertools
import os
import numpy as np
import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
from spacy.tokenizer import Tokenizer

nlp = en_core_web_sm.load()



dir='/Users/tobias/all_code/projects/portfolio-website-2022/_projects/'
files = os.listdir(dir)
files = [f for f in files if f[-3:] == '.md']
pat_html = re.compile(r'<[^>]+>|\\n',re.MULTILINE)

# for f in files:
#     with open(os.path.join(dir,f),'r') as a:
#         article = a.readlines()
#         doc = nlp(pat_html.sub('',str(article)))
#         words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
#         print(f'{f},{len(words)}')

out = []
seen = set()
tags = []
patta = re.compile('tags:\s\[(?:(?:\s?\'[a-z A-Z-]+\')+,?)+\]$',re.IGNORECASE)
patsub = re.compile('"')
tre = re.compile(r'''\,''')
l_remove = re.compile(r'\]|\[')
l_remove2 = re.compile(r'\\n')
# def ct(nlp):
#     return Tokenizer(nlp.vocab, infix_finditer=tre.finditer)
# nlp.tokenizer= ct(nlp)

for f in files:
    with open(os.path.join(dir,f),'r') as a:
        for line in itertools.islice(a,2,8):
            tal = patta.findall(line)
            if tal != None:
                for i in tal:
#                    tals = patsub.sub('\'',i)
                    print(f'tals {i}')
                    tags.append(i)
            else:
                continue
# for (idx,tag) in enumerate(tags):
#     tags[idx] = l_remove.sub('',tag)
#     tags[idx] = l_remove2.sub(' ',tag)
print(len(tags))
tags = list(set(tags))
print(len(tags))
# print(np.array(tags).shape)
print(f'\n\n TAGS: {tags[:2]}')
# print(str(tags))
# doc = nlp(str(tags))
#words = [token.text_with_ws for token in doc]
# words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
# print(words)
# print(f'{len(words)}')
for w in tags:
    if w not in seen:
        print(f'w {w}')
        out.append(w)
    seen.add(w)
print(f'\n\nout: {out}')
# for line in itertools.islice(ff,2,8):
#     ttl = patt.search(line)
#     ddl = patd.search(line)
#     ccl = patc.search(line)
#     if ttl != None:
#         ttls = patsub.sub(' ',ttl[1])
#         td[f[:-3]]["title"] = ttls
#     elif ddl != None:
#         ddls = patsub.sub(' ',ddl[1])
#         td[f[:-3]]["description"] = ddls
#     elif ccl != None:
#         ccls = patsub.sub(' ',ccl[1])
#         td[f[:-3]]["category"] = ccls
#     elif tal != None:
#         tals = patsub.sub(' ',tal[1])
#         td[f[:-3]]["tags"] = tals
#     else:
#         continue
# for word in words:
#     if word not in
