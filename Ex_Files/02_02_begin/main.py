greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"
doon = "max"

intrupution = f"Hello {name}"
disruption = f"Hii {doon}"

greet_format = "Hello {}"
greet_formats = "Hello p{}p jjjj" 

formatted = greet_format.format(name)
formattedext = greet_formats.format(doon)

print(intrupution, formatted)
print(formattedext)