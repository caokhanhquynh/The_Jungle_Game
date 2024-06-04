import pygame

pygame.init()

WIDTH = 350
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Jungle Chess!')
medium_font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# game cariables and images
blue_animals = ['elephant', 'lion', 'tiger', 'leopard','wolf', 'dog', 'cat', 'mouse']
blue_locations = [(6,2), (0,0), (6,0), (2,2), (4,2), (5,1), (1,1), (0,2)]

red_animals = ['elephant', 'lion', 'tiger', 'leopard','wolf', 'dog', 'cat', 'mouse']
red_locations = [(0,6), (6,8), (0,8), (4,6), (2,6), (5,7), (1,7), (6,6)]

protected_cave = [(2,0), (3,1), (4,0), (3,7), (2,8), (4,8)]
lake = [(1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
cave = [(3,0), (3,8)]

# 0 - red turn no selection: 1-red turn piece selected: 2- blue turn no selection, 3 - blue turn piece selected
turn_step = 0
selection = 100
valid_moves = []

#animal images
blue_elephant = pygame.image.load('img/elephant.png')
blue_elephant = pygame.transform.scale(blue_elephant, (40, 40))
blue_lion = pygame.image.load('img/lion.png')
blue_lion = pygame.transform.scale(blue_lion, (40, 40))
blue_tiger = pygame.image.load('img/tiger.png')
blue_tiger = pygame.transform.scale(blue_tiger, (40, 40))
blue_leopard = pygame.image.load('img/leopard.png')
blue_leopard = pygame.transform.scale(blue_leopard, (40, 40))
blue_wolf = pygame.image.load('img/wolf.png')
blue_wolf = pygame.transform.scale(blue_wolf, (40, 40))
blue_dog = pygame.image.load('img/dog.png')
blue_dog = pygame.transform.scale(blue_dog, (40, 40))
blue_cat = pygame.image.load('img/cat.png')
blue_cat = pygame.transform.scale(blue_cat, (40, 40))
blue_mouse = pygame.image.load('img/mouse.png')
blue_mouse = pygame.transform.scale(blue_mouse, (40, 40))

blue_images = [blue_elephant, blue_lion,blue_tiger, blue_leopard, blue_wolf, blue_dog, blue_cat, blue_mouse]

red_elephant = pygame.image.load('img/elephant.png')
red_elephant = pygame.transform.scale(red_elephant, (40, 40))
red_lion = pygame.image.load('img/lion.png')
red_lion = pygame.transform.scale(red_lion, (40, 40))
red_tiger = pygame.image.load('img/tiger.png')
red_tiger = pygame.transform.scale(red_tiger, (40, 40))
red_leopard = pygame.image.load('img/leopard.png')
red_leopard = pygame.transform.scale(red_leopard, (40, 40))
red_wolf = pygame.image.load('img/wolf.png')
red_wolf = pygame.transform.scale(red_wolf, (40, 40))
red_dog = pygame.image.load('img/dog.png')
red_dog = pygame.transform.scale(red_dog, (40, 40))
red_cat = pygame.image.load('img/cat.png')
red_cat = pygame.transform.scale(red_cat, (40, 40))
red_mouse = pygame.image.load('img/mouse.png')
red_mouse = pygame.transform.scale(red_mouse, (40, 40))

red_images = [red_elephant, red_lion,red_tiger, red_leopard, red_wolf, red_dog, red_cat, red_mouse]

animal_list = ['elephant', 'lion', 'tiger', 'leopard','wolf', 'dog', 'cat', 'mouse']

#check variables/ flashing counter
counter = 0
winner = ''
game_over = False

# game board
column = 7
row = 10
def draw_board():
    for i in range(column):
        for j in range(row):
            x = i * 50
            y = j * 50
            pygame.draw.rect(screen, 'light gray', [x, y, 50, 50])
    
    #draw lake rows and collumns
    blue_rows = [3, 4, 5]
    blue_columns = [1, 2, 4, 5]
    for i in blue_rows:
        for j in blue_columns:
            pygame.draw.rect(screen, 'deepskyblue2', [ j * 50, i * 50, 50, 50])
            
    #draw protected cave
    for i in range (len(protected_cave)):
        pygame.draw.rect(screen, 'darkgray', [protected_cave[i][0] * 50, protected_cave[i][1] * 50, 50, 50])
        
    #draw winning cave
    for i in range (len(cave)):
        pygame.draw.rect(screen, 'firebrick3', [cave[i][0] * 50, cave[i][1] * 50, 50, 50])
    
    for i in range(row):
        pygame.draw.line(screen, 'black', (0, i * 50), (WIDTH, i * 50), 2)
        
    for i in range(column):
        pygame.draw.line(screen, 'black', (i * 50, 0), (i * 50, HEIGHT), 2)
        
    pygame.draw.rect(screen, 'darkgray', [0, HEIGHT - (HEIGHT // row), WIDTH, HEIGHT // row])
    status_text = ['Red: Select a Piece to Move!', 'Red: Select a Destination!',
                   'Blue: Select a Piece to Move!', 'Blue: Select a Destination!']
    # Set the turn_step to the appropriate value
    screen.blit(medium_font.render(status_text[turn_step], True, 'black'), (20, 460))
    
#draw pieces onto board
def draw_pieces():
    for i in range(len(red_animals)):
        index = animal_list.index(red_animals[i])
        pygame.draw.circle (screen, 'red', [red_locations[i][0] * 50 + 25, red_locations[i][1] * 50 + 25], 20)
        screen.blit(red_images[index], (red_locations[i][0] * 50 + 5, red_locations[i][1] * 50 + 5))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [red_locations[i][0] * 50 + 1, red_locations[i][1] * 50 + 1,
                                                 50, 50], 2)
        
    for i in range(len(blue_animals)):
        index = animal_list.index(blue_animals[i])
        pygame.draw.circle (screen, 'blue', [blue_locations[i][0] * 50 + 25, blue_locations[i][1] * 50 + 25], 20)
        screen.blit(blue_images[index], (blue_locations[i][0] * 50 + 5, blue_locations[i][1] * 50 + 5))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [blue_locations[i][0] * 50 + 1, blue_locations[i][1] * 50 + 1,
                                                  50, 50], 2)

#function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'elephant':
            moves_list = check_elephant(location, turn)
        elif piece == 'lion':
            moves_list = check_lion(location, turn)
        elif piece == 'tiger':
            moves_list = check_tiger(location, turn)
        elif piece == 'leopard':
            moves_list = check_leopard(location, turn)
        elif piece == 'wolf':
            moves_list = check_wolf(location, turn)
        elif piece == 'dog':
            moves_list = check_dog(location, turn)
        elif piece == 'cat':
            moves_list = check_cat(location, turn)
        elif piece == 'mouse':
            moves_list = check_mouse(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_elephant(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        temp_location = (10, 10)
        piece = ''
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'mouse' and temp_location not in protected_cave and target not in lake:
                moves_list.append(target)
    return moves_list

def check_lion(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        temp_location = (10, 10)
        piece = ''
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and temp_location not in protected_cave and target not in lake:
                moves_list.append(target)
    return moves_list

def check_tiger(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        temp_location = (10, 10)
        piece = ''
        if target[1] == 9:
            continue
        else: 
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and piece != 'lion' and temp_location not in protected_cave and target not in lake:
                moves_list.append(target)
    return moves_list

def check_leopard(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        temp_location = (10, 10)
        piece = ''
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and piece != 'lion' and piece != 'tiger' and temp_location not in protected_cave and target not in lake:
                moves_list.append(target)
    return moves_list

def check_wolf(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        temp_location = (10, 10)
        piece = ''
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and piece != 'lion' and piece != 'tiger' and piece != 'leopard' and temp_location not in protected_cave:
                moves_list.append(target)
    return moves_list

def check_dog(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        piece = ''
        temp_location = (10, 10)
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and piece != 'lion' and piece != 'tiger' and piece != 'leopard' and piece != 'wolf' and temp_location not in protected_cave:
                moves_list.append(target)
    return moves_list

def check_cat(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        piece = ''
        temp_location = (10, 10)
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'elephant' and piece != 'lion' and piece != 'tiger' and piece != 'leopard' and piece != 'wolf' and piece != 'dog'  and temp_location not in protected_cave and target not in lake:
                moves_list.append(target)
    return moves_list

def check_mouse(position, color):
    moves_list = []
    if color == 'red':
        enemies_list = blue_locations
        friends_list = red_locations
    else:
        enemies_list = red_locations
        friends_list = blue_locations
        
    targets =[(1, 0), (-1,0), (0,1), (0,-1)]
    for i in range(4):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        piece = ''
        temp_location = (10, 10)
        if target[1] == 9:
            continue
        else:
            if color == 'red':
                for i in range (len(blue_locations)):
                    if blue_locations[i] ==target:
                        piece = blue_animals[blue_locations.index(target)]
                        temp_location = blue_locations[i]
            else:
                for i in range (len(red_locations)):
                    if red_locations[i] == target:
                        piece = red_animals[red_locations.index(target)]
                        temp_location = red_locations[i]
            if target not in friends_list and piece != 'lion' and piece != 'tiger' and piece != 'leopard' and piece != 'wolf' and piece != 'cat' and temp_location not in protected_cave:
                moves_list.append(target)
    return moves_list

red_options = check_options(red_animals, red_locations, 'red')
blue_options = check_options(blue_animals, blue_locations, 'blue')

#check for valid moves
def check_valid_moves():
    if turn_step < 2:
        options_list = red_options
    else:
        options_list = blue_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 50 + 25, moves[i][1] * 50+ 25), 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [20, 40, 500, 50])
    screen.blit(medium_font.render(f'{winner} won the game!', True, 'white'), (20, 40))
    screen.blit(medium_font.render(f'Press ENTER to Restart!', True, 'white'), (20, 70))

# Initialize the selected piece and valid moves
selected_piece = None
valid_moves = []

# Run the game loop
run = True
while run:
    # Call the draw_board function
    draw_board()
    draw_pieces()
    
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_coord = event.pos[0] // 50
            y_coord = event.pos[1] // 50
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in red_locations:
                    selection = red_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    red_locations[selection] = click_coords
                    if click_coords in blue_locations:
                        blue_piece = blue_locations.index(click_coords)
                        blue_animals.pop(blue_piece)
                        blue_locations.pop(blue_piece)
                    for i in range (len(red_locations)):
                            if red_locations[i] == (3, 0):
                                winner = 'red'
                    blue_options = check_options(blue_animals, blue_locations, 'blue')
                    red_options = check_options(red_animals, red_locations, 'red')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
    
            if turn_step > 1:
                if click_coords in blue_locations:
                    selection = blue_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    blue_locations[selection] = click_coords
                    if click_coords in red_locations:
                        red_piece = red_locations.index(click_coords)
                        red_animals.pop(red_piece)
                        red_locations.pop(red_piece)
                    for i in range (len(blue_locations)):
                            if blue_locations[i] == (3, 8):
                                winner = 'blue'
                    blue_options = check_options(blue_animals, blue_locations, 'blue')
                    red_options = check_options(red_animals, red_locations, 'red')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                red_animals = ['elephant', 'lion', 'tiger', 'leopard','wolf', 'dog', 'cat', 'mouse']
                red_locations = [(0,6), (6,8), (0,8), (4,6), (2,6), (5,7), (1,7), (6,6)]
                blue_animals = ['elephant', 'lion', 'tiger', 'leopard','wolf', 'dog', 'cat', 'mouse']
                blue_locations = [(6,2), (0,0), (6,0), (2,2), (4,2), (5,1), (1,1), (0,2)]
                turn_step = 0
                selection = 100
                valid_moves = []
                blue_options = check_options(blue_animals, blue_locations, 'blue')
                red_options = check_options(red_animals, red_locations, 'red')
    
    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()