def calcular_adicional(antiguedad, presentismo, edad):
    if 0.5 < antiguedad <= 2:
        adicional_antiguedad = 0.05
    elif 2 < antiguedad < 5:
        adicional_antiguedad = 0.10
    elif 5 <= antiguedad < 10:
        adicional_antiguedad = 0.15
    elif antiguedad >= 10:
        adicional_antiguedad = 0.20
    else:
        adicional_antiguedad = 0.00


    adicional_presentismo = 0.10 if presentismo > 95 else 0.00

    if edad >= 65:
        return 0

    return adicional_antiguedad + adicional_presentismo
