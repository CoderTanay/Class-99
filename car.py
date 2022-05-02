class Car(object):
    def __init__(self, model, brand, type, color, topSpeed):
        self.model=model
        self.brand=brand
        self.type=type
        self.color=color
        self.topSpeed=topSpeed
    def start(self):
        print('Started!')
    def stop(self):
        print('Stop!')
    def accelerate(self):
        print('Accelerating!')
    def changeGear(self):
        print('Changed Gear!')
Lamborghini = Car('Aventador', 'Lamborghini', 'Coupe', 'Green', '220')
print(Lamborghini.model)
Lamborghini.accelerate()