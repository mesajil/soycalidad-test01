from defineproducts import products
from defineoptions import options
from showmenu import show_menu
from getoption import get_option

salir = False
while (not salir):
  # Leer opción
  show_menu(products, options)
  option = get_option(options)

  # Ejecutar opción
  option_type = options[option]['type']
  if (option_type != 'salir'):
    # La opción elegida no es 'salir'
    print('hello')
  else:
    # La opción elegida es 'salir'
    salir = True

# Imprimir mensaje de despedida
print()
print('Programa finalizado')
