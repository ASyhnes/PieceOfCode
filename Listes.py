'''Remplacer un élément dans une liste'''

liste = ['Python', '5', 'py', '4', 'PHP', '8']
# affichage de la liste
print("liste originale : " + str(liste))
#remplacement
res = [elem.replace('4', '5') for elem in liste]
# print result
print("liste apres replacement : " + str(res))


'''Echanger deux éléments d'une liste'''

l = ['a','e','c','d','b','f']
print(l)
idx1 = l.index('e')
idx2 = l.index('b')
l[idx1], l[idx2] = l[idx2], l[idx1]

print(l)

'''Echanger plusieurs éléments d'une liste'''
l = ['c','e','a','d','b','f']
print(l)
for i,j in [(1,4),(0,2)]:
        l[i], l[j] = l[j], l[i]

print(l)

"Transformer une ligne en liste"

'solution1'
str = "Ceci n'est pas du code"
print(str.split())
'''donnera ['Ceci', "n'est", 'pas', 'du', 'code']'''

'Solution2'
str = "ça non plus"
print(list(str.strip()))
''' ['ç', 'a', ' ', 'n', 'o', 'n', ' ', 'p', 'l', 'u', 's']'''


'mélanger une liste de maniére aléatoire'
import random
random.shuffle(liste)

'créer une liste de nombre aléatoire'

import random
random.sample(range(1, 100), 3)
