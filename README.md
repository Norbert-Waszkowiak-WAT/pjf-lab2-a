[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/y2ObC3O0)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15204041)
# pjf-lab2-a

Na podstawie ponizszego diagramu UML zaimplementuje klasy:
- Creature
- Human
- Bat
- Vampire
- Team
- Simulation

Modyfikuj wyłącznie plik `solution.py`.
![Diagram](../tmp/pjf-lab2-a/vampireExtendedWithSimulation.png)

### Dziedzinienie wielobazowe
W diagramie mamy doczynienia z dziedziczeniem wielobazowym, poniewaz klasa Vampire dziedziczy po klasach Human i Bat.

Podczas korzystania z dziedziczenia wielobazowego, należy zwrócić uwagę na kilka rzeczy:  
Kolejność dziedziczenia: Kolejność klas bazowych w definicji klasy jest ważna. Python szuka atrybutów i metod w klasach bazowych od lewej do prawej. To znaczy, jeśli dwie klasy bazowe mają metodę o tej samej nazwie, metoda z klasy, która jest wymieniona pierwsza, będzie miała pierwszeństwo.  
Wywoływanie konstruktorów klasy bazowej: Podczas korzystania z dziedziczenia wielobazowego, konstruktory klas bazowych nie są automatycznie wywoływane. Musisz wywołać je ręcznie. Możesz to zrobić za pomocą funkcji super(), która zwraca tymczasowy obiekt klasy bazowej, umożliwiając wywołanie jej metod. Pamiętaj, że super() odwołuje się do kolejności MRO (Method Resolution Order), więc może nie zawsze działać jak oczekiwano w przypadku dziedziczenia wielobazowego.  
Oto przykład dziedziczenia wielobazowego w Pythonie, gdzie klasa Vampire dziedziczy po klasach Human i Bat:
```python
class Human:
    def __init__(self, name):
        self.name = name

class Bat:
    def __init__(self, wing_span):
        self.wing_span = wing_span

class Vampire(Human, Bat):
    def __init__(self, name, wing_span):
        Human.__init__(self, name)
        Bat.__init__(self, wing_span)
```
W powyższym przykładzie, konstruktory klas Human i Bat są wywoływane ręcznie w konstruktorze klasy Vampire.

### Dodatkowe założenia

Zakładamy, że siła ataku:
- Bat = 5pkt, o 5pkt wiecej jeżeli wingSpan > 5 i o 5pkt wiecej jeżeli `flight_speed` > 5
- Human = 10pkt, 100pkt jeżeli occupation == `Soldier` i 5pkt jeżeli `born_year` > 2000
- Vampire = 15pkt, jeżeli atakuje klase Human i Human po ataku ma mniej niż 50% zdrowia to zwiększa swoje zdrowie o 10pkt

Maksymalne i początkowe zdrowie:
- Bat = 40pkt
- Human = 100pkt
- Vampire = 300pkt

Wszystkie wampiry urodziły się w 1900 roku

Atak drużyny A na drużynę B polega na tym, że każdy żywy członek drużyny A atakuje członka zwróconego przez metode `get_defender()` drużyny B
W symulacji `execute_round()` polega na tym, że drużyna A atakuje drużynę B, a następnie drużyna B atakuje drużynę A
Metoda `has_ended()` zwraca `True` jeżeli któraś z drużyn nie ma żywych członków
Metoda `execute()` wykonuje rundy symulacji aż do momentu zakończenia

### Testy jednostkowe
Testy są podzielone na nastepujące pliki:
- `test_human.py` - za 10pkt
- `test_bat.py` - za 10pkt
- `test_vampire.py` - za 10pkt
- `test_team.py` - za 25pkt
- `test_simulation.py` - za 15pkt
Łącznie 70pkt.

Aby uruchomić testy, wpisz w terminalu:
```bash
pytest
```
