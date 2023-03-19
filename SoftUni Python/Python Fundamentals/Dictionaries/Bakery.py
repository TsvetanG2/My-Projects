products = {}
data = input().split()

for index in range(0, len(data), 2): #започваме от 1вият индекс и вървим през 2
    key = (data[index])
    value = int(data[index+1])
    # Трябват да бъдат интегер навсякъде, може да се сложи отдолу int(value), но е по-добре да се
    # превърнат в интегер навсякъде, за това го слагаме горе
    products[key] = value

print(products)
