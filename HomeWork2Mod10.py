from time import sleep
from threading import Thread
from random import randint

class Knights(Thread):
    def __init__(self, name, skill, enemy_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemy_num = enemy_num
        print(f"Имя: {self.name}, умение: {self.skill}")

    def run(self):
        count = 0
        while self.enemy_num > 0:
            self.enemy_num -= self.skill
            count += 1

            if self.enemy_num < 0:
                self.enemy_num = 0
            print(f"{self.name}, день битвы {count}: осталось {self.enemy_num} врагов")
            sleep(1)

knight1 = Knights("Рыцарь1", randint(1,100), 100)
knight2 = Knights("Рыцарь2", randint(1,100), 100)

print("Сражение началось")
knight1.start()
knight2.start()

knight1.join()
knight2.join()
print("Битва окончена")
