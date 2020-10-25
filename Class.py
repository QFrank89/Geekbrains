class Auto:

    auto_color = ""
    auto_model = ""
    auto_year = -1
    auto_doors = -1

    def on_auto_start(self):
        print(f"Заводим автомобиль {self.auto_model}")

    def on_auto_stop(self):
        print("Остановка")

    def open_door(self, door):
        if door > self.auto_doors:
            print("Такая дверь не существует")
        elif door <= 0:
            print("Некорректный номер двери")
        else:
            print(f"Открылась дверь {door}")


toyota = Auto()
toyota.on_auto_start()
toyota.auto_color = "blue"
toyota.auto_model = "Toyota"
toyota.auto_year = "1999"
toyota.auto_doors = 2
toyota.open_door(3)
toyota.open_door(1)

vaz = Auto()
vaz.auto_color = "Red"
vaz.auto_model = "Vaz 2106"
vaz.auto_year = 1987
vaz.auto_doors = 4
vaz.open_door(2)


toyota.on_auto_start()
toyota.on_auto_stop()

vaz.on_auto_start()
vaz.on_auto_stop()