class Human:
    name = "Name"
    color_eyes = "Color_eyes"
    number_fingers = "10"

    def display_info_name(self):
        print("Hello, your name - ", self.name)

    def display_info_color_eyes(self):
        print("Your color of eyes - ", self.color_eyes)

    def display_info_fingers(self):
        print("Your number of fingers - ", self.number_fingers)


human1 = Human()
human1.name = "Daria"
human1.display_info_name()
human1.color_eyes = "brown"
human1.display_info_color_eyes()
human1.number_fingers = "8"
human1.display_info_fingers()

human2 = Human()
human2.name = "Laura"
human2.display_info_name()
human2.color_eyes = "blue"
human2.display_info_color_eyes()
human2.display_info_fingers()


class Pencils:
    names = "name"
    ink = "ink"

    def __init__(self, names, ink):
        self.names = names
        self.ink = ink

    def printer(self):
        print("Your name and ink - ", self.names, " and ", self.ink)


pencil1 = Pencils("Dasarus", "black")
pencil2 = Pencils("LeGaOl", "blue")

pencil2.printer()
