import os

libs = {"rdflib" , "networkx" , "matplotlib" , "py2neo",
        "owlready2","pandas","random","numpy","tensorflow==1.14.0","abc",
        "scikit-learn","linecache","time","os","requests",
        "bs4","imdb","base64","Uillib"}
try:
    for lib in libs:
        os.system(" pip3 install " + lib)
        print("{}   Install successful".format(lib))
except:
    print("{}   failed install".format(lib))