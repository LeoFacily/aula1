import string
import random

class Vehicle:

    def __init__(self, name, model):
        self.name = name
        self.model = model

class VehicleRegistry:

    def __init__(self, Vehicle):
        self.vehicle = Vehicle

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        first_section = id[:2]
        second_section = ''.join(random.choices(string.digits, k=2))
        third_section = ''.join(random.choices(string.ascii_uppercase, k=2))
        return f"{first_section}-{second_section}-{third_section}"

class VehicleType:

    def __init__(self,Vehicle):
        self.brand = Vehicle.name

    def define_price(self):
        if self.brand == 'Tesla Model 3':
            catalogue_price = 445000
        elif self.brand == 'Chevrolet Bold':
            catalogue_price = 317000
        elif self.brand == 'BMW i3':
            catalogue_price = 319950
        elif self.brand == 'Honda Civic LX':
            catalogue_price = 127900

        return catalogue_price

class tax_pay:

    tax_default = 0.05

    def __init__(self, model):
        self.model = model

    def tax_pay(self, price):

        if self.model == 'Elétrico':
            tax_default = 0.02

        # calcula a valor a ser pago
        payable_tax = tax_default * price
        return payable_tax

class Application:

    def register_vehicle(self, brand: string):

        carro1 = Vehicle('Tesla Model 3', 'Elétrico')
        registro1 = VehicleRegistry(carro1)
        veiculo1 = registro1.generate_vehicle_id(12)

        # gera um id com 12 caracteres
        vehicle_id = registro1.generate_vehicle_id(12)

        # gera a placa de baseado no id do veículo
        license_plate = registro1.generate_vehicle_license(vehicle_id)

        # determina o preco do veiculo
        catalogue_price = 0
        tipoVeiculo1 = VehicleType(carro1)
        print(tipoVeiculo1.define_price())
        tipo_veiculo_preco = tipoVeiculo1.define_price()
        tax = tax_pay(carro1.model)
        tax2 = tax.tax_pay(tipo_veiculo_preco)

        print(f'Marca: {carro1.name}')
        print(f'ID: {vehicle_id}')
        print(f'Placa: {license_plate}')
        print(f'Imposto a ser pago: {tax2}')


app = Application()
app.register_vehicle('Honda Civic LX')
