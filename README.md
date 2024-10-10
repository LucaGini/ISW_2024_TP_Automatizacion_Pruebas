# Cálculo de Adicionales al Sueldo - Automatización de Pruebas - ISW UTN ISI 2024 C402

Este proyecto consiste en un sistema que calcula el adicional al sueldo de los empleados de una empresa, basándose en la antigüedad, presentismo y edad de los empleados. Además, se incluyen pruebas automatizadas desarrolladas con **PyTest** para verificar el correcto funcionamiento del sistema.

## Descripción del Sistema

El sistema calcula el adicional del sueldo según las siguientes reglas:

1. **Antigüedad del empleado**:
   - Antigüedad de **0 a 0.5 años (6 meses)**: no le corresponde adicional por antiguedad.
   - Antigüedad de **0.5 a 2 años**: 5% adicional.
   - Antigüedad de **más de 2 años pero menos de 5**: 10% adicional.
   - Antigüedad de **5 a 10 años**: 15% adicional.
   - Antigüedad de **más de 10 años**: 20% adicional.

3. **Presentismo**:
   - Si el empleado tiene un presentismo **superior al 95%**, recibe un **10%** adicional, idependientemente a su antigüedad.

4. **Edad de jubilación**:
   - Si el empleado tiene **65 años o más**, no recibe ningún adicional.

## Archivos Principales

- **calcular_sueldo.py**: Contiene la lógica del sistema para calcular los adicionales al sueldo.
- **test_calcular_adicional.py**: Contiene las pruebas automatizadas para verificar el correcto cálculo del sistema.

## Requisitos

- Python 3.11+
- PyTest 8.3.3 o superior

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/LucaGini/ISW_2024_TP_Automatizacion_Pruebas.git

## Integrantes
- Luca Gini - luca.giniclc@gmail.com
- Luisina Gutierrez - luisinagutierrez2618@gmail.com
