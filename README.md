# Network analysis Project
Citation network analysis

### Project Description
---------------------

An analysis of the scientific paper and citation aminer dataset https://www.aminer.cn/citation. 

We aim to see how different classification methods cluster the papers, and if the clusters show a predisposition towards clustering within the same scientific journals that the nodes/papers are from. Our assumption is that there will be clusters within clusters, with scientific domains making up the highest level clusters, and individual journals being the subclusters within the domain cluster. If we are able to classify journals by their respective scientific domains, we will use this to accomplish our task.

Our other approach to the data is to analyse the noun phrases in the article abstracts. We will possibly use TextBlob tool to parse the noun phrases out of the abstracts. We will then compare the noun phrases found inside a cluster and see if there are any common nouns between articles within the same cluster. 
---------------------

Direct link to ACM citation data used:
[Citation-network V1](https://lfs.aminer.cn/lab-datasets/citation/citation-network1.zip)

TextBlob tool:
[TextBlob](https://textblob.readthedocs.io/en/dev/)
