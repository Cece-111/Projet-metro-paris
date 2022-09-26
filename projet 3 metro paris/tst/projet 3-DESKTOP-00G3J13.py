import pickle

fich = open('metro.pkl','rb')
graphMetroTest, graphMetro, dicMetro=pickle.load(fich)
fich.close()

print(graphMetroTest,"\n\n" ,graphMetro,"\n\n", dicMetro) ############################

def index_sommet(station, ligne):
    return(dicMetro[str(station), str(ligne)])

def infoStation(index):
    for cle in dicMetro.keys():
        if dicMetro[cle] == index:
            return cle


def voisins(numSommetIndex):
    listeSommetVopisin=[]
    for nbVoisins in range(len(graphMetro[numSommetIndex])):
        listeSommetVopisin.append(graphMetro[numSommetIndex][nbVoisins])
    return(listeSommetVopisin)

print("Les voisins de 5 sont",voisins(5))

def existe(S1,S2):
    l1=voisins(S1)
    for voisinsL1 in l1:
        if voisinsL1[0]==S2:
            return True
    return False
print(existe(5,6))

print(existe(index_sommet("Belleville","2"),index_sommet("Goncourt","11")))


def poids(som1,som2):
    if not existe(som1,som2):
        return -1
    else:
        for i in voisins(som1):
            if i[0]==som2:
                return i[1]

print("Le poids est de",poids(5,6))


def aretes():
    listeAretes=[]
    i=0
    for stationsListe in graphMetro:
        for stations in stationsListe:
            listeAretes.append((i,stations[0]))
        i+=1
    return listeAretes
print(aretes())


def enleve(liste,elt):
    if elt not in liste:
        return "L'élément demandé n'est pas dans la liste"
    else:
        liste.remove(elt)
    return liste

