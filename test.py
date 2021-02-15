from transformers import pipeline
***REMOVED***
***REMOVED***
***REMOVED***

summarizer = pipeline("summarization")

sql_in = ***REMOVED***
Select Pid, Abstract
from paper
***REMOVED***
mod_abstracts = defaultdict(str)
***REMOVED***
***REMOVED***
***REMOVED***
        c.execute(sql_in)
        for pmid, abstract in c.fetchall():
            # if abstract is None:
            #     summary_text = None
            # else:
            #     summary_text = summarizer(str(abstract), max_length=100, min_length=5, do_sample=False)[0]['summary_text']
            #     mod_abstracts[pmid] = summary_text
            if str(pmid) == '33464943':
                print(abstract)
***REMOVED***
  ***REMOVED***
