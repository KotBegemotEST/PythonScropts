# from rich.console import Console
# from rich.table import Table
# from rich.text import Text
# import random
# import time

# console = Console()

# class Taxi:
#     def __init__(self, driver, model):
#         self.driver = driver
#         self.model = model
#         self.speed = random.randint(100, 180)
#         self.status = "Готов к гонке!"

#     def drive(self):
#         console.log(f"[cyan]{self.driver} выезжает на {self.model} со скоростью {self.speed} км/ч...[/]")
#         time.sleep(1)

#     def drift(self):
#         result = random.choice(["удачно", "почти перевернулся", "взорвал светофор"])
#         console.log(f"[magenta]{self.driver} делает дрифт: {result}![/]")
#         time.sleep(1)

#     def show_info(self):
#         table = Table(title="🚕 Инфо о такси")

#         table.add_column("Водитель", style="bold yellow")
#         table.add_column("Модель", style="green")
#         table.add_column("Скорость", style="red")
#         table.add_column("Статус", style="cyan")

#         table.add_row(self.driver, self.model, f"{self.speed} км/ч", self.status)
#         console.print(table)

# # === Симуляция ===
# taxi1 = Taxi("Даниэль", "Peugeot 406")
# taxi2 = Taxi("Эмильен", "Renault Clio")

# taxi1.show_info()
# taxi2.show_info()

# console.print("\n[bold]🏁 Начинается гонка![/bold]\n")
# time.sleep(1)

# for taxi in [taxi1, taxi2]:
#     taxi.drive()
#     taxi.drift()

# console.print("\n[bold green]Гонка завершена! Кто победил — решать зрителям![/bold green]")
from rich.console import Console
from rich.table import Table
import random
import time

console = Console()

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.health = 100
        self.power = random.randint(15, 30)
        self.alive = True

    def injure(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            self.health = 0
            console.log(f"[red]{self.name} ({self.role}) был убит Чужим![/]")
        else:
            console.log(f"[yellow]{self.name} ({self.role}) получил {damage} урона! Осталось {self.health} HP.[/]")

    def attack_alien(self, alien):
        if not self.alive:
            return
        damage = self.power + random.randint(-5, 5)
        alien.health -= damage
        if alien.health < 0:
            alien.health = 0
        console.log(f"[bold green]{self.name} атакует Чужого и наносит {damage} урона![/]")
        time.sleep(0.5)

class Alien:
    def __init__(self):
        self.aggression = random.randint(1, 10)
        self.health = 120

    def attack(self, crew: CrewMember):
        damage = random.randint(15, 40) + self.aggression * 2
        crew.injure(damage)

    def is_alive(self):
        return self.health > 0

class Ship:
    def __init__(self):
        self.status = "Все системы работают"
        self.rooms = [
            "Машинное отделение",
            "Навигационный центр",
            "Медблок",
            "Склад",
            "Комната отдыха"
        ]

    def trigger_alarm(self, room):
        self.status = f"🚨 Обнаружено присутствие Чужого в локации: {room}!"
        console.log(f"[bold red]{self.status}[/]")

    def show_status(self):
        console.print(f"[blue]Статус корабля:[/] {self.status}")

class Mission:
    def __init__(self, crew_list):
        self.crew = crew_list
        self.alien = Alien()
        self.ship = Ship()

    def simulate(self):
        console.print("\n[bold green]🚀 Миссия начинается![/bold green]\n")
        self.ship.show_status()
        time.sleep(1)

        for round in range(1, 6):
            if not self.alien.is_alive():
                console.print("\n[bold green]🎉 Экипаж победил Чужого![/bold green]")
                break

            console.print(f"\n[bold]Раунд {round}:[/bold]")
            room = random.choice(self.ship.rooms)
            console.log(f"[cyan]📡 Сканирование помещения: {room}...[/]")
            time.sleep(1)

            if random.random() < 0.7 and self.alien.is_alive():
                self.ship.trigger_alarm(room)

                alive_crew = [c for c in self.crew if c.alive]
                if not alive_crew:
                    break

                victim = random.choice(alive_crew)
                self.alien.attack(victim)

                attackers = [c for c in self.crew if c.alive and c != victim]
                if attackers:
                    attacker = random.choice(attackers)
                    attacker.attack_alien(self.alien)
                    console.log(f"[bold cyan]У Чужого осталось {self.alien.health} HP.[/]")
            else:
                console.log("[green]Скан чист. Экипаж дышит спокойно.[/]")

            if not any(c.alive for c in self.crew):
                console.print("\n[bold red]☠️ Весь экипаж уничтожен. Миссия провалена.[/bold red]")
                return

            time.sleep(1)

        if self.alien.is_alive():
            console.print("\n[bold red]👽 Чужой выжил. Миссия под угрозой![/bold red]")

        console.print("\n[bold cyan]📋 Итоги миссии:[/bold cyan]")
        self.summary()

    def summary(self):
        table = Table(title="🧑‍🚀 Экипаж")
        table.add_column("Имя", style="yellow")
        table.add_column("Роль", style="green")
        table.add_column("Здоровье", style="red")
        table.add_column("Статус", style="cyan")

        for c in self.crew:
            status = "🟢 Жив" if c.alive else "🔴 Погиб"
            table.add_row(c.name, c.role, str(c.health), status)

        console.print(table)

# === Запуск миссии ===
crew = [
    CrewMember("Рипли", "Капитан"),
    CrewMember("Даллас", "Штурман"),
    CrewMember("Эш", "Офицер науки"),
    CrewMember("Паркер", "Инженер"),
]

mission = Mission(crew)
mission.simulate()
