# Se definen los objetos originales a utilizar

Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Se crea un objeto único para facilitar la programación y lectura:
# products = {
#   1: {
#     'name': 'Pantalones',
#     'price': 200.00,
#     'stock': 50
#   },
#   ...
# }

products = {}
for id, name in Productos.items():
  products[id] = {
    'name': name,
    'price': Precios[id],
    'stock': Stock[id]
  }
