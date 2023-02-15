import itertools
import os


dir='/Users/tobias/all_code/projects/portfolio-website-2022/_projects/'
files = os.listdir(dir)
ll = 2
ul = 8
for f in files:
    if f[-3:] == '.md':
        with open(os.path.join(dir,f),'r') as ff:
            for num,line in zip(range(ll,ul),itertools.islice(ff,ll,ul)):
                print(f'line {num}: {line}')
    else:
        continue

