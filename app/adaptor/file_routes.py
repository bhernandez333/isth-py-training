# Empty
from flask import request, jsonify, make_response
from application import file_service


def get_file(nombre):
    result = file_service.get_file(nombre)


def create_file(nombre, contenido):
    result = file_service.post_file(nombre, contenido)
