customer_1 = {"name": "Dalton","Age": 12}
customer_2 = {"name": "Dalton","Age": 12,"eyes": "Blue"}
print customer_1 
print customer_2
print type (customer_1)
print customer_1.keys()
print customer_1.values()
print customer_1.items()
print customer_1["name"]
print customer_1.items()[0]
if "eyes" in customer_2: 
	print customer_2["eyes"]
else:
	print "Nope chuck-Testa"