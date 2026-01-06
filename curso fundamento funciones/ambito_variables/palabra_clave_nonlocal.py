def exterior():
    a = 50 #a es de ámbito local para la función exterior

    def interior():
        nonlocal a
        a = 20


    interior()
    print(a)


exterior()