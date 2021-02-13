***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

pmids_db = []
titles_db=[]
abstracts_db =[]

***REMOVED***
***REMOVED***
***REMOVED***

Entrez.email = 'linshuan@ubc.ca'
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
    abstract = str(record["AB"])
    mesh = str(record["MH"]).replace("'", "").replace("[", "").replace("]", "")
***REMOVED***
***REMOVED***
    pt = str(record["PT"]).replace("'", "").replace("[", "").replace("]", "")
    au = str(record["AU"])
    dp = str(record["DP"])
    la = str(record["LA"])
    pmc = str(record["PMC"])
    si = str(record["SI"])
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
    



with open("citation.txt") as handle:
    ***REMOVED***
    ***REMOVED***
        # pmids.append(record['PMC'])
        # titles.append(record['TI'])
        # abstracts.append(record['AB'])
        print(record['Titl'])
        print('-------------------')


sql= ***REMOVED***
***REMOVED***
Values(?, ?, ?, ?)
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
        for idx, pmid in enumerate(pmids):
            c.execute(sql, (pmid, titles[idx], abstracts[idx]))
***REMOVED***

***REMOVED***
***REMOVED***
