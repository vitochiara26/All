# class Ave:
#     def volar(self):
#         return "Estoy volando"

# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    
# def hacerVolar(ave = Ave):
#     return ave.volar()

# print(hacerVolar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave):
    pass
