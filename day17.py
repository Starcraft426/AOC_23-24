# dijsktra algorithm
input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split("\n")                             # plan
n_points, depart = len(list(input[0]))*len(input), 1                        # différents argments obligatoire
arrivee = n_points
l = []
for i, line in enumerate(input):
    for j, elem2 in enumerate(list(line)):
        if i != 0:
            l.append([(i-1)*len(input[0])+j+1, i*len(input[0])+j+1, int(elem2)])
        if j != 0:
            l.append([i*len(input[0])+j, i*len(input[0])+j+1, int(elem2)])
print(l)
#l = [[1,2,1],[1,4,2],[2,6,3],[2,3,2],[4,3,3],[4,5,4],[3,6,3],[3,5,2],[3,7,3],[6,7,4],[5,7,5]]
orient = False                                             # est-ce que le graphe est orienté

adjm = [0]*n_points                                        # création de la matrice d'adjacense
tab3 = list(adjm)
for i in range(n_points):
    adjm[i] = list(tab3)

for elem in l:                                             # remplissage de la matrice d'adjacence
    ligne, colone, valeur = elem
    adjm[ligne-1][colone-1] = valeur
    if not orient:
        adjm[colone-1][ligne-1] = valeur


point = depart-1                                           # point: variable du point acuel, ici, départ
indexes = [i for i in range(n_points) if i+1 != depart]    # indexes valides
trajets = {i: [] for i in range(n_points)}                 # liste des trajets utiles à l'algo
trajets[depart-1].append([None, 0, -1])                    # formation de la donnée de trajet: [point précédent, longueur chemin, last lenght]

# boucle principale
for j in range(n_points):                                  # for et non while car pire des cas nombre de points
    for i, elem in enumerate(adjm[point]):
        if i != point and i in indexes and elem:           # si point valide différent de lui même et lien avec le depart, ajout aux trajets
            trajets[i].append([point, trajets[point][0][1]+elem, trajets[point][0][1]])

    t = []
    for key in trajets:                                    # recherche du prochain point en fonction de la longueur des trajets
        if key in indexes and len(trajets[key]):
            t += [trajets[key][0]+[key]]                   # ajout des trajets valides + numero du point pour savoir lequel choisir
    t.sort(key=lambda l: l[1])                             # tri du plus court
    point = t[0][3]                                        # récupération du point
    del(indexes[indexes.index(point)])                     # suppression du point de la liste

    if point == arrivee-1: break                           # si on est à l'arrivée, finir boucle

point = sorted(trajets[arrivee-1], key= lambda l: l[1])[0] # récupération du dernier point pour retour en arrière
chemin = [arrivee-1]
for i in range(n_points):                                  # retour en arrière
    for elem in trajets[point[0]]:                         # recuperation du bon point en fonction de la longueur chemn, d'où le <last_lenght> dans trajet
        if elem[1] == point[2]:
            chemin.append(point[0])
            point = elem
            break                                          # si point trouvé, plus besoin de chercher
    if point[0] is None:                                   # si point est l'arrivée, fin du programme
        break
chemin= chemin[::-1]                                       # retournement liste
chemin = [elem+1 for elem in chemin]                       # ajout de 1 à chaque valeur (juste pour voir que les points sont les bons si premier point 1 et non 0)
print(chemin)