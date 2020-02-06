import pandas as pd
import math

def topsis(arglist):

    dataset = pd.read_csv(arglist[0])

    d = dataset.iloc[:, 1:]

    for column in d:
        v_nfac = math.sqrt(sum(x*x for x in d[column]))
        d[column] = d[column]/v_nfac
    
    weight_list = map(int, arglist[1].split(','))

    weight_list = [float(x)/sum(weight_list) for x in weight_list]

    i = 0

    for column in d:
        d[column] = d[column]*weight_list[i]
        i = i + 1

    i = 0

    beh_list = list(arglist[2].split(','))

    Vb = []
    Vw = []

    for column in d:
        if beh_list[i] == '+':
            Vb.append(max(d[column]))
            Vw.append(min(d[column]))
        else:
                Vb.append(min(d[column]))
                Vw.append(max(d[column]))
        i = i + 1
    
    Perf_score = []

    for row in d.itertuples(index=False):
        i = 0
        eucvalB = 0
        eucvalW = 0
        for x in row:
            eucvalB = eucvalB + (x - Vb[i])*(x - Vb[i])
            eucvalW = eucvalW + (x - Vw[i])*(x - Vw[i])
            i = i + 1
        eucvalB = math.sqrt(eucvalB)
        eucvalW = math.sqrt(eucvalW)
        Perf_score.append(eucvalW/(eucvalW + eucvalB))
    
    dataset['Performance Score'] = Perf_score
    dataset["Rank"] = dataset["Performance Score"].rank(ascending=False)

    dataset.to_csv(arglist[0], index=False)
    Atts = dataset.iloc[:,0]
    Ranks = dataset.iloc[:,-1]
    print("Best Attribute: {}".format(Atts[Ranks.idxmin()]))