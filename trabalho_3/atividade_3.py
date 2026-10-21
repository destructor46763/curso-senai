import json

livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"titulo": "Grande Sertão: Veredas", "autor": "João Guimarães Rosa", "ano": 1956},
]

texto_json = json.dumps(livros, ensure_ascii=False, indent=4)

print(texto_json)
print(type(texto_json))