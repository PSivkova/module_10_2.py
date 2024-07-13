from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        for j in range(5):
            enemy -= self.power
            print(f'{self.name}: сражается {j+1} день(дня)..., осталось {enemy} воинов.'+'\n')
        print(f'{self.name} одержал победу спустя {j+1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
