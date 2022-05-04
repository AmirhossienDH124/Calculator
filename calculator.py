import pygame
import sys

pygame.init()

width = 8*32 + 16
height = 1*32 + 16
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Calculator")

fps = 10
fps_clock = pygame.time.Clock()

item = ""
operation = ""
result = ""

font = pygame.font.Font(pygame.font.get_default_font(), 32)

x = 8

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if result != "":
                result = ""
                item = ""

            if event.key == pygame.K_KP_1:
                item += "1"
            if event.key == pygame.K_KP_2:
                item += "2"
            if event.key == pygame.K_KP_3:
                item += "3"
            if event.key == pygame.K_KP_4:
                item += "4"
            if event.key == pygame.K_KP_5:
                item += "5" 
            if event.key == pygame.K_KP_6:
                item += "6"
            if event.key == pygame.K_KP_7:
                item += "7"
            if event.key == pygame.K_KP_8:
                item += "8"
            if event.key == pygame.K_KP_9:
                item += "9"
            if event.key == pygame.K_KP_0:
                item += "0"
            
            if event.key == pygame.K_KP_PLUS:
                item += "+"
                operation = "+"
            if event.key == pygame.K_KP_MINUS:
                item += "-"
                operation = "-"
            if event.key == pygame.K_KP_MULTIPLY:
                item += "*"
                operation = "*"
            if event.key == pygame.K_KP_DIVIDE:
                item += "/"
                operation = "/"

            if event.key == pygame.K_BACKSPACE:
                item = item[:-1]
            
            if event.key == pygame.K_RETURN:
                item = item.split(operation)
                number_1 = int(item[0])
                number_2 = int(item[1])

                if operation == "+":
                    result = number_1 + number_2
                if operation == "-":
                    result = number_1 - number_2
                if operation == "*":
                    result = number_1 * number_2
                if operation == "/":
                    if number_2 != 0:
                        result = number_1 // number_2
                    else:
                        result = "!"
                item = str(result)
                x = 8

            item_surface = font.render(item, True, (170, 170, 170))
            screen.fill((0, 0, 0))
            if item_surface.get_width() > width - 16 and result == "":
                x -= 18
            screen.blit(item_surface, (x, 8))
            pygame.display.update()

    fps_clock.tick(fps)
