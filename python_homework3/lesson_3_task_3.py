from address import Address
from mailing import Mailing

address1 = Address("123456", "Moscow", "Tverskaya", 1, 15 )
address2 = Address("555676", "St.Petersburg", "Komsomola", 18, 9 )

mailing1 = Mailing(address1, address2, 2750, "FN9580588LX")

print ("Отправление ", mailing1.track, "из", mailing1.from_address.index, mailing1.from_address.city, 
      mailing1.from_address.street, mailing1.from_address.house, "-", mailing1.from_address.appartment, "в", mailing1.to_address.index, mailing1.to_address.city, 
      mailing1.to_address.street, mailing1.to_address.house, "-", mailing1.to_address.appartment, ".", "Стоимость: ", mailing1.cost, "рублей.")