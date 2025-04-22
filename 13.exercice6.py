#Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans nombre1 et nombre2.
nombre1=input("entrez le prremier nombre")
nombre2=input("entrez le deuxieme nombre")
resultat=0

#nombre1 et nombre2 sont des chaînes de caractères (str). Utilisez la fonction isnumeric (explication de la fonction) pour vérifier que ce sont des nombres.
# 1.Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")
# 2.Sinon, convertissez les deux nombres en nombres entiers avec la fonction int.
# 3.Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.
# 4. Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme
# 5. Effectuez le calcul en fonction de la valeur de operation (par exemple en utilisant if - elif - else) et stockez le résultat dans la variable resultat.
# 6. Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour quitter le programme si le deuxième nombre est 0.
if (nombre1.isnumeric() and nombre2.isnumeric()):
    nombre1=int(nombre1)
    nombre2=int(nombre2)
    operation=input("Quelle operation souhaitez-vous utilisez?")
    if(operation in ("+","-","*","/",)):
        if(operation=="+"):
            resultat=nombre1+nombre2
        elif(operation=="-"):
            resultat=nombre1-nombre2
        elif(operation=="*"):
            resultat=nombre1*nombre2
        else:
            if nombre2==0:
                raise SystemExit(operation," on peut pas diviser par 0.________Fin du programme_______")
            # Astuce : lors de la division, utilisez la fonction round pour arrondir le résultat et le rendre plus lisible !
            resultat=round(nombre1/nombre2,2)
    else:
        raise SystemExit(operation," n'est pas une operation._________Fin du programme________")
else:
    raise SystemExit("_______Fin du programme_______")

#Affichez le resultat.
print(resultat)

