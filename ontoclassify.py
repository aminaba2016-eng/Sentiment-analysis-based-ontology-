#!/usr/bin/python

# from lxml import etree

# realation = etree.parse("C:/Users/HP/Desktop/memoire/Newontologieresto.owl")
# for type_rel in realation.xpath("/Ontology/Prefix/Declaration"):
#    value = type_rel.get('Class IRI')
#    print(value)

# from lxml import etree
# tree = etree.parse("C:/Users/HP/Desktop/memoire/restaurantonto4.owl")
# for user in tree.xpath("/Ontology/Declaration/Class"):
#     print(user.get("IRI"))
from lxml import etree

tree = etree.parse("C:/Users/HP/Desktop/memoire/restaurantonto100.owl")
for user in tree.xpath("/Ontology/Declaration/Class"):
    print(user.get("IRI"))
for x in tree.xpath("/Ontology/Declaration/NamedIndividual"):
    print(x.get("IRI"))
# for x in tree.xpath("//ClassAssertion/Class"):
#    if x.get("IRI") == "#concept_negative":
#        g = tree.xpath("//ClassAssertion/Class/NamedIndividual")
#        print(g.get('IRI'))
from owlready2 import *
onto = get_ontology("file://Newontologieresto.owl").load()

for i in onto.instances():
    print(i)








