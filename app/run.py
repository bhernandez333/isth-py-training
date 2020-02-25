from app.adaptor import file_routes as file
from app.domain.model import Usuario

print('Iniciando')
U = Usuario()
U.Username = "Usuario"
U.Nombre = "Nombre"
U.Apellido = "Apellido"
file.create_file("nombre.txt", U)