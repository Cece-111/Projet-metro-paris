import pickle
from random import *

fichier = open('metro.pkl','rb')
grapheMetroTest, grapheMetro, dicMetro=pickle.load(fichier)
fichier.close()



def index_sommet(station, ligne):
    return(dicMetro[str(station), str(ligne)])

index_sommet('Pont-Neuf', '7')



def infoStation(index):
    for cle in dicMetro.keys():
        if dicMetro[cle] == index:
            return cle

##infoStation(173)



def voisins(numSommetIndex, graphe):
    listeSommetVoisin = []
    for nbVoisins in range (len(graphe[numSommetIndex])):
        listeSommetVoisin.append(graphe[numSommetIndex][nbVoisins])
    return  listeSommetVoisin

##voisins(index_sommet('Pont-Neuf', '7'))



def existe(S1, S2, graphe):
    l1=voisins(S1, graphe)
    for voisinsL1 in l1:
        if voisinsL1[0]==S2:
            return True
    return False

##existe(index_sommet("Belleville", 2),index_sommet("Goncourt", 11))



def poids(som1, som2, graphe):
    if not existe(som1,som2, graphe):
        return -1
    else:
        for i in voisins(som1, graphe):
            if i[0]==som2:
                return i[1]

##"Le poids est de",poids(index_sommet("Belleville", 2),index_sommet("Belleville", 2))



def aretes(graphe):
    listeAretes=[]
    i=0
    for stationsListe in graphe:
        for stations in stationsListe:
            listeAretes.append((i,stations[0]))
        i+=1
    return listeAretes

##aretes()



def enleve(liste, elt):
    if elt in liste:
        liste.remove(elt)
    return liste

def indice(L,n,dep):
    if n in L:
        for i in range(len(L)):
            if L[i] == n:
                return i-dep
    else:
        return 0

def tableau(graphe):
    tableau = [0] * (len(graphe))
    return tableau

grapheMini = [[(1,20),(2,28),(5,80)],[(0,20),(2,26),(3,82),(4,78),(5,54)],[(0,28),(1,26),(4,70)],[(1,82),(4,20),(7,36)],[(1,78),(2,70),(3,20),(5,20),(6,16)],[(0,80),(1,54),(4,20),(6,40)],[(4,16),(5,40),(7,24)],[(3,36),(6,24)]]

def dijkstra(graphe, dep):
    distances = [float('inf')]*len(graphe)
    distances[dep] = 0
    for i in range(2):
        nonVisites = [i for i in range(len(graphe))]
        while nonVisites != []:
            s = min(nonVisites)
            voisin = voisins(s, graphe)
            for elem in voisin:
                distances[elem[0]] = min(distances[elem[0]], distances[s] + elem[1])
            nonVisites.pop(indice(distances,s,dep))
    return distances

##print(dijkstra(grapheMini, 0))

def dijkstraChem(graphe, dep):
    distances = [float('inf')] * len(graphe)
    distances[dep] = 0
    pred = [0] * len(graphe)
    pred[dep] = -1
    for i in range(2):
        nonVisites = [i for i in range(len(graphe))]
        while nonVisites != []:
            s = min(nonVisites)
            voisin = voisins(s, graphe)
            for elem in voisin:
                if distances[elem[0]] > distances[s] + elem[1]:
                    distances[elem[0]] = distances[s] + elem[1]
                    pred[elem[0]] = s
            nonVisites.pop(indice(distances,s,dep))
    return distances, pred

##print(dijkstraChem(grapheMini, 0))

def cheminD(pred):
    chemin = [[] for i in range(len(pred))]
    for i in range(len(pred)):
        if pred[i] <= 0:
            chemin[i].append(i)
        else:
            j = i
            while j != 0:
                chemin[i].append(j)
                j = pred[j]
            chemin[i].append(j)
    for i in range(len(chemin)):
        chemin[i].reverse()
    for i in range(len(chemin)):
        if len(chemin[i]) > 1:
            chemin[i] = tuple(chemin[i])
    return chemin

##print(cheminD([-1, 0, 0, 1, 5, 1, 4, 6]))

def afficheChemin(s1,s2,graphe):
    d,p=dijkstraChem(graphe,s1)
    chemin = cheminD(p)
    return chemin[s2]

##print(afficheChemin(0,7,grapheMini))