from smartphone import Smartphone

Catalog = [
Smartphone(brand="Apple iPhone", model="3G", phone_number="+79165472239"),
Smartphone(brand="Samsung", model="Galaxy Note4", phone_number="+79158304511"),
Smartphone(brand="Infinix", model="Zero30 5G", phone_number="+79119256787"),
Smartphone(brand="Xiaomi", model="Redmi A2", phone_number="+79036115169"),
Smartphone(brand="Tecno", model="SPARK 20", phone_number="+79115259197")
]


for i in Catalog:
    i.sayPhone()
