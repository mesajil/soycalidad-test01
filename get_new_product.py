def get_new():
  """ Obtiene los datos de un producto nuevo a través de un formulario """

  return {
    'name': get_name(),
    'price': get_price(),
    'stock': get_stock()
  }


def get_name():
  print()
  while True:
    # Leer un nombre no vacío
    name = input('Ingrese el nombre del producto: ').strip()
    if name:
        return name
    else:
        print('El nombre no puede estar vacío. Por favor, ingrese un nombre válido.')


def get_price():
  print()
  while True:
    # Leer un número
    try:
      return float(input('Ingrese el precio del producto: '))
    except:
      print('Entrada inválida. Por favor, ingrese un número.')


def get_stock():
  print()
  while True:
    # Leer un número
    try:
      return int(input('Ingrese el stock del producto: '))
    except:
      print('Entrada inválida. Por favor, ingrese un número entero.')