"""
Este menu mostrara los productos adecuadamente formateados y las acciones:

=========================================
           Lista de Productos
=========================================
1        Pantalones         200.0      50
2        Camisas            120.0      45
3        Corbatas           50.0       30
4        Casacas            350.0      15
=========================================

[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
Elija opción:
"""

def show_menu(products = {}, options = {}):
  # Mostrar tabla de productos
  print()
  print_line()
  print(' '*13, 'Lista de Productos')
  print_line()
  for id, product in products.items():
    print(f'{id:>3}\t{product['name']:<18}{product['price']:<10}\t{product['stock']:<10}')
  print_line()

  # Mostrar menú de acciones
  print()
  for i, (id, option) in enumerate(options.items(), start=1):
    print(f"[{id}] {option['name']}", end='')
    # Imprimir separador si no es el último
    if (i != len(options)):
      print(', ', end='')
  print()

def print_line():
  print('='*45)