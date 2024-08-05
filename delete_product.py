from get_product_id import get_id

def eliminar(products):
  """ Eliminar un producto de la base de datos """

  # Obtener id del producto a eliminar
  id = get_id(products, 'Ingrese id del producto a eliminar: ') 

  # Confirmar acción
  accept = input(f'\nConfirmar eliminación (y): ')
  if (accept != 'y'):
    # Mostrar mensaje de operación abortada
    print('\nProceso cancelado')
  else:
    # Eliminar el producto
    del products[id]

    # Mostrar mensaje de eliminación correcta
    print(f'\nEl producto de id {id} ha sido eliminado correctamente')

