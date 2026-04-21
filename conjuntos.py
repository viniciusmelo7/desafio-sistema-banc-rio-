carros = set(["palio", "gol", "uno", "celta", "gol", "onix"])
print(carros)

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")


linguagens = {"python", "java", "c++", "python", "javascript"}
print(linguagens)

conjunto_a = {1,2}
conjunto_b = {2,3}
print(conjunto_a.union(conjunto_b)) # {1, 2, 3}
print(conjunto_a.intersection(conjunto_b)) # {2}
print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 3}

print(conjunto_a.issubset(conjunto_b)) # False
print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_a.isdisjoint(conjunto_b)) # False
print(conjunto_a.isdisjoint({3,4})) # True

sorteio = {1, 23}
print(sorteio.add(1))