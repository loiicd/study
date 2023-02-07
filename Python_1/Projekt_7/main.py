from classes import *

car = Car(color="black", cylinder=4, power=220)
car.run_offroad()
car.show_pollution()
wash_ticket = Ticket(wash_wheel=True, wash_body=True)
car_wash_garage = CarWash()
car_wash_garage.wash(ticket=wash_ticket, car=car)
car.show_pollution()