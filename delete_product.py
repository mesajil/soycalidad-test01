from get_product_id import get_id

# Esta opción permite eliminar productos existentes. Para ello se deberá ingresar el id del producto a eliminar. Se mostrará mensaje con el nombre y id del producto para confirmar la eliminación.

def eliminar(products):
  # Obtener id del producto a eliminar
  id = get_id(products, 'Ingrese id del producto a eliminar: ') 

  # Confirmar acción
  accept = input(f'\nConfirmar eliminación (y/n): ')
  if (accept != 'y'):
    # Mostrar mensaje de operación abortada
    print('\nProceso cancelado')
  else:
    # Eliminar el producto
    del products[id]

    # Mostrar mensaje de eliminación correcta
    print(f'\nEl producto de id {id} ha sido eliminado correctamente')
    
  # Imprimir pausa
  input('\nPresione cualquier tecla para continuar ...')
