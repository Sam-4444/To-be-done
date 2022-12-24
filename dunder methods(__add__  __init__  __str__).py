
class a:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"this is the __str__ method ! {self.name}"

    def __add__(self, other):
        return f"this is __add__ method ! {self.age+other.age}"


p1 = a("Sam ", 44)
p2 = a("Max ", 22)

print(p1)
print(p1+p2)
