from  smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 14 Pro Max", "+79161234567")
phone2 = Smartphone("Samsung", "Galaxy S23 Ultra", "+79201234678")
phone3 = Smartphone("Xiaomi", "Mi 13 Pro", "+79341234789")
phone4 = Smartphone("Huawei", "P60 Pro", "+79451234890")
phone5 = Smartphone("OnePlus", "11 Pro", "+79561234901")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brend_phone} - {phone.phone_model}. {phone.subscriber_number}")