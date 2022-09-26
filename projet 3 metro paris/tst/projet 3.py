import pickle
from random import*

fich = open('metro.pkl','rb')
graphMetroTest, graphMetro, dicMetro=pickle.load(fich)
fich.close()

graphMini=[[(1,20),(2,28),(5,80)],[(0,20),(2,26),(3,82),(4,78),(5,54)],[(0,28),(1,26),(4,70)],[(1,82),(4,20),(7,36)],[(1,78),(2,70),(3,20),(5,20),(6,16)],[(0,80),(1,54),(4,20),(6,40)],[(4,16),(5,40),(7,24)],[(3,36),(6,24)]]

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

#print("Les voisins de 5 sont",voisins(5))

def existe(S1,S2):
    l1=voisins(S1)
    for voisinsL1 in l1:
        if voisinsL1[0]==S2:
            return True
    return False
#print(existe(5,6))

#print(existe(index_sommet("Belleville","2"),index_sommet("Goncourt","11")))


def poids(som1,som2):
    if not existe(som1,som2):
        return -1
    else:
        for i in voisins(som1):
            if i[0]==som2:
                return i[1]

#print("Le poids est de",poids(5,6))


def aretes():
    listeAretes=[]
    i=0
    for stationsListe in graphMetro:
        for stations in stationsListe:
            listeAretes.append((i,stations[0]))
        i+=1
    return listeAretes
#print(aretes())


def enleve(liste,elt):
    if elt not in liste:
        return "L'élément cherché n'est pas dans la liste. "
    else:
        liste.remove(elt)
    return liste

#print(enleve([1,2,3,4,5],4))
print("\n"*3)
def tableau(graphe):
    tableau = [0] * (len(graphe)+1)
    return tableau

def dijkstra(graphe, dep):
    nonVisites = len(graphe)
    dist = []
    voisin = graphe[dep]
    tab = tableau(graphe)
    fin = 0
    for i in range(len(voisin)):
        dist.append(voisin[i])
    for i in range(len(dist)):
        L = []
        L.append(dist[i][1])
        tab[dist[i][0]] = L[0]
    while [0,0] in tab:
        d = randint(0,len(graphe))
        if tab[d] not in dist:
            voisin = voisins(tab[d][0])
            for i in range(len(voisin)):
                if voisin[i] not in dist:
                    dist.append(voisin[i])
            for i in range(len(dist)-1):
                L = []
                L.append(dist[i][1])
                print('ahgjazhgazzhgjazhgzahgajhg',dist)
                tab[dist[i][0]] = L[0]
    return  tab

print(dijkstra(graphMini,0))





