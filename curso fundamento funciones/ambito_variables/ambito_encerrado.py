def exterior():
    a = 50 #a es de ámbito local para la función exterior

    def interior():
        print(a) #interior puede acceder a la variable a de exterior


    interior()


exterior()