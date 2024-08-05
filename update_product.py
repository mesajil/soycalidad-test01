from showmenu import show_table
from get_product_id import get_id


def actualizar(products):
  """ Script para actualizar un producto existente en la base de datos """

  # Imprimir un mensaje informativo para actualizar un producto
  print_message()

  # Solicitar id del producto a actualizar
  id = get_id(products, 'Ingrese id del producto a actualizar: ') 

  # Solicitar datos a actualizar
  product = input_updated_product(products[id].copy())
  
  # Confirmar acción
  print('\nSe actualizará el siguiente producto:')
  show_table({id: product}, 'Datos a actualizar')

  accept = input(f'\nConfirmar operación (y): ')
  if (accept != 'y'):
    # Mostrar mensaje de operación abortada
    print('\nAcción cancelada')
  else:
    # Actualizar el producto
    products[id] = product

    # Mostrar mensaje de éxito
    print(f'\nSe ha actualizado el producto con id {id}')


def input_updated_product(product):
  # Actualizar nombre si es válido
  name = get_name()
  if (name):
    product['name'] = name
  
  # Actualizar precio si es válido
  price = get_price()
  if (price != None):
      product['price'] = price
  
  # Actualizar stock si es válido
  stock = update_stock(product['stock'])

  if (stock != None):
    product['stock'] = stock
  
  return product


def get_name():

  # Obtener y enviar nombre válido
  print()
  while True:
    # Leer un nombre no vacío
    name = input('Ingrese el nombre del producto: ')
    
    # Retornar None en caso se haya presionado Enter
    if not name:
      return

    # Validar nombre
    name = name.strip() # Eliminar espacios en blanco al inicio y final
    if name:
        return name
    else:
        print('El nombre no puede estar vacío. Por favor, ingrese un nombre válido.')


def get_price():
  print()
  while True:
    # Leer entrada
    precio = input('Ingrese el precio del producto: ')
    
    # Retornar None en caso se haya presionado Enter
    if not precio:
      return
    
    # Validar precio
    try:
      return float(precio)
    except:
      print('Entrada inválida. Por favor, ingrese un número.')


def update_stock(original_stock):
  print()
  while True:
    # Leer entrada
    data = input('Ingrese el stock del producto: ')

    # Retornar None en caso se haya presionado Enter
    if not data:
      return
    
    # Validar stock
    try:
      # Leer primer caracter 
      prefix = data[0]

      # Resolver stock dependiendo del valor del prefijo
      stock = None
      if (prefix in ['+', '-']):
        units = int(data[1:].strip()) # Unidades a restar o sumar al stock
        stock = original_stock + units if prefix == '+' else original_stock - units
      else:
        # Si no hay prefijo alguno entonces se retorna el valor
        stock = int(data.strip())
      
      # Aceptar números no negativos
      if (stock >= 0):
        return stock
      else:
        print('El stock resultante es negativo. Por favor, ingrese nuevamente.')

    except:
      print('Entrada inválida. Por favor, ingrese un número entero.')


def print_message():
  # Imprimir un mensaje informativo para actualizar un producto
  msg = '''
  |-------------------------------------------------------------------------|
  |                          ACTUALIZAR PRODUCTO                            |
  |                                                                         |
  |  1)  Presione enter en caso no desee actualizar un campo específico.    |
  |                                                                         |
  |  2)  Para actualizar el stock de un producto usted podrá utilizar los   |
  |      prefijos de suma o resta, o simplemente ingresar el nuevo valor:   |
  |                                                                         |
  |      1. Prefijo (+): Para sumar stock al actual. Por ejemplo: +30       |
  |      2. Prefijo (-): Para restar stock al actual. Por ejemplo: -2       |
  |      3. Sin prefijo: Para reemplazar el stock actual. Por ejemplo: 260  |
  |-------------------------------------------------------------------------|'''
  print(msg)