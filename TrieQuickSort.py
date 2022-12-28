'''Source: https://www.youtube.com/watch?app=desktop&v=YNCKVNPI8Qs'''

def quicksort(liste):
    if len(liste) <=1:
        return liste
    pivot = liste.pop()
    '''pop renvoi au dernier elément de la liste et le suprime'''

    petit = []
    '''création de la liste "petit"'''
    grand = []
    '''idem "grand"'''

    '''création d'une fonction: tout ce qui est plus petit va dans la lsite "pett" 
    et plus grand dans la liste "grand'''

    for nombre in liste:
        if nombre < pivot:
            petit.append(nombre)
        else:
            grand.append(nombre)
    return quicksort(petit)+[pivot]+quicksort(grand)
A = [1,9,178,9,987,987,11]
print(quicksort(A))