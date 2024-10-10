import pytest
from calcular_sueldo import calcular_adicional

# Pruebas por tablas de decisión
def test_tablas_decision():
    # Caso 1: Antigüedad de 1 año, presentismo de 96%, edad 30 (5% por antigüedad + 10% por presentismo)
    assert round(calcular_adicional(1, 96, 30), 2) == 0.15
    
    # Caso 2: Antigüedad de 4 años, presentismo de 90%, edad 40 (10% por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(4, 90, 40), 2) == 0.10
    
    # Caso 3: Antigüedad de 7 años, presentismo de 100%, edad 45 (15% por antigüedad + 10% por presentismo)
    assert round(calcular_adicional(7, 100, 45), 2) == 0.25
    
    # Caso 4: Antigüedad de 11 años, presentismo de 85%, edad 50 (20% por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(11, 85, 50), 2) == 0.20
    
    # Caso 5: Antigüedad de 0.4 años, presentismo de 85%, edad 50 (sin adicional por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(0.4, 85, 50), 2) == 0.00
    
    # Caso 6: Antigüedad de 1 año, presentismo de 85%, edad 50 (5% por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(1, 85, 50), 2) == 0.05
    
    # Caso 7: Antigüedad de 3 años, presentismo de 98%, edad 50 (10% por antigüedad, con adicional por presentismo)
    assert round(calcular_adicional(3, 98, 50), 2) == 0.20
    
    # Caso 8: Antigüedad de 8 años, presentismo de 85%, edad 50 (15% por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(8, 85, 50), 2) == 0.15
    
    # Caso 9: Antigüedad de 11 años, presentismo de 97%, edad 50 (20% por antigüedad, con adicional por presentismo)
    assert round(calcular_adicional(11, 97, 50), 2) == 0.30
    
    # Caso 10: Antigüedad de 0.4 años, presentismo de 96%, edad 50 (sin adicional por antigüedad, con adicional por presentismo)
    assert round(calcular_adicional(0.4, 96, 50), 2) == 0.10
    
    # Caso 11 (jubilado): Antigüedad de 26 años, presentismo de 85%, edad 67 (sin adicional por antigüedad, sin adicional por presentismo)
    assert round(calcular_adicional(26, 85, 67), 2) == 0.00

# Pruebas por valores límite
def test_valores_limite():
    # 0 < antigüedad <= 0.5
    assert round(calcular_adicional(0, 94, 30), 2) == 0.00  # 0% antigüedad
    assert round(calcular_adicional(0.5, 94, 30), 2) == 0.00  # 0% antigüedad
    assert round(calcular_adicional(0.583, 94, 30), 2) == 0.05  # 7 meses - 5% antigüedad
    
    # 0.5 < antigüedad <= 2
    assert round(calcular_adicional(2, 94, 30), 2) == 0.05  # 5% antigüedad
    assert round(calcular_adicional(3, 94, 30), 2) == 0.10  # 10% antigüedad
    
    # 2 < antigüedad < 5
    assert round(calcular_adicional(4, 94, 30), 2) == 0.10  # 10% antigüedad

    # 5 <= antigüedad < 10
    assert round(calcular_adicional(5, 94, 30), 2) == 0.15  # 15% antigüedad
    assert round(calcular_adicional(9, 94, 30), 2) == 0.15  # 15% antigüedad
    
    # 10 <= antigüedad
    assert round(calcular_adicional(10, 94, 30), 2) == 0.20  # 20% antigüedad
    
    # Presentismo 
    assert round(calcular_adicional(4, 96, 30), 2) == 0.20  # 10% antigüedad + 10% presentismo
    assert round(calcular_adicional(4, 95, 30), 2) == 0.10  # 10% antigüedad

    # Jubilación
    assert round(calcular_adicional(10, 100, 65), 2) == 0.00  # No hay adicional si ya tiene 65 años
    assert round(calcular_adicional(10, 100, 64), 2) == 0.30  # Adicional antigüedad + presentismo
