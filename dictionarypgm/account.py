# account={"acno":1000,
#          "opening_date":"10-01-2019",
#          "type":"savings",
#          "pname":"ram"
#          }
#
# print(account["acno"])
# print("balance" in account)
# account["balance"]=500
# print(account)
# account["balance"]+=1000
# print(account)


mobile={
    "mobile_name":"redminote12pro",
    "display":"led",
    "price":45000
}
print(mobile.get("mobile_nam"))
print(mobile.get("display"))
print(mobile.get("price"))
print(mobile.get("mobile_name"))

# if "band" in mobile:
#     mobile["band"]="5g"
# else:
#     mobile["band"]="4g"
#
# mobile["price"]=mobile["price"]+1000 if mobile["price"]>4000 else 3000
# mobile["band"]
# print(mobile)


mobile["band"] = "5g" if "band" in mobile else "4g"
if mobile["price"] >40000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500
print(mobile)
