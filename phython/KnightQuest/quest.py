import pgzrun

# Define width and height of the game grid & size of each grid tile
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.5  # How often the guards move in seconds

# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

MAP = [
    "WWWWWWWWWWWWWWWW",
    "W   G  W     K W",
    "W WWWW WWWWWWW W",
    "W W   G     W  W",
    "W W WWWWWWW W WW",
    "W W   K     W  W",
    "W WWWWW WWWWWW W",
    "W    G   P     W",
    "W WWWWW WWWWW WW",
    "W   K  W   G  WW",
    "W WWWWWWWWWWW  D",
    "WWWWWWWWWWWWWWWW"
]



def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

def SetupGame():
    global player, keysToCollect, gameOver, guards
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"), pos=GetScreenCoords(x, y))
                guards.append(guard)  # FIXED: was guards.append(guards)

def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def DrawGameOver():
    screenMiddle = (WIDTH // 2, HEIGHT // 2)
    screen.draw.text("Game Over", midbottom=screenMiddle,
                     fontsize=GRID_SIZE, color="red", width=1)

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()

def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            gameOver = True
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break
    player.pos = GetScreenCoords(x, y)

def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def MoveGuard(guard):
    global gameOver
    if gameOver:
        return

    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    if playerX > guardX and guardX + 1 < GRID_WIDTH and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and guardX - 1 >= 0 and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and guardY + 1 < GRID_HEIGHT and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and guardY - 1 >= 0 and MAP[guardY - 1][guardX] != "W":
        guardY -= 1

    guard.pos = GetScreenCoords(guardX, guardY)

    if guardX == playerX and guardY == playerY:
        gameOver = True

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)

# Start the game
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)  
pgzrun.go()
