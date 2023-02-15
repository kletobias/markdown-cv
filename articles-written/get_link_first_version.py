import os
import re

dir='/Users/tobias/all_code/projects/portfolio-website-2022/_projects/'
files = os.listdir(dir)
host = 'https://deep-learning-mastery.com/projects/'
# for f in files:
#     print(f)
#     print(f'is .md: {f[-3:] == ".md"}')

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

mdf = cl(files,host)
print(mdf)

def get_title_description(dir,files):
    patt = re.compile('^title:\s\'(.+)\'$',re.IGNORECASE)
    patd = re.compile('^description:\s\'(.+)\'$',re.IGNORECASE)
    patsub = re.compile('<br>')
    md_files = []
    cv_text_all = []
    td = {}
    for f in files:
        if f[-3:] == '.md':
            td[f] = {}
            md_files.append(f)
            indicator = 0
            with open(os.path.join(dir,f),'r') as ff:
                for line in ff.readlines():
                    buf = line
                    if indicator == 0:
                        ttl = patt.search(buf)
                        if ttl != None:
                            ttls = patsub.sub(' ',ttl[1])
                            td[f]["title"] = ttls
                            indicator += 1
                        else:
                            continue
                    if indicator == 1:
                        ddl = patd.search(buf)
                        if ddl != None:
                            ddls = patsub.sub(' ',ddl[1])
                            td[f]["description"] = ddls
                            indicator += 1
                        else:
                            continue
    for k in td.keys():
        print(td[k].items())
        cv_text = f'\n{td[k]["title"]}\n\n{td[k]["description"]}\n\n'
        cv_text_all.append(cv_text)

    with open('cv_articles.md','w+') as f:
        for item in cv_text_all:
            f.write(item)
    return cv_text_all

td = get_title_description(dir,files)
for item in td:
    print()
    print(item)
    print()
