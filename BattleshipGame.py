class BattleshipGame:
    def __init__(self, size=10, players=2):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = {}
        self.battlefield = [[' ' for _ in range(size)] for _ in range(size)]
        self.players = players

        self.ship_types = {
            1: {'class': 'Carrier', 'size': 5, 'coord': []},
            2: {'class': 'Battleship', 'size': 4, 'coord': []},
            3: {'class': 'Destroyer', 'size': 3, 'coord': []},
            4: {'class': 'Submarine', 'size': 3, 'coord': []},
            5: {'class': 'Patrol Boat', 'size': 2, 'coord': []}
        }

    def print_ships_info(self):
        ships_info = [
            {"No.": 1, "Class of ship": "Carrier", "Size": 5},
            {"No.": 2, "Class of ship": "Battleship", "Size": 4},
            {"No.": 3, "Class of ship": "Destroyer", "Size": 3},
            {"No.": 4, "Class of ship": "Submarine", "Size": 3},
            {"No.": 5, "Class of ship": "Patrol Boat", "Size": 2},
        ]

        # Print the header
        header = f"{'No.':<5} {'Class of ship':<20} {'Size':<5}"
        print(header)
        print("=" * len(header))

        # Print each ship's information
        for ship in ships_info:
            print(f"{ship['No.']:<5} {ship['Class of ship']:<20} {ship['Size']:<5}")
        print()

    def print_grid(self):
        """Prints the grid with the headers and the grid cells
        This is the grid that the player will see with their ships"""
        print('                 🛟 BATTLESHIP GRID 🛟')
        for row in range(self.size + 1):
            for col in range(self.size + 1):
                print('+' + '-' * 4, end='')
            print('+')
            for col in range(self.size + 1):
                if row == 0 and col == 0:
                    print('|' + ' ' * 4, end='')
                    for i in range(65, 65 + self.size):
                        print('|', chr(i), ' ', end='')
                    break
                if col == 0 and row != 0:
                    print('|', str(row).rjust(2) + ' ', end='')  #Ensures it is right justified with two characters
                else:
                    if row != 0:
                        print('|' + '  ' + self.grid[row - 1][col - 1] + ' ', end='') #Grid cells are 0-index; but grid cell is 1-indexed with the headers due to iteration. -1 adjusts for this
            print('|')
        for col in range(self.size + 1):
            print('+' + '-' * 4, end='')
        print('+')

    def battlefield_grid(self):
        """Prints the battlefield grid with the headers and the grid cells
        This is the grid that the player will see with their hits and misses"""
        print('                 🛟 BATTLESHIP GRID 🛟')
        for row in range(self.size + 1):
            for col in range(self.size + 1):
                print('+' + '-' * 4, end='')
            print('+')
            for col in range(self.size + 1):
                if row == 0 and col == 0:
                    print('|' + ' ' * 4, end='')
                    for i in range(65, 65 + self.size):
                        print('|', chr(i), ' ', end='')
                    break
                if col == 0 and row != 0:
                    print('|', str(row).rjust(2) + ' ', end='')  # Ensures it is right justified with two characters
                else:
                    if row != 0:
                        print('|' + '  ' + self.battlefield[row - 1][col - 1] + ' ',
                              end='')  # Grid cells are 0-index; but grid cell is 1-indexed with the headers due to iteration. -1 adjusts for this
            print('|')
        for col in range(self.size + 1):
            print('+' + '-' * 4, end='')
        print('+')

    def add_ship(self, name, coordinates):
        if self.players == 2:
            if not self.validate_ship_placement(coordinates):
                return False

            self.ships[name] = coordinates
            for (x, y) in coordinates: #Unpacks tuple
                self.grid[x][y] = name[0].upper()  #assigns tuple values into grid indices
            return True

        elif self.players == 1:
            if not self.bot_ship(coordinates):
                return False

            self.ships[name] = coordinates
            for (x, y) in coordinates:
                self.grid[x][y] = name[0].upper()
            return True

    def validate_ship_placement(self, coordinates):
        """Validates if ship coordinates are contiguous and within the grid"""
        # Extract x and y coordinates
        x_coords, y_coords = zip(*coordinates)
        x_set = set(x_coords)
        y_set = set(y_coords)

        # Check if all x coordinates or y coordinates are the same (forming a line)
        if len(x_set) == 1:  # All x coordinates are the same
            y_range = range(min(y_coords), max(y_coords) + 1)
            # Check if y coordinates are contiguous; set() removes duplicates; and checks if the set of y coordinates is equal to the range of y coordinates
            if not set(y_coords) == set(y_range):
                print(f'y_coords: {y_coords} are not contiguous')
                return False

        elif len(y_set) == 1:  # All y coordinates are the same
            x_range = range(min(x_coords), max(x_coords) + 1)
            if not set(x_coords) == set(x_range):
                print(f'x_coords: {x_coords} are not contiguous')
                return False
        else:
            print('Coordinates are not contiguous')
            return False

        # Check if coordinates are within the grid
        for (x, y) in coordinates:
            if not (0 <= x < self.size and 0 <= y < self.size):
                print("Invalid coordinates!")
                return False
            if self.grid[x][y] != ' ':
                print(f'Coordinates {x, y} are already occupied')
                return False

        return True


    def get_user_input(self):
        """Gets user input for ship placement"""
        for ship_no, ship_info in self.ship_types.items():
            name = ship_info['class']
            length = ship_info['size']
            dict_coordinates = ship_info['coord']
            # Produces an infinite loop until an exception occurs or a break. Allows for reattempts at placing ships
            while True:
                print(f'Placing {name} (size {length}):')
                coordinates = []
                for i in range(length):
                    while True:
                        coord = input(f"Enter coordinates for part {i + 1} (e.g., 'A5'): ")
                        if len(coord) < 2 or not coord[1:].isdigit():
                            print("Incorrect coordinates. Please enter a letter followed by a number (e.g., 'A5').")
                            continue
                        try:
                            y = ord(coord[0].upper()) - 65  # Convert 'A' to 0, 'B' to 1, etc.
                            x = int(coord[1:]) - 1
                            if not (0 <= y < self.size and 0 <= x < self.size):
                                raise ValueError
                            coordinates.append((x, y))
                            break
                        except ValueError:
                            print("Incorrect coordinates. Please enter valid coordinates within the grid (e.g., 'A5').")

                if self.add_ship(name, coordinates):
                    self.print_grid()
                    print("Ship placed successfully.")
                    for coordinate in coordinates:
                        dict_coordinates.append(coordinate)
                    break
                else:
                    print(f"Failed to place {name}. Please try again.")

    def check_hit(self):
        """Checks if missile hit or miss"""
        ships_total = 17
        missile_hit = 0
        missiles_shot = 0
        while missile_hit < ships_total:
            # Get user input, validate, and convert to coordinates
            while True:
                coord = input(f'Enter coordinates to attack! (e.g.,"A5"): ')
                if len(coord) < 2 or not coord[1:].isdigit():
                    print("Incorrect coordinates. Please enter a letter followed by a number (e.g., 'A5').")
                    continue
                try:
                    y = ord(coord[0].upper()) - 65  # Convert 'A' to 0, 'B' to 1, etc.
                    x = int(coord[1:]) - 1
                    if not (0 <= y < self.size and 0 <= x < self.size):
                        raise ValueError
                    coord_missile = (x, y)
                    break
                except ValueError:
                    print("Incorrect coordinates. Please enter valid coordinates within the grid (e.g., 'A5').")

            # Increment missile count for scoreboard
            missiles_shot += 1

            # Check if missile hit or miss
            if self.grid[x][y] == ' ':
                self.grid[x][y] = 'X'
                self.battlefield[x][y] = 'X'
                self.battlefield_grid()
                print('Miss! Try again!')
                continue
            elif self.grid[x][y] == 'X':
                print('Coordinate already used. It was a miss.')
                continue
            elif self.grid[x][y] == '☠':
                print('Coordinate already used. It was a hit.')
                continue

            # Check if missile hit or miss via iterating through ship coordinates
            for ship_id, ship_info in self.ship_types.items():
                for coord in ship_info['coord']:
                    if coord_missile == coord and self.grid[x][y] != '☠':
                        missile_hit += 1
                        self.battlefield[x][y] = '☠'
                        self.grid[x][y] = '☠'
                        self.battlefield_grid()
                        print(f'Ship {ship_info["class"]}, size: {ship_info["size"]}, has been hit! ')

                        ship_info['coord'].remove(coord)
                        if len(ship_info['coord']) == 0:
                            print(f'Ship {ship_info["class"]} has been destroyed! ')

                        break

        print('All ships have been destroyed. Mission complete.')
        return missiles_shot

    def random_ships(self):
        """Randomly places ships on the grid"""
        from random import randint, choice
        for ship_no, ship_info in self.ship_types.items():
            name = ship_info['class']
            length = ship_info['size']
            dict_coordinates = ship_info['coord']
            while True:
                orientation = choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    x = randint(0, self.size - 1)
                    y = randint(0, self.size - length)
                    coordinates = [(x, y + i) for i in range(length)]
                else:
                    x = randint(0, self.size - length)
                    y = randint(0, self.size - 1)
                    coordinates = [(x + i, y) for i in range(length)]

                if self.add_ship(name, coordinates):
                    for coordinate in coordinates:
                        dict_coordinates.append(coordinate)
                    break

    def bot_ship(self, coordinates):
        """Validates if ship coordinates are contiguous and within the grid"""
        # Extract x and y coordinates
        x_coords, y_coords = zip(*coordinates)
        x_set = set(x_coords)
        y_set = set(y_coords)

        # Check if all x coordinates or y coordinates are the same (forming a line)
        if len(x_set) == 1:  # All x coordinates are the same
            y_range = range(min(y_coords), max(y_coords) + 1)
            # Check if y coordinates are contiguous; set() removes duplicates; and checks if the set of y coordinates is equal to the range of y coordinates
            if not set(y_coords) == set(y_range):
                return False

        elif len(y_set) == 1:  # All y coordinates are the same
            x_range = range(min(x_coords), max(x_coords) + 1)
            if not set(x_coords) == set(x_range):
                return False
        else:
            return False

        # Check if coordinates are within the grid
        for (x, y) in coordinates:
            if not (0 <= x < self.size and 0 <= y < self.size):
                return False
            if self.grid[x][y] != ' ':
                return False

        return True





print('This is either a single player or double player battleship game. If you are playing solo, the computer will randomly place the ships for you to guess.\n')
print('If you are playing with two players, Player 1 will input the location of the ships, and Player 2 will guess the location of the ships.\n'
      'Then Player 2 will input their battleships and Player 1 will guess. The player with the least amount of missiles used wins! \n')

players = input('Would you like to play solo (1) or with two players (2) (1/2): ')
while True:
    if players == '1':
        print('You are playing solo. The computer will randomly place the ships for you to guess.\n')
        game1 = BattleshipGame(10, 1)
        game1.print_ships_info()
        game1.random_ships()
        game1.battlefield_grid()
        score = game1.check_hit()
        print(f'Missiles Used/End Score: {score}\n')
        break
    elif players == '2':
        game1 = BattleshipGame(10)
        game1.print_ships_info()
        game1.print_grid()
        game1.get_user_input()
        player2_score = game1.check_hit()
        print(f'Player 2 Missiles Used: {player2_score}\n')
        print('Player 2, it is now your turn to input your ships.\n')
        game2 = BattleshipGame(10)
        game2.print_ships_info()
        game2.print_grid()
        game2.get_user_input()
        player1_score = game2.check_hit()
        if player1_score < player2_score:
            print(f'Player 1 wins with only {player1_score} missiles used vs. Player 2 using {player2_score} missiles')
        else:
            print(f'Player 2 wins with only {player2_score} missiles used vs. Player 1 using {player1_score} missiles')
        break
    else:
        print('Invalid input. Please enter 1 or 2.\n')
        players = input('Would you like to play solo (1) or with two players (2) (1/2): ')
        continue