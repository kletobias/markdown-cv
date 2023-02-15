#!python -m spacy download en_core_web_sm
import re

import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp("This so long.")
print([(w.text, w.pos_) for w in doc])



dir='/Users/tobias/all_code/projects/portfolio-website-2022/_projects/'
files = os.listdir(dir)
files = [f for f in files if f[-3:] == '.md']
pat_html = re.compile(r'<[^>]+>|\\n',re.MULTILINE)

for f in files:
    with open(os.path.join(dir,f),'r') as a:
        article = a.readlines()
        doc = nlp(pat_html.sub('',str(article)))
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        print(f'{f},{len(words)}')
