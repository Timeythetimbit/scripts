import pygame, time, random, math
from pygame import mixer
pygame.init()

FPS = 60
clock = pygame.time.Clock()
prevTime = time.time()

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Space.png')
pygame.display.set_icon(icon)

#Player Set up
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerSpeed = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

enemyImg = pygame.image.load('enemy.png')
enemyX = 0
enemyY = 0
enemySpeed = 6 * (60/FPS)

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

screen = pygame.display.set_mode((800,600))

mixer.music.load('background.wav')

missileImg = pygame.image.load('rainbow missle.png')
missileX = 0
missileY = playerY
missileSpeed = 360 * (60/FPS)
missileReady = True

def fireMissile(x,y):
    global missileReady
    missileReady = False
    screen.blit(missileImg, (x+16, y+16))

def isCollision(targetX, targetY, projectileX, projectileY):
    distance = math.sqrt(((targetX-projectileX)**2) + ((targetY - projectileY)**2))
    if distance <80:
        return True
    else:
        return False

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def showScore(x,y):
    scoreText = font.render("Score: " +str(score), True, (255,255,255))
    screen.blit(scoreText, (x,y))


running = True
while running:

    clock.tick(FPS)

    now = time.time()
    deltaTime = now- prevTime
    prevTime = now

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerSpeed = -360 * deltaTime
            if event.key == pygame.K_RIGHT:
                playerSpeed = 360 * deltaTime
            if event.key == pygame.K_SPACE:
                missileX = playerX
                fireMissile(missileX, missileY)
                if missileY <=0:
                    missileY = playerY
                    missileReady = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerSpeed = 0
            if event.key == pygame.K_SPACE:
                mixer.Sound('laser.wav').play()
                missileX = playerX
    playerX +=playerSpeed

    player(playerX,playerY)

        
    enemyX += enemySpeed
    if enemyX <=0:
        enemyX = 0
        enemySpeed = 360 *deltaTime
        enemyY += 40
    if enemyX >= 736:
        enemyX = 736
        enemySpeed = -360 * deltaTime
        enemyY += 40
    enemy(enemyX,enemyY)

    if not missileReady:
        missileY -= missileSpeed * deltaTime
        fireMissile(missileX,missileY)
        if missileY <=0:
            missileY = playerY
            missileReady = True
        if isCollision(enemyX, enemyY, missileX, missileY):
            mixer.Sound('explosion.wav').play()
            missileY = playerY
            missileReady = True
            score +=1

            enemyX = random.randint(0,736)
            enemyY = random.randint(50,150)

    showScore(textX, textY)

    pygame.display.update()