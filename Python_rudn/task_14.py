'''
NKAbd-02-25, 10:56, Samir Galiev
Vol. 14, Task 2
Создаем класс про телевизоры
'''

class TV:
    def __init__(self, brand = "Unknown", diagonal = 0, IS4k = False, price =0.0):
        self.brand = brand 
        self.diagonal = diagonal 
        self.IS4k = IS4k
        self.price = price

    @classmethod
    def say_gex(cls, data_str): #TV из строки. Типо когда brand;диагональ там;блаблаблабла
        parts = data_str.split(';')
        brand = parts[0]
        diagonal = int(parts[1])
        IS4k = parts[2].lower() == 'true'
        price = float(parts[3])
        return cls(brand, diagonal, IS4k, price)
    
    @classmethod
    def bitch(cls, other):
        #Конструктор копирования
        return cls(other.brand, other.diagonal, other.IS4k, other.price)
    

    #геттеры и сеттеры 
    def beriPRICE(self):
        return self.price
    def zadaiPRICE(self, new_price):
        self.price = new_price
    
    def display(self): #вывод инфы о телевизоре 
            print(f"Brand: {self.brand}, Diagonal: {self.diagonal}\", "
              f"4K: {'Yes' if self.IS4k else 'Fuck off bitch >:P'}, Price: ${self.price:.2f}")

    #сравнение двух кирпичей
    def kakoe_govno_ti_kupil(self, other, consider_price=False):
        if self.diagonal != other.diagonal:
            return self.diagonal > other.diagonal 
        if self.IS4k != other.IS4k:
            return self.IS4k
        #если все одинаково, учитываем цену
        if consider_price:
            return self.price < other.price
        return False

if __name__ == "__main__":
    tv1 = TV()
    tv2 = TV("Samsung", 55, True, 700.0)
    tv3 = TV.bitch(tv2)

    tv4 = TV.say_gex("LG;65;True;900.0")

    print("TV1 (default): ")
    tv1.display()

    print("TV2 (custom): ")
    tv2.display()

    print("TV3 (copy of TV2):")
    tv3.display()

    print("TV4 (from string):")
    tv4.display()

    # Использование геттера и сеттера
    tv1.zadaiPRICE(299.99)
    print(f"\nTV1 new price: ${tv1.beriPRICE():.2f}")

    print("\nIs TV2 better than TV1 (size/4K only)?", tv2.kakoe_govno_ti_kupil(tv1))

    # Сравнение с учётом цены (эмуляция перегрузки)
    tv5 = TV("Sony", 55, True, 649.99)  # такой же, но дешевле
    print("TV5:")
    tv5.display()
    print("Is TV5 better than TV2 (considering price)?", tv5.kakoe_govno_ti_kupil(tv2, consider_price=True))




    