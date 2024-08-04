from get_new_product import get_new
from showmenu import show_table

def agregar(products):
  # Solicitar datos del nuevo producto
  product = get_new()
  
  # Confirmar acción
  new_id = len(products) + 1 # Nuevo id contiguo
  print('\nSe agregarán los siguientes productos:')
  show_table({new_id: product}, 'Producto nuevo')

  accept = input(f'\nConfirmar operación (y/n): ')
  if (accept != 'y'):
    # Mostrar mensaje de operación abortada
    print('\nAcción cancelada')
  else:
    # Agregar el nuevo producto
    products[new_id] = product

    # Mostrar mensaje de éxito
    print(f'\nSe ha creado un nuevo producto con id {new_id}')
  
  # Imprimir pausa
  input('\nPresione cualquier tecla para continuar ...')