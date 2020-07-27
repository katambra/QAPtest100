from volunteer_dict import volunteers


class Volunteer:
    def __init__(self, name="", surname="", city="", status=""):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def init_from_dict(self, volunteer_dict):

        self.name = volunteer_dict.get("name")
        self.surname = volunteer_dict.get("surname")
        self.city = volunteer_dict.get("city")
        self.status = volunteer_dict.get("status")


for vol in volunteers:
    vol_ = Volunteer()
    vol_.init_from_dict(vol)
    print(vol_.name, vol_.surname, ", г.", vol_.city, ", статус ", vol_.status)
