import random

class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.hits = []

    def hit(self, coordinate):
        if coordinate in self.coordinates and coordinate not in self.hits:
            self.hits.append(coordinate)
            return True
        return False

    def is_sunk(self):
        return len(self.hits) == len(self.coordinates)


class Board:
    def __init__(self, ships):
        self.ships = ships
        self.shots = []
        self.board = [['О' for _ in range(6)] for _ in range(6)]

    def shoot(self, coordinate):
        if coordinate in self.shots:
            raise ValueError("Вы уже стреляли в эту клетку!")
        if not (1 <= coordinate[0] <= 6 and 1 <= coordinate[1] <= 6):
            raise ValueError("Координаты выстрела должны быть в пределах игрового поля!")
        self.shots.append(coordinate)
        for ship in self.ships:
            if ship.hit(coordinate):
                if ship.is_sunk():
                    print("Корабль потоплен!")
                self.board[coordinate[0]-1][coordinate[1]-1] = 'X'
                return True
        self.board[coordinate[0]-1][coordinate[1]-1] = 'T'
        return False

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))


def generate_ships():
    # Здесь вы можете добавить свою логику генерации кораблей
    ships = []
    for _ in range(4):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        ships.append(Ship([(x, y)]))
    return ships


def play_game():
    player_ships = generate_ships()
    computer_ships = generate_ships()

    player_board = Board(player_ships)
    computer_board = Board(computer_ships)

    while True:
        player_board.print_board()
        x = int(input("Введите координату x: "))
        y = int(input("Введите координату y: "))
        try:
            hit = player_board.shoot((x, y))
            if hit:
                print("Попадание!")
            else:
                print("Промах!")
        except ValueError as e:
            print(e)

        x = random.randint(1, 6)
        y = random.randint(1, 6)
        computer_board.shoot((x, y))

        if all(ship.is_sunk() for ship in player_ships):
            print("Компьютер выиграл!")
            break
        elif all(ship.is_sunk() for ship in computer_ships):
            print("Вы выиграли!")
            break


if __name__ == "__main__":
    play_game()
