import pydcatchu

NS = pydcatchu.BaseNamespace("https://mgds.oeg.fi.upm.es/")

A1 = pydcatchu.Agent("MGDS")
A1.set_namespace(NS)

C1 = pydcatchu.Catalogue("Raw data", "Raw input data", A1)
C1.set_namespace(NS)

Da1 = pydcatchu.Dataset("Carto", "Cartographic data for MGDS visualizer")
Da1.set_namespace(NS)

Di1 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/raw/Carto.tar.xz")
Di1.set_namespace(NS)
Di1.set_title("Compressed folder")

Da1.add_distribution(Di1)


Da2 = pydcatchu.Dataset("Sentinel-2 observation", "Satelite data for MGDS visualizer")
Da2.set_namespace(NS)

Di2 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/raw/sentinel/T30TVK_20201219T110451_B04.jp2")
Di2.set_namespace(NS)
Di2.set_title("B04 band")

Da2.add_distribution(Di2)

Di3 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/raw/sentinel/T30TVK_20201219T110451_B08.jp2")
Di3.set_namespace(NS)
Di3.set_title("B08 band")

Da2.add_distribution(Di3)


Da3 = pydcatchu.Dataset("Censal", "Census data for MGDS visualizer")
Da3.set_namespace(NS)

Di4 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/raw/Censal.tar.xz")
Di4.set_namespace(NS)
Di4.set_title("Compressed folder")


Da3.add_distribution(Di4)


# JSON

Da4 = pydcatchu.Dataset("Processed data", "Processed data for MGDS visualizer in JSON format")
Da4.set_namespace(NS)

Di5 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/json/barrios_shape.json")
Di5.set_namespace(NS)

Da4.add_distribution(Di5)

Di6 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/json/distritos_shape.json")
Di6.set_namespace(NS)

Da4.add_distribution(Di6)

Di7 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/json/indexesBarrios.json")
Di7.set_namespace(NS)

Da4.add_distribution(Di7)

Di8 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/json/indexesCensal.json")
Di8.set_namespace(NS)

Da4.add_distribution(Di8)

Di9 = pydcatchu.Distribution("https://mgds.oeg.fi.upm.es/static-data/json/indexesDistritos.json")
Di9.set_namespace(NS)

Da4.add_distribution(Di9)



C1.add_dataset(Da1)
C1.add_dataset(Da2)
C1.add_dataset(Da3)
C1.add_dataset(Da4)

print(C1.graph().serialize(format="xml").decode("UTF-8"))

