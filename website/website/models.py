from SPARQLWrapper import SPARQLWrapper, JSON
from string import Template


class SPARQL_Model:

    # test method
    def getAttraction(self):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")

        sparql.setQuery('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:ManMade.
                
                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        print(result)
        return result

    def get_by_attraction(self, attraction):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$key.
                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(key=attraction)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result

    def get_by_att_and_transport(self, attraction, transport):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$attraction;
                alias:hasAccessBy alias:$transport.
                
                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(attraction=attraction, transport=transport)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result

    def get_by_att_tran_fare(self, attraction, transport, fare):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$attraction;
                alias:hasAccessBy alias:$transport;
                alias:hasFare alias:$fare.
                
                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(attraction=attraction, transport=transport, fare=fare)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result

    def get_by_att_tran_fare_enter(self, attraction, transport, fare, entertains):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$attraction;
                alias:hasAccessBy alias:$transport;
                alias:hasFare alias:$fare;
                alias:entertainBy alias:$entertains.
                

                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(attraction=attraction, transport=transport, fare=fare, entertains=entertains)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result

    def get_by_att_tran_fare_enter_room(self, attraction, transport, fare, entertains, room):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$attraction;
                alias:hasAccessBy alias:$transport;
                alias:hasFare alias:$fare;
                alias:entertainBy alias:$entertains;
                alias:hasFacilityOf alias:$room.

                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(attraction=attraction, transport=transport,
                                 fare=fare, entertains=entertains, room=room)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result

    def get_by_att_fare(self, attraction, fare):
        sparql = SPARQLWrapper("http://localhost:3030/mydataset/sparql")
        query = Template('''
            PREFIX alias: <http://www.semanticweb.org/vishnupv/ontologies/testontology#>
            SELECT *
            WHERE {
                ?attraction a alias:$attraction;
                alias:hasFare alias:$fare.

                ?attraction alias:id ?id.
                ?attraction alias:name ?name.
                ?attraction alias:highlight ?highlight.
                ?attraction alias:location ?location.
            }
        ''')
        query = query.substitute(attraction=attraction, fare=fare)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        result = sparql.query().convert()
        return result