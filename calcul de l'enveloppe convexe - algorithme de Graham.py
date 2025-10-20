"""
Calcul de l'enveloppe convexe - algorithme de Graham

Le but de ce programme est de relier les points appartenants à l'enveloppe
convexe d'un nuage de points, et ce en utilisant l'algorithme de Graham.

Compléxité en temps : O(n) + O(n * log(n)) + O(n) = O(n * log(n))
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math

def visuel(points, connections=[]):
    """
    La fonction prend en entrée les points ainsi que les connections entre les points
    et réalise un graphique en reliant ces points
    """
    liens = []
    for i in range(len(connections)-1):
        liens.append((connections[i], connections[i+1]))
    liens.append((connections[0], connections[-1]))
    connections = liens

    numbers = []
    for connection in connections:
        numbers.append((points.index(connection[0]), points.index(connection[1])))
    connections = numbers

    points = np.array(points) # On convertit la liste des coordonnées des points en tableau numpy
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, color='blue') #On affiche les points
    for connection in connections: #On fait les connections en rouge
        x = [points[i][0] for i in connection]
        y = [points[i][1] for i in connection]
        plt.plot(x, y, color='red', marker='o')
    for i, point in enumerate(points): #annotation des points
        plt.annotate(str(i), (point[0], point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Représentation des lignes')
    plt.grid(True)
    plt.show()

#calcul de l'angle entre deux points et l'horizontale
def angle(point1, point2):
    # Calcul des différences entre les coordonnées x et y des deux points
    diff_x = point2[0] - point1[0]
    diff_y = point2[1] - point1[1]
    # Calcul de l'angle en radians en utilisant atan2
    angle_radians = math.atan2(diff_y, diff_x)
    # Conversion de l'angle en degrés
    angle_degres = math.degrees(angle_radians)
    return angle_degres

def orientation(triplet):
    #Renvoie true si on a tourné à gauche, False si on a tourné à droite
    p = triplet[0]
    q = triplet[1]
    r = triplet[2]
    return ((q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])) >= 0

n = 50

#Génération de points aléatoires
print("Génération des points...")
points = [(random.randint(-1000,1000),random.randint(-1000,1000)) for i in range(n)]
p = points.copy()

#Graham scan
#Calcul du point tout en bas (il est sur l'enveloppe convexe)
print("Détermination du point du bas..")
bas = points.copy()
bas.sort(key = lambda x: x[1])
bas = bas[0]
#calcul de tous les angles avec le point du bas et l'horizontale
print("Rangement des points...")
connexions = []
angles = []
for point in points:
    angles.append([angle(bas, point), point])
angles.sort(key = lambda x: x[0])

#On relie les points dans l'ordre des angles avec l'horizontale
for i in range(n-1):
    connexions.append((angles[i][1], angles[i+1][1]))
connexions.append((angles[n-1][1], angles[0][1]))

#visuel(p, connexions)
temp = []
for duo in connexions:
    temp.append(duo[0])
    temp.append(duo[1])
connexions = temp

temp = []
for point in angles:
    temp.append(point[1])
points = temp

print("Suppressions des chemins erronés et création des nouveaux...")

plt.ion()  # Activation du mode interactif
plt.draw()
visuel(p, points)
plt.pause(1)
c = 0
while c < len(points)-2:
    triplet = points[c:c+3]
    g = orientation(triplet)
    if g:
        c += 1
        plt.draw()
        visuel(p, points)
        plt.pause(.05)
        plt.clf()
    else:
        points.pop(c+1)
        c -= 1

plt.ioff()  # Désactivation du mode interactif
visuel(p, points)