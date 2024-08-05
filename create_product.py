from get_new_product import get_new
from showmenu import show_table

def agregar(products = {}):
  """ Script para agregar un nuevo producto """
  
  # Solicitar datos del nuevo producto
  product = get_new()
  
  # Definir el id del nuevo producto
  if products:
      new_id = max(products.keys()) + 1  # Obtiene el id maximo en la lista y le suma 1
  else:
      new_id = 1  # Caso cuando no hay productos

  # Mostrar el producto a agregar
  print('\nSe agregarán los siguientes productos:')
  show_table({new_id: product}, 'Producto nuevo')

  # Confirmar acción
  accept = input(f'\nConfirmar operación (y): ')
  if (accept != 'y'):
    # Mostrar mensaje de operación abortada
    print('\nAcción cancelada')
  else:
    # Agregar el nuevo producto
    products[new_id] = product

    # Mostrar mensaje de éxito
    print(f'\nSe ha creado un nuevo producto con id {new_id}')
