from defineproducts import products
from defineoptions import options
from showmenu import show_menu
from getoption import get_option

salir = False
while (not salir):
  # Leer opción
  show_menu(products, options)
  option_id = get_option(options)
  option = options[option_id]

  # Ejecutar opción
  if (option['type'] != 'salir'):
    # La opción elegida no es 'salir'
    option['fn'](products)
  else:
    # La opción elegida es 'salir'
    salir = True

# Imprimir mensaje de despedida
print('\nPrograma finalizado')
