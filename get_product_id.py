def get_id(products, msg = 'Ingrese id del producto: '):
  """ Lee un id de producto """
  print()
  while True:
    id = int(input(msg))
    if (id not in products):
      print('ID inválido. Ingrese nuevamente.')
    else:
      return id