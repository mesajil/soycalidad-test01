from delete_product import eliminar
from create_product import agregar

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
    'fn': None,
    'type': None
  },
  4: {
    'name': 'Salir',
    'fn': None,
    'type': 'salir'
  }
}