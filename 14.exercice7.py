# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").
# Stockez cette valeur dans une variable nombres.nombres est une chaîne de caractères (str)
nombre=input("saisir une liste en separant les elemsent par une virgule ")
somme=0

# Utilisez la fonction split(explication de la fonction) pour transformer cette chaîne de caractères en une variable de type liste liste.liste est une liste de chaîne de caractères.
listNombre=nombre.split(',')

#Transformez liste en une liste d'entiers liste_entiers, en utilisant la fonction int. Vous devrez convertir chaque élément un par un ! Utilisez une boucle.
listNombreint=[]
for nb in listNombre:
    entier=int(nb)
    listNombreint.append(entier)

#Calculez et affichez la somme des nombres dans la liste.
for nb in listNombreint:
    somme=somme+nb
print(f"la somme est: {somme}")

#Calculez et affichez la moyenne des nombres dans la liste.
moyenne=round(somme/len(listNombreint),2)
print(f"la moyenne est: {moyenne}")

#Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne
n=0
for nb in listNombreint:
    if float(nb)>moyenne:
        n=n+1
print(f"le nombre des elment superieur à la moyenne ({moyenne}) dans la liste sont au nombre de: {n}")