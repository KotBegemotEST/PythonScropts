#pip intall rich
from rich.console import Console
from rich.table import Table
from rich.text  import Text
import random

# console = Console()
# for i in range(5,0,-1):
#     console.log(f"[bold green]Allien will bea ttack your ship after {i} sec")
#     sleep(1)
# console.log("You are attacked")

console =  Console()

class CrewMember:
    # name,role,hp,power (rand0m),status
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.hp = 100
        self.power = random.randint(15,30)
        self.status = True


    def attack_allien():
        pass

    def injure():
        pass
    
class Alien:
    def __init__(self):
        self.aggression = random.randint(1,10)
        self.hp = 120   

    def attack():
        pass

    def is_alive():
        pass

# aggression, hp
class Ship:
    def __init__(self):
        self.rooms = ["Engine room","Medical block","Warehouse","Rest room","Navigation center"]
        self.status = True

    def trigger_alarm():
        pass

    def show_status():
        pass

#    status, rooms
class Misson:
    def __init__(self,crewList):
        self.crew = crewList
        self.alien = Alien()
        self.ship = Ship()

    def simulate():
        pass

    def summary(self):
        table = Table(title= "ekipaaž")
        table.add_column("Name", style='yellow')
        table.add_column("Role", style='green')
        table.add_column("Health", style='red')
        table.add_column("status", style='cyan')

        for crewMember in self.crew:
            if crewMember.status == False:
                status = "Died"
            else:
                 status = "Alive"
            table.add_row(crewMember.name, crewMember.role, str(crewMember.hp), status)
        console.print(table)

# crew, alien, ship

crew = [
    CrewMember("Ripli","Capitain"),
    CrewMember('Dallas', "Sailor"),
    CrewMember("Esh", "Science officer"),
    CrewMember("Parker", "Engineer")
]

mission1 = Misson(crew)
mission1.summary()