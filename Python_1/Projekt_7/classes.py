class Car:
    def __init__(self, color: str, cylinder: int, power: int):
        self.color = color
        self.cylinder = cylinder
        self.power = power
        self.pollution = {"body": 0, "wheel": 0}

    def show_pollution(self):
        print("---------- Pollution Status ----------")
        print(f"Karosserie: {self.pollution['body']}")
        print(f"Räder: {self.pollution['wheel']}")

    def run_offroad(self):
        self.pollution = {"body": 0.6, "wheel": 0.8}


class Ticket:
    def __init__(self, wash_wheel: bool, wash_body: bool):
        self.wash_wheel = wash_wheel
        self.wash_body = wash_body


class CarWash:
    def __init__(self):
        pass

    @staticmethod
    def wash(ticket: Ticket, car: Car):
        if ticket.wash_wheel == True:
            car.pollution = {"body": 0, "wheel": 0}
        if ticket.wash_body == True:
            car.pollution = {"body": 0, "wheel": 0}