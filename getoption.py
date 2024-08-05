
def get_option(options = {}):
  """ Obtiene y retorna la opción elegida por el usuario """
  
  option = None
  print()
  while (True):
    option = int(input('Elija opción: '))
    if (option not in options):
      print('Opción inválida. Ingrese nuevamente.')
    else:
      return option
