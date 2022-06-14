product={"name":"kajal","brand":"lakme","price":"110","color":"black","offer_price":"110"}
print(product["brand"])
print(product["name"])
print(product["color"])
print(product["price"])

print("expire_date"in product)
product["expire_date"]=2022
print(product)
print(product["offer_price"])
product["offer_price"]=70
print(product)