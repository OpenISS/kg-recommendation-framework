from owlready2 import *

def add_individual(class_name, individual_name):
    path = "/Users/yuhaomao/master/sample/hello2222.rdf"
    onto = get_ontology(path).load()
    with onto:
        # print(class_name)
        exec('onto.{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
        # exec('("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
    onto.save("/Users/yuhaomao/master/sample/hello2222.rdf")

def add_objectproperty(domain_name,objectproprety,range_name):
    path = "/Users/yuhaomao/master/sample/hello2222.rdf"
    onto = get_ontology(path).load()
    with onto:
        exec('class {0}(ObjectProperty): \n domain=[{1}] \n range = [{2}]'.format(objectproprety,domain_name,range_name))
        onto.save("/Users/yuhaomao/master/sample/hello2222.rdf")
        
def add_triples(domain_name,objectproprety,range_name):
    path = "/Users/yuhaomao/master/sample/hello2222.rdf"
    # iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
    onto = get_ontology(path).load()
    with onto:
        exec('onto.{0}.{1} = [onto.{2}]'.format(domain_name,objectproprety,range_name))
        # onto.test1.has_for_ingredient = [onto.acetaminophen]
        onto.save("/Users/yuhaomao/master/sample/hello2222.rdf")

# add_triples("test1",'has_for_ingredient', 'acetaminophen')
# add_objectproperty("Thing","xxx","Thing")

def add_2rdf(triples):
    """
    triples is a list [[head,relation,tail],[...],[...]]
    """
    path = "/Users/yuhaomao/master/sample/hello2222.rdf"
    onto = get_ontology(path).load()
    
    for i in triples:
        head = i[0]
        relation = i[1]
        tail = i[2]
        
        with onto:
            head_exist = exec('onto.{}'.format(head))
            relation_exist = exec('onto.{}'.format(relation))
            tail_exist = exec('onto.{}'.format(tail))
            if head_exist != None and relation_exist != None and tail_exist != None:
                add_triples(head, relation, tail)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", head)
                if relation_exist == None:
                    add_objectproperty("Thing", relation, "Thing")
                if tail_exist == None:
                    add_individual("owl:Thing", tail)
                add_triples(head, relation, tail)

# triples = [['movie1', 'has_for_ingredient111111', 'idontknow'], ['rm1022288896', 'poster_link', 'movie1'], ['my_drug', 'new_relation', 'new_drug'], ['test1', 'has_for_ingredient', 'acetaminophen']]
# add_2rdf(triples)