"""Top5 hoteles mejores valuados"""
hotel_uno = input("Ingresa el nombre del hotel numero 1: ")
punt_hotel_uno =  input("Ingresa la puntuación del hotel numero 1: ")

hotel_dos = input("Ingresa el nombre del hotel numero 2: ")
punt_hotel_dos =  input("Ingresa la puntuación del hotel numero 2: ")

hotel_tres = input("Ingresa el nombre del hotel numero 3: ")
punt_hotel_tres =  input("Ingresa la puntuación del hotel numero 3: ")

orden = "El orden de los hoteles es: \n"
hotel_uno += ". Stars:"+str(punt_hotel_uno) + "/5 \n"
hotel_dos += ". Stars:"+str(punt_hotel_dos) + "/5 \n"
hotel_tres += ". Stars:"+str(punt_hotel_tres) + "/5 \n"


print(orden + hotel_uno + hotel_dos + hotel_tres + str(punt_hotel_uno > punt_hotel_dos > punt_hotel_tres))
print(orden + hotel_uno + hotel_tres + hotel_dos + str(punt_hotel_uno > punt_hotel_tres > punt_hotel_dos))

print(orden + hotel_dos + hotel_uno + hotel_tres + str(punt_hotel_dos > punt_hotel_uno > punt_hotel_tres))
print(orden + hotel_dos + hotel_tres + hotel_uno + str(punt_hotel_dos > punt_hotel_tres > punt_hotel_uno))

print(orden + hotel_tres + hotel_uno + hotel_dos + str(punt_hotel_tres > punt_hotel_uno > punt_hotel_dos))
print(orden + hotel_tres + hotel_dos + hotel_uno + str(punt_hotel_tres > punt_hotel_dos > punt_hotel_uno))
