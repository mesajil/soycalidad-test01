from defineproducts import products
from defineoptions import options
from showmenu import show_menu
from getoption import get_option

salir = False
while (not salir):
  show_menu(products, options)
  option = get_option(options)
  print(option)
  salir = True