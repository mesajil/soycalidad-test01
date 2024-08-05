import sys

def get_id(products, msg = 'Ingrese id del producto: '):
  """ Lee un id de producto """
  
  print()
  while True:
    try:
      id = int(input(msg))
      if (id not in products):
        print('ID no encontrado. Ingrese nuevamente.')
      else:
        return id
    except ValueError:
        print('ID inválido. Ingrese nuevamente.')
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        sys.exit()  # Termina el programa