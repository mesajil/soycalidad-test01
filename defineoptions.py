from delete_product import eliminar
from create_product import agregar
from update_product import actualizar

"""
Contiene información relevante de la opciones del menú. Contiene:

  - id de la opción
  - name: el nombre de la opción
  - fn: la función a ejecutar
  - type: Indica el tipo de opción. Por ejemplo, 'salir' para indicar que la opción termina el programa.
"""

options = {
  1: {
    'name': 'Agregar',
    'fn': agregar,
    'type': None
  },
  2: {
    'name': 'Eliminar',
    'fn': eliminar,
    'type': None
  },
  3: {
    'name': 'Actualizar',
    'fn': actualizar,
    'type': None
  },
  4: {
    'name': 'Salir',
    'fn': None,
    'type': 'salir'
  }
}