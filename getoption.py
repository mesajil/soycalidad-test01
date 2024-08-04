""" Retorna la opción del menú. Itera cuantas veces sea necesario para obtener un valor de opción válido. """

def get_option(options = {}):
  option = None
  print()
  while (True):
    option = int(input('Elija opción: '))
    if (option not in options):
      print('Opción inválida. Ingrese nuevamente.')
    else:
      return option
