class Shop:
    def __init__(self) -> None:
        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def buy_product(self,find_product,quantity):
        for product in self.products:
            product.quantity=product.quantity-quantity
            if find_product ==product.name and quantity<=product.quantity:
                return f'congratulation! you brought {quantity} {product.name}'
            else:
                return f'{find_product} is not available in our shop'

class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity

ryans=Shop()
mouse=Product('mouse',150,5)
keyboard=Product('keyboard',650,10)
sound_box=Product('sound_box',1600,8)
ryans.add_product(mouse)
ryans.add_product(keyboard)
ryans.add_product(sound_box)

print(ryans.buy_product('mouse',2))
print(ryans.buy_product('mouse',4))
print(ryans.buy_product('ram',2))
