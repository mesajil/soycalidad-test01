from delete_product import eliminar
from create_product import agregar
from update_product import actualizar

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