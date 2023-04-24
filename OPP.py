class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices
        
    def total_price(self,prices):
        return sum(prices)

prices = [5, 10, 15, 20, 25]
cart = ShoppingCart(prices)
total = cart.total_price()
print(total)
