import pandas as pd
import rdflib
import time

import ssl

ssl._create_default_https_context = ssl._create_unverified_context



def getDCAT(url):

    try:

        graph = rdflib.Graph()

        partials = rdflib.Graph()

        graph.parse(url, format='xml')

    except:

        return graph

    DCAT = rdflib.Namespace("http://www.w3.org/ns/dcat#")

    #match += graph.triples((None, rdflib.RDF.type, DCAT.Catalog))
   
    for x in graph.triples((None, rdflib.RDF.type, DCAT.Dataset)):
        for y in graph.triples((x[0], None, None)):
            partials.add(y)
            #print(y)
        

    for x in graph.triples((None, rdflib.RDF.type, DCAT.Distribution)):
        for y in graph.triples((x[0], None, None)):
            partials.add(y)
            #print(y)
    
    return partials

bigG = rdflib.Graph()

DCAT = rdflib.Namespace("http://www.w3.org/ns/dcat#")
DCT = rdflib.Namespace("http://purl.org/dc/terms/")
DCE = rdflib.Namespace("http://purl.org/dc/elements/1.1/")


bigG.bind("dcat", DCAT)
bigG.bind("dct", DCT)
bigG.bind("dce", DCE)

data = pd.read_csv("1.csv")

for x in data.itertuples():


    RDF = x.RDF
    DCAT = x._8

    if pd.isna(DCAT) and not pd.isna(RDF) and RDF.split(".")[-1] != "geojson":
    
        print("RDF:",RDF)

        bigG += getDCAT(RDF)

        #time.sleep(1)

    if not pd.isna(DCAT):
    
        print("DCAT:", DCAT)

        bigG += getDCAT(DCAT)

        #time.sleep(1)

data = pd.read_csv("2.csv")

for x in data.itertuples():


    RDF = x.RDF
    DCAT = x._8

    if pd.isna(DCAT) and not pd.isna(RDF) and RDF.split(".")[-1] != "geojson":
    
        print("RDF:",RDF)

        bigG += getDCAT(RDF)

        #time.sleep(1)

    if not pd.isna(DCAT):
    
        print("DCAT:", DCAT)

        bigG += getDCAT(DCAT)

        #time.sleep(1)

data = pd.read_csv("3.csv")

for x in data.itertuples():


    RDF = x.RDF
    DCAT = x._9

    if pd.isna(DCAT) and not pd.isna(RDF) and RDF.split(".")[-1] != "geojson":
    
        print("RDF:",RDF)

        bigG += getDCAT(RDF)

        #time.sleep(1)

    if not pd.isna(DCAT):
    
        print("DCAT:", DCAT)

        bigG += getDCAT(DCAT)

        #time.sleep(1)

file = open("output.rdf", "w")
file.write(bigG.serialize(format="xml").decode("utf-8"))



    
