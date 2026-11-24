"""Gera um CSV FICTÍCIO no formato do Scimago, só para testar o portal.
Os valores de SJR são inventados. Troque pelos CSVs reais baixados do Scimago."""
import random, csv, sys
random.seed(7)
saida = sys.argv[1]
# (ISSN, título, categorias)
reais = [
 ("00949655","Journal of Statistical Computation and Simulation",["Statistics and Probability","Modeling and Simulation"]),
 ("01692070","International Journal of Forecasting",["Business and International Management","Statistics and Probability","Economics and Econometrics"]),
 ("09275398","Journal of Empirical Finance",["Finance","Economics and Econometrics"]),
 ("22251146","Econometrics",["Economics and Econometrics","Statistics and Probability"]),
 ("00036846","Applied Economics",["Economics and Econometrics"]),
 ("15372707","Journal of Business and Economic Statistics",["Statistics and Probability","Economics and Econometrics"]),
 ("1099131X","Journal of Forecasting",["Economics and Econometrics","Statistics and Probability"]),
 ("19845146","Revista Brasileira de Financas",["Finance","Economics and Econometrics"]),
 ("24523062","Econometrics and Statistics",["Statistics and Probability","Economics and Econometrics"]),
 ("16790731","Revista Brasileira de Financas (impresso)",["Finance"]),
 ("03777332","Empirical Economics",["Economics and Econometrics"]),
 ("1093474X","Journal of the American Water Resources Association",["Water Science and Technology","Ecology"]),
 ("03784754","Mathematics and Computers in Simulation",["Modeling and Simulation","Numerical Analysis"]),
]
cats = ["Statistics and Probability","Economics and Econometrics","Finance","Modeling and Simulation",
        "Water Science and Technology","Ecology","Numerical Analysis","Business and International Management"]
linhas=[]; sid=1000
for issn,t,cs in reais:
    sid+=1; linhas.append((sid,t,issn,round(random.uniform(0.15,3.5),3),cs))
for i in range(260):
    sid+=1
    cs=random.sample(cats,random.choice([1,1,2]))
    linhas.append((sid,f"Periódico fictício {i:03d}",f"9{i:07d}",round(random.expovariate(1/0.8),3),cs))
linhas.sort(key=lambda x:-x[3])
with open(saida,"w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f,delimiter=";",quoting=csv.QUOTE_ALL)
    w.writerow(["Rank","Sourceid","Title","Type","Issn","SJR","SJR Best Quartile","H index","Categories","Areas"])
    for r,(sid,t,issn,sjr,cs) in enumerate(linhas,1):
        q="Q1" if r<=len(linhas)*.25 else "Q2" if r<=len(linhas)*.5 else "Q3" if r<=len(linhas)*.75 else "Q4"
        w.writerow([r,sid,t,"journal",issn,str(sjr).replace(".",","),q,10,"; ".join(f"{c} ({q})" for c in cs),"Mixed"])
