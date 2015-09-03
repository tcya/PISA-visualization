import json
import copy

### Reshape PISA data
data = {}
fin_dat = {}
factor = ['bathroom', 'car', 'cell', 'pc', 'tv']
subject = ['Maths', 'Reading', 'Science']
possession = ['None', 'One', 'Two', 'Three or more']
for i in factor:
    with open('generated_data/dat_' + i + '.json','r') as f:
        data[i] = json.loads(f.read())
tmp = {}
for p in possession:
    tmp[p] = {}
tmp2 = {}
for s in subject:
    tmp2[s] = copy.deepcopy(tmp)
tmp3 = {}
for f in factor:
    tmp3[f] = copy.deepcopy(tmp2)
for f in factor:
    for item in data[f]:
        cnt = item['CNT']
        sub = item['Subject']
        poss = item['Number of possession']
        mini = item['Minimum']
        fir_q = item['First quantile']
        median = item['Median']
        thir_q = item['Third quantile']
        maxi = item['Maximum']
        quants = {'Minimum': mini, 'First quantile': fir_q, 'Median': median, 'Third quantile': thir_q, 'Maximum': maxi}
        if cnt not in fin_dat.keys():
            fin_dat[cnt] = copy.deepcopy(tmp3)
        fin_dat[cnt][f][sub][poss] = quants

with open('data.json', 'w') as outfile:
    json.dump(fin_dat, outfile, sort_keys = True, indent = 2)


### Reshape GDP data
gdp = {}
with open('generated_data/gdp_pcap.tsv') as f:
    out = f.readlines()
for line in out[1:]:
    cnt, g = line.split('\t')
    gdp[cnt] = float(g)
with open('gdp_pisa.json', 'w') as outfile:
    json.dump(gdp, outfile, sort_keys = True, indent = 2)
