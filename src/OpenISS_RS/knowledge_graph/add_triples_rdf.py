from owlready2 import *

def add_individual(class_name, individual_name,path):
    """
    add individual
    """
    onto = get_ontology(path).load()
    with onto:
        # print(class_name)
        exec('onto.{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
        # exec('("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
        onto.save(path)

def add_objectproperty(domain_name,objectproprety,range_name,path):
    """
    add objectproperty
    """
    onto = get_ontology(path).load()
    with onto:
        exec('class {0}(ObjectProperty): \n domain=[{1}] \n range = [{2}]'.format(objectproprety,domain_name,range_name))
        onto.save(path)
        
def add_triple(domain_name,objectproprety,range_name,path):
    """
    add a triple to path file
    """
    onto = get_ontology(path).load()
    with onto:
        exec('onto.{0}.{1} = [onto.{2}]'.format(domain_name,objectproprety,range_name))
        # onto.test1.has_for_ingredient = [onto.acetaminophen]
        onto.save(path)

def add_triples(triples,path):
    """
    triples is a list [[head,relation,tail],[...],[...]]
    """
    onto = get_ontology(path).load()
    
    for i in triples:
        print("sss")
        print(i)
        head = i[0]
        relation = i[1]
        tail = i[2]
        print(head)
        print(relation)
        print(tail)
        
        with onto:
            head_exist = exec('onto.{}'.format(head))
            relation_exist = exec('onto.{}'.format(relation))
            tail_exist = exec('onto.{}'.format(tail))
            if head_exist != None and relation_exist != None and tail_exist != None:
                add_triple(head, relation, tail,path)
            else:
                if head_exist == None:
                    add_individual("owl:Thing", head,path)
                if relation_exist == None:
                    add_objectproperty("Thing", relation, "Thing",path)
                if tail_exist == None:
                    add_individual("owl:Thing", tail,path)
                add_triple(head, relation, tail,path)
            onto.save(path)



a = [['Anthony_Russo', 'director', 'Avengers_Endgame_2019'],
['Robert_Downey_Jr', 'star', 'Iron_Man_2008'],
['Robert_Downey_Jr', 'writer', 'Русский_ковчег'],
['star_A', 'star', 'Ahí_va_el_diablo']]
add_triples(a,"../../samples/hello2222.rdf")


# [' Anthony Russo.', 'director', 'Avengers:_Endgame_(2019)']
# ['Robert_Downey_Jr.', 'star', 'Iron_Man_(2008)']
# ['Robert_Downey_Jr.', 'writer', 'Русский_ковчег']
# ['star_A', 'star', 'Ahí_va_el_diablo']