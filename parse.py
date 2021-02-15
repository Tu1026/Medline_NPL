from re import search
from Bio import Medline,Entrez
from mysql.connector import connect, Error
from contextlib import closing
from collections import defaultdict
import os
articles = defaultdict(list)



search_terms = """
(Sudden Cardiac Arrest) AND (Canada)
"""

Entrez.email = os.environ['email']
handle = Entrez.esearch(db="pubmed", retmax=100, term=search_terms)
pmids = []
records = Entrez.read(handle)
handle.close()
for id in records['IdList']:
    pmids.append(id)

handle = Entrez.efetch(db="pubmed",rettype="medline",retmode="text", id=pmids)
records = Medline.parse(handle)
for record in records:
    try:
        abstract = str(record["AB"])
    except:
        try:
            abstract = str(record['OAB'])
        except:
            abstract = None
            print('passing by')
    pmid = str(record["PMID"])
    title = str(record["TI"]).replace("'", "").replace("[", "").replace("]", "")
    try:
        doi=str(record["AID"])
    except:
        doi = str(record["SO"]).split('doi:',1)[1]
    articles[pmid].append(title)
    articles[pmid].append(abstract)

handle.close()
    
sql= """
INSERT INTO paper (Pid, Title, Abstract, mod_abstract)
Values(%s, %s, %s, %s)
"""

try:
  with closing(connect(host="localhost", user="wilsontu", password="chubbyt566", database="litdb")) as cnxn:
    with closing (cnxn.cursor()) as c:
        for pmid, elements in articles.items():
            c.execute(sql, (pmid, elements[0], elements[1], None))
            c.execute('commit')

except Error as e:
  print(e)

