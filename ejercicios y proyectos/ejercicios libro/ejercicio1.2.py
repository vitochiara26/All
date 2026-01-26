"""Calcular un descuento del 25% para el precio de un curso y
mostrarle al usuario cuanto se ahorra y cuanto va a pagar"""

precio_curso = 109.89
precio_descuento = precio_curso * 0.25
descuento = precio_curso - precio_descuento

print(f"El precio del curso es de {precio_curso}$")
print(f"con el descuento de 25% te ahorras {descuento:.2f}$")
print(f"y pagarias por el curso solo {precio_descuento:.2f}$")
