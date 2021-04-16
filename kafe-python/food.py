from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ': Rp' + str(self.price) + ' (' + str(self.calorie_count) + 'kCal)'
    
    def calorie_info(self):
        print('kCal: ' + str(self.calorie_count))
