user = {
    'name': 'Lucas',
    'email': 'lcsavb@gmail.com',
    'age': 32
}

# Criando um objeto, boa prática primeira letra ser maiúscula:


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


obj_user = User('Lucas', 'lcsavb@gmail.com', 25)


class Lampada:

    def __init__(self, estado='apagado'):
        self.estado = estado

    def retornar_estado(self):
        return self.estado

    def esta_apagada(self):
        if self.estado == 'apagado':
            return True
        return False

    def pressionar_interruptor(self):
        if self.estado == 'apagado':
            self.estado = 'aceso'
        else:
            self.estado= 'apagado'


# os objetos são as lampadas 1 e 2


lampada1 = Lampada(estado='apagado')
print(lampada1.estado)
print(lampada1.esta_apagada())
# lampada1.acesa = True é melhor encapsular da seguinte forma:
lampada1.pressionar_interruptor()
print(lampada1.estado)
print(lampada1.esta_apagada())

lampada2 = Lampada()

print(lampada2.esta_apagada())

