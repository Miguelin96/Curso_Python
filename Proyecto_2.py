nombre = input("Cual es tu nombre: ")
ventas = input("Cuales han sido tus ventas: ")

venta_mas_comision = float(ventas) * 13/100

print(f"Estimado {nombre} tus comisiones este mes furon de: {round(venta_mas_comision)} €")