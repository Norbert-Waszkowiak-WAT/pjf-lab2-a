class Creature:
    def __init__(self, name, max_health):
        self._name = name
        self._max_health = max_health
        if isinstance(self, Vampire):
            self._health = 300
        else:
            self._health = max_health

    def decrease_health(self, amount) -> None:
        if amount > 0:
            if self._health < amount:
                self._health = 0
            else:
                self._health -= amount
        else:
            if self._max_health < self._health - amount:
                self._health = self._max_health
            else:
                self._health -= amount

    def get_health(self) -> int:
        return self._health

    def get_max_health(self) -> int:
        return self._max_health
    
    def get_health_percent(self) -> float:
        return self._health / self._max_health * 100
    
    def is_alive(self) -> bool:
        if self._health > 0:
            return True
        else:
            return False
    
    def attack(self, attacked_creature):
        pass

class Human(Creature):
    def __init__(self, name, occupation, born_year):
        Creature.__init__(self, name, 100)
        self._occupation = occupation
        self._born_year = born_year

    def get_occupation(self) -> str:
        return self._occupation

    def get_birth_year(self) -> int:
        return self._born_year

    def attack(self, attacked_creature):
        damage = 10
        if self._occupation == "Soldier":
            damage = 100
        if self._born_year > 2000:
            damage = 5
        attacked_creature.decrease_health(damage)

class Bat(Creature):
    def __init__(self, name, wing_span, flight_speed):
        Creature.__init__(self, name, 40)
        self._wing_span = wing_span
        self._flight_speed = flight_speed

    def get_fly_speed(self) -> int:
        return self._flight_speed

    def get_wing_span(self) -> int:
        return self._wing_span
    
    def change_flight_speed(self, speed: int) -> None:
        self._flight_speed = speed

    def attack(self, attacked_creature):
        damage = 5
        if self._wing_span > 5:
            damage += 5
        if self._flight_speed > 5:
            damage += 5
        attacked_creature.decrease_health(damage)

class Vampire(Human, Bat):
    def __init__(self, name, occupation, wing_span, flight_speed):
        Human.__init__(self, name, occupation, 1900)
        Bat.__init__(self, name, wing_span, flight_speed)
        self._max_health = 300

    def attack(self, attacked_creature):
        damage = 15
        attacked_creature.decrease_health(damage)
        if isinstance(attacked_creature, Human):
            if attacked_creature.get_health_percent() < 50.0:
                self.decrease_health(-10)

class Team():
    def __init__(self):
        self._creatures = []

    def add(self, creature: Creature) -> None:
        self._creatures.append(creature)
    
    def get_alive_members(self):
        pass

    def get_defender(self) -> Creature:
        pass

    def attack(self, other_team) -> None:
        pass

    def is_at_least_one_alive_member(self) -> bool:
        pass

class Simulation():
    def __init__(self, team_A, team_B):
        self._teamA = team_A
        self._teamB = team_B
    
    def execute_round(self) -> None:
        pass

    def has_ended(self) -> bool:
        pass

    def execute(self) -> None:
        pass
    
    def get_winner(self) -> Team:
        pass
