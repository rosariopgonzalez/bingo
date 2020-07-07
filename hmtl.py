from jinja2 import Template
from src.bingo import crear_carton

template = Template (open('plantilla.j2').read())

print(template.render(usuario="Ro"))

template = Template(open("web/plantilla.j2").read())
file = open ("bingo.html" , "w")
file.write(template.render(carton = crear_carton()))
file.close()
print ("Generando \"bingo.html\".")