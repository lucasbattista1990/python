#union de conjuntos

a = frozenset({1,2,3,4,5}) #no se puede modificar el conjunto
b = {4,5,6,7,8}
k = {1,2,3,4,5,6,7,8,9,10}


print(a)
print(b)

print("Union: ",a.union(b)) #union de conjuntos
print("k es un subconjunto de a?", a.issubset(k)) #subconjunto
print("el conjunto a no conparte nada con el conjunto k?",a.isdisjoint(k)) #no conparte
print("a es un superconjunto de k?",a.issuperset(k)) #superconjunto

c = a | b #union de conjuntos

print("Union: ",c) #union de conjuntos

d = {22,33,44,55,66} #conjunto
e = {44,55,66,77,88} #conjunto

f = d & e #interseccion de conjuntos
g = d - e #diferencia de conjuntos
h = d ^ e #diferencia simetrica de conjuntos

print("Diferencia simetrica",h)
print("Interseccion: ",f)
print("resta: ",g)