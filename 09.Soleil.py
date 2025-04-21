avec_soleil =False
en_semaine = False

if avec_soleil and not en_semaine:
    print("On va à la plage!")
elif avec_soleil and en_semaine:
    print("On va au travail!")
else:
    print("On reste à la maison!")