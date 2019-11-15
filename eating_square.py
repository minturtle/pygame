import pygame
import random


pygame.init()


width = 1024
height = 640

#player의 클래스
class Player(pygame.sprite.Sprite) :
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()
        self.speed = 3
        self.size = img.get_size()

    #player보다 먹이가 더큰지확인
    def small_player(self, other):
        if (self.size >= other.size):
            return False
        else:
            return True


#pray의 클래스
class Prey(pygame.sprite.Sprite) :
    def __init__(self,  img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()
        self.size = img.get_size()

def main() :
    heart = 3
    score = 0
    game_loop = True #게임실행 여부

    clock = pygame.time.Clock()

    #스크린의 초기화
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())
    pygame.display.set_caption("Eating  Rectangle")

    # 먹이,플레이어 객체리스트 생성
    player_list = pygame.sprite.Group()
    prey_list = pygame.sprite.Group()

    #플레이어 생성
    player_img = pygame.image.load("C:\\Users\\a0104_000\\Desktop\\programing\\python\\game\\eating square\\images\\player.png").convert()
    player = Player(player_img)
    player_list.add(player)

    for i in range(10):
        #이미지 로드
        URL = "C:\\Users\\a0104_000\\Desktop\\programing\\python\\game\\eating square\\images\\prey{}.png".format(str(random.randint(1,5)))
        img = pygame.image.load(URL).convert()
        #먹이객체의 생성
        prey = Prey(img)
        prey.rect.x = random.randint(0, width)
        prey.rect.y = random.randint(0, height)
        prey_list.add(prey)

    while (game_loop):
        #스크린을 깨끗이
        screen.fill((0,0,0))
        background.fill((0,0,0))

        #모든 이벤트 창
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) :
                game_loop = False
            if(heart == 0):
                game_loop = False

            # 키가 눌려졌을때 그리고 그키가 스페이스 바일때
            #키가 떼졌을때는 KEYUP
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    player.speed = 10
                    player.image = pygame.image.load("C:\\Users\\a0104_000\\Desktop\\programing\\python\\game\\eating square\\images\\player_dash.png").convert()

            if (event.type == pygame.KEYUP and event.key == pygame.K_SPACE):
                player.speed = 3
                player.color= (255,255,255)
                player.image = pygame.image.load("C:\\Users\\a0104_000\\Desktop\\programing\\python\\game\\eating square\\images\\player.png").convert()
        #충돌 확인, 제거
        #hit_list에는 제거된 스프라이트가 담겨있음
        hit_list = pygame.sprite.spritecollide(player, prey_list,True,pygame.sprite.collide_rect)

        for prey in hit_list:
            if(player.small_player(prey)):
                heart-=1
                print("heart:"+str(heart))
            else:
                score += 1
                print("score:"+str(score))
            hit_list.pop()






        #키보드 입력창
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            player.rect.y -= player.speed
        if pressed[pygame.K_DOWN]:
            player.rect.y += player.speed
        if pressed[pygame.K_RIGHT]:
            player.rect.x += player.speed
        if pressed[pygame.K_LEFT]:
            player.rect.x -= player.speed

        #플레이어 객체 그리기
        player_list.draw(background)

        #먹이 객체 그리기
        prey_list.draw(background)


        screen.blit(background, (0,0))
        pygame.display.flip()
        clock.tick(60)





main()