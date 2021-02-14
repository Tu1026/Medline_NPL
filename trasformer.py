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
            if abstract is None:
                summary_text = None
            else:
                summary_text = summarizer(str(abstract), max_length=100, min_length=5, do_sample=False)[0]['summary_text']
                mod_abstracts[pmid] = summary_text
                print('trained')
***REMOVED***
  ***REMOVED***

sql_out = ***REMOVED***
Update paper
Set mod_abstract = %s
Where Pid = %s
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
        for pid, string in mod_abstracts.items():
            c.execute(sql_out, (string, pid))
***REMOVED***
***REMOVED***
  ***REMOVED***
