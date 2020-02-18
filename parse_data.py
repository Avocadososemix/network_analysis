import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from pathlib import Path as pathlib

os.path.exists("D:\graphs\DBLP_citation_test.txt")
 
test = open(r"D:\graphs\DBLP_citation_test.txt", 'r') 
test.readlines()[0:25]

G = nx.Graph()

def parse_data():
    with open(r'D:\graphs\DBLP-citation-Jan8.txt', 'r',  encoding="utf8") as f:
        reference={}
        readFile = f.readlines()
        for line in readFile:
            
            if '#index' in line:
                G.add_node(line[7:].rstrip())
                reference['index'] = line[7:].rstrip()
                
            elif '#*' in line:
                reference={}
                #G.add_node(reference['index'], title=(line[3:].rstrip()))
                reference['title'] = line[3:].rstrip()
            elif '#@' in line:
                reference['author'] = line[3:].rstrip().rsplit(";")
            elif '#t' in line:
                reference['year'] = line[3:].rstrip()
            elif '#c' in line:
                reference['venue'] = line[3:].rstrip()
            elif '#%' in line:
                G.add_edge(reference['index'], line[2:].rstrip())
            elif '#!' in line:
                reference['abstract'] = line[3:].rstrip()


data = pd.DataFrame(parse_data(), columns =('index', 'id', 'title', 'author',
                                            'year', 
                                  'venue', 'citations', 'abstract'))
                                  
print(G.number_of_nodes(), 'nodes')
print(G.size(), 'edges')
