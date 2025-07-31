import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.5

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

stage = 0
gameOver = False
playerWon = False

# Define 3 different maps with increasing difficulty
STAGE_MAPS = [
    [  # Stage 1 — Intro stage
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
    ],
    [  # Stage 2 — Tight spaces, more keys and guards
        "WWWWWWWWWWWWWWWWW",
        "WP G  W   K   K W",
        "W W WWWWW WWWW  W",
        "W   G   W     G W",
        "W WWWWW WWWWWWW W",
        "W     K W   K   W",
        "W WWWWW W WWWWWWW",
        "W   G   W   G   W",
        "W WWWWWWW WWWWWWW",
        "W     K   G   K W",
        "W WWWWWWWWWWWWD W",
        "WWWWWWWWWWWWWWWW"
    ],
    [  # Stage 3 — Final stage, hard maze with lots of guards
        "WWWWWWWWWWWWWWWWW",
        "WP  G  DW  K  G W",
        "W W WWWWW WWWWW W",
        "W W   K   G   K W",
        "W WWWWWWWWWWWWW W",
        "W G     G    G  W",
        "W WWWWWWWWWWWWW W",
        "W K   G   K   G W",
        "W WWWWWWWWWWWWW W",
        "W   G     G     W",
        "W WWWWWWWWWWWWW W",
        "WWWWWWWWWWWWWWWW"
    ],
    [  # Stage 4 - Guard Gauntlet
        "WWWWWWWWWWWWWWWW",
        "W   G     G    W",
        "W  K   W   K   W",
        "W  W           W",
        "W   G   P  WG  W",
        "W              W",
        "W  K   W   K   W",
        "W   G     G    W",
        "W              W",
        "W  WK   W   K  W",
        "W      WD  G   W",
        "WWWWWWWWWWWWWWWW"
    ],
    [  # Stage 5 - The Death Grid (Nightmare)
        "WWWWWWWWWWWWWWWW",
        "W K G W G W G DW",
        "W W W W W W W WW",
        "W G   G K   G  W",
        "W W W W W W W WW",
        "W K G   W   G  W",
        "W W W W W W W WW",
        "W G   K G   K  W",
        "W W W W W W W WW",
        "W K G   G   G  W",
        "WPW W W W W W WW",
        "WWWWWWWWWWWWWWWW"
    ]
]









def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

def DrawScenery():
    current_map = STAGE_MAPS[stage]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = current_map[y][x]
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
    screen.draw.text("Game Over", midbottom=screenMiddle, fontsize=GRID_SIZE, color="red", width=1)
    if playerWon:
        screen.draw.text("You Escaped!", midtop=screenMiddle, fontsize=GRID_SIZE, color="green", width=1)
    else:
        screen.draw.text("You Were Caught!", midtop=screenMiddle, fontsize=GRID_SIZE, color="red", width=1)
    
    screen.draw.text("Press SPACE to Restart", midtop=(screenMiddle[0], screenMiddle[1] + GRID_SIZE), fontsize=GRID_SIZE // 2, color="white", width=1)

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()

def SetupGame():
    global player, keysToCollect, guards, gameOver, playerWon
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False
    playerWon = False
    current_map = STAGE_MAPS[stage]

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = current_map[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"), pos=GetScreenCoords(x, y))
                guards.append(guard)

def MovePlayer(dx, dy):
    global gameOver, playerWon, stage
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
        return
    square = STAGE_MAPS[stage][y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            stage += 1
            if stage >= len(STAGE_MAPS):
                gameOver = True
                playerWon = True
            else:
                clock.unschedule(MoveGuards)
                SetupGame()
                clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
            return

    for key in keysToCollect:
        if GetActorGridPos(key) == (x, y):
            keysToCollect.remove(key)
            break
    player.pos = GetScreenCoords(x, y)

def on_key_down(key):
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def on_key_up(key):
    if key == keys.SPACE and gameOver:
        global stage
        
        clock.unschedule(MoveGuards)
        SetupGame()
        clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)

def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)
    map = STAGE_MAPS[stage]
    if playerX > guardX and guardX + 1 < GRID_WIDTH and map[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and guardX - 1 >= 0 and map[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and guardY + 1 < GRID_HEIGHT and map[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and guardY - 1 >= 0 and map[guardY - 1][guardX] != "W":
        guardY -= 1
    guard.pos = GetScreenCoords(guardX, guardY)
    if (guardX, guardY) == (playerX, playerY):
        print("Caught by guard!")
        gameOver = True

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)

SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()
