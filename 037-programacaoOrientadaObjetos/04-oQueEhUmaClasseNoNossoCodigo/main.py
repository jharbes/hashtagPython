class Pessoa:
    def __init__(self,name,age,weight) -> None:
        self.name=name
        self.age=age
        self.weight=weight

jorge=Pessoa('Jorge Nami Harbes',39,86.0)

print(jorge) # <__main__.Pessoa object at 0x0000026BC981FC10>
print(jorge.__class__) # <class '__main__.Pessoa'>
print(jorge.__class__.__name__) # Pessoa

print(jorge.__dict__) # {'name': 'Jorge Nami Harbes', 'age': 39, 'weight': 86.0}
print(vars(jorge)) # {'name': 'Jorge Nami Harbes', 'age': 39, 'weight': 86.0}