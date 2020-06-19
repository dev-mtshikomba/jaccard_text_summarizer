# jaccard_text_summarizer
Using the Jaccard ranking algorithm to summarize a document

>>
This summarizer is based off of the Jaccard Similarity ranking algorithm and it assumes the first sentence is the most important as it is believed its purpose is to introduce the document and its topic, all sentences below it simply extends it with greater in-depth explanations. 
The first step is to check how similar each sentence is to the first sentence of the document using the Jaccard similarity. Based on this result we rank the sentences in the document from most similar to least similar. 
The higher the rank score the more similar the sentence is to the first sentence.  After ranking the sentences, we pick the top N sentences and use them to summarize (create a much shorter version of the document) the document.
This algorithm does not take sentences into consideration with a zero-rank score

>>
I belived there is more cleaning and stemming that needs to be done on this algorithm.

## Install Requirements
```
pip install -r requirements.txt
```

- Open the notebook and start experimenting
- You can also copy the Jaccard_summarizer into you project and customize it, but please dont forget to credit this respository. Enjoy!
