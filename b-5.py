class Chair:

    def __init__(self, legs, material, shape):
        self.legs = legs
        self.material = material
        self.shape = shape

    def __str__(self):
        return f'количество ножек: {self.legs}, материал: {self.material}, форма:  {self.shape}'

    def __repr__(self):
        return f'количество ножек: {self.legs}, материал: {self.material}, форма:  {self.shape}'


Chair1 = (4, "дерево", "квадрат")
print(Chair1)
print([Chair1])