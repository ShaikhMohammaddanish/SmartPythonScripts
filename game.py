import pygame, random
pygame.init()

#coloure & globle ver
whight= (255, 255, 255)
red = (255, 0, 0)
black= (0,0,0)
#display setting
popup = pygame.display.set_mode((800,600))
pygame.display.set_caption("Danish Shaikh")
clock = pygame.time.Clock()
r = True
score = 0
snack=[]
def welcome():
    k= True
    while k:
        popup.fill((100, 200, 200))
        print_on_display("Welcome To Snack Game ", 150, 150, 56)
        print_on_display("Shaikh Mohammaddanish", 0, 0, 30)
        print_on_display("Press 'D' To Play ",  200, 250, 56)
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                k= False
                close()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_d:
                    game()
                    k = False


def plot_snack():
    for x,y in snack:
        pygame.draw.rect ( popup, black, [ x, y, 10, 10 ] )


def print_on_display (text, x, y, z):
    font = pygame.font.SysFont ( None, z )
    z=font.render(text, True, black)
    popup.blit(z, [x, y])

def close():
    global r,score
    popup.fill ( whight )
    print_on_display ( "Game Over your score is "+str(score), 250, 200 , 50)
    print_on_display ( "Press Enter To Continue", 250, 250, 50)
    for event in pygame.event.get ( ):
        if event.type == pygame.QUIT:
            r = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                snack.clear()
                score=0
                welcome()
        else:
            print_on_display ( "Press Enter To Continue", 250, 250, 50)
def game():
    global snack, r,score
    snack_x = 500
    snack_y = 500
    valosity_x = 0
    valosity_y = 0
    food_x = random.randint ( 100, 700 )
    food_y = random.randint ( 100, 500 )

    while r:
        if snack_x == 800 or snack_y == 600 or snack_x== 0 or snack_y==0:
            close()

        else:
            for event in pygame.event.get ( ):
                if event.type == pygame.QUIT:
                    r = False

                # event handling
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        valosity_x = 0
                        valosity_y = 5
                    if event.key == pygame.K_UP:
                        valosity_x = 0
                        valosity_y = -5

                    if event.key == pygame.K_RIGHT:
                        valosity_x = 5
                        valosity_y = 0

                    if event.key == pygame.K_LEFT:
                        valosity_x = -5
                        valosity_y = 0
            snack_x = valosity_x + snack_x
            snack_y = valosity_y + snack_y
            head = []
            head.append(snack_x)
            head.append(snack_y)
            snack.append(head)

            popup.fill ( whight )
            clock.tick ( 30 )
            # pygame.draw.rect(popup,black,[snack_x, snack_y, 10,10])
            plot_snack()
            with open ( "highscore.txt", "r" ) as f:
                y=f.read(3)
            print_on_display ("score " + str ( score)+ "high score "+y , 5, 5, 50 )
            pygame.draw.rect ( popup, red, [ food_x, food_y, 10, 10 ] )
            with open ( "highscore.txt" ) as f:
                highscore = f.read ( 3 )
            if score > (int ( highscore )):
                print_on_display ( "You Made Highscore", 400, 0, 50)
                with open ( "highscore.txt", "w" ) as f:
                    f.write ( str ( score ) )
            if abs ( snack_x - food_x ) < 15 and abs ( snack_y - food_y ) < 15:
                food_x = random.randint ( 100, 700 )
                food_y = random.randint ( 100, 500 )
                pygame.draw.rect ( popup, red, [ food_x, food_y, 10, 10 ] )
                score += 1
                snack.append([food_x, food_y])
            if len(snack)>(score+1):
                del snack[0]
            if snack.count(snack[0]) == 2:
                snack_y=snack_y=0
                close()
        pygame.display.update ( )

welcome()
exit(pygame)




