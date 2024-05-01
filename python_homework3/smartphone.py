class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def sayPhone(self):
        print("[Марка телефона: ", self.brand)
        print("Модель телефона: ", self.model)
        print("Абонентский номер: ", self.phone_number, "]")

