from transformers import pipeline
from contextlib import closing
from mysql.connector import connect, Error
from collections import defaultdict

summarizer = pipeline("summarization")

sql_in = """
Select Pid, Abstract
from paper
"""
mod_abstracts = defaultdict(str)
try:
  with closing(connect(host="localhost", user="wilsontu", password="chubbyt566", database="litdb")) as cnxn:
    with closing (cnxn.cursor()) as c:
        c.execute(sql_in)
        for pmid, abstract in c.fetchall():
            # if abstract is None:
            #     summary_text = None
            # else:
            #     summary_text = summarizer(str(abstract), max_length=100, min_length=5, do_sample=False)[0]['summary_text']
            #     mod_abstracts[pmid] = summary_text
            if str(pmid) == '33464943':
                print(abstract)
except Error as e:
    print(e)
