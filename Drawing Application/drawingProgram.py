import pygame

def main():
    running = True
    brushFill = False
    brushColor = pygame.Color(0, 0, 0, 255)
    brushSize = 1
    
    pygame.display.init()
    clock = pygame.time.Clock()

    windowWidth = 1925
    windowHeight = 1025

    window = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Drawing Program")

    windowColor = [255, 255, 255]
    window.fill(windowColor)

    pygame.display.update()


    

    """Print the menu here"""
    
    print("Red - 1")
    print("Orange - 2")
    print("Yellow - 3")
    print("Green - 4")
    print("Blue - 5")
    print("Purple - 6")
    print("Turquoise - 7")
    print("Olive - 8")
    print("White - 9")
    print("Black - 0")
    print("Brush Size Increase is Plus Button")
    print("Brush Size Decrease is Minus Button")

    while running:
        fLock = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_EQUALS]:
                brushSize += 1
                print(brushSize)
            if keys[pygame.K_MINUS]:
                brushSize -= 1
                print(brushSize)
            if keys[pygame.K_1]:
                brushColor = pygame.Color("Red")
                print("Color:Red")
            if keys[pygame.K_2]:
                brushColor = pygame.Color("Orange")
                print("Color:Orange")
            if keys[pygame.K_3]:
                brushColor = pygame.Color("Yellow")
                print("Color:Yellow")
            if keys[pygame.K_4]:
                brushColor = pygame.Color("Green")
                print("Color:Green")
            if keys[pygame.K_5]:
                brushColor = pygame.Color("Blue")
                print("Color:Blue")
            if keys[pygame.K_6]:
                brushColor = pygame.Color("Purple")
                print("Color:Purple")
            if keys[pygame.K_7]:
                brushColor = pygame.Color("Turquoise")
                print("Color:Turquoise")
            if keys[pygame.K_8]:
                brushColor = pygame.Color("Olive")
                print("Color:Olive")
            if keys[pygame.K_9]:
                brushColor = pygame.Color("White")
                print("Color:White")
            if keys[pygame.K_0]:
                brushColor = pygame.Color("Black")
                print("Color:Black")
            if keys[pygame.K_f] and not fLock:
                fLock = True
                if brushFill == False:
                    brushFill = True
                    print("Fillmode: True")
                else:
                    brushFill = False
                    print("Fillmode: False")

            if brushSize < 1:
                brushSize = 1
                
                

            if pygame.mouse.get_pressed()[0]:
                if brushFill == True:
                    mousepos = pygame.mouse.get_pos()
                    mousecolor = window.get_at(mousepos)
                    print(mousecolor)
                    if mousecolor != brushColor:
                        pixelQueue = []
                        pixelQueue.append(mousepos)
                        while pixelQueue:
                            pixel = pixelQueue.pop(0)
                            window.set_at(pixel, brushColor)
                            if pixel[1] >= 1:
                                if window.get_at((pixel[0], pixel[1] - 1)) == mousecolor:
                                    window.set_at((pixel[0], pixel[1] - 1), brushColor)
                                    pixelQueue.append((pixel[0], pixel[1] - 1))
                            if pixel[1] < windowHeight - 1:
                                if window.get_at((pixel[0], pixel[1] + 1)) == mousecolor:
                                    window.set_at((pixel[0], pixel[1] + 1), brushColor)
                                    pixelQueue.append((pixel[0], pixel[1] + 1))

                            if pixel[0] >= 1:
                                if window.get_at((pixel[0] - 1, pixel[1])) == mousecolor:
                                    window.set_at((pixel[0] - 1, pixel[1]), brushColor)
                                    pixelQueue.append((pixel[0] - 1, pixel[1]))
                                
                            if pixel[0] < windowWidth - 1:
                                if window.get_at((pixel[0] + 1, pixel[1])) == mousecolor:
                                    window.set_at((pixel[0] + 1, pixel[1]), brushColor)
                                    pixelQueue.append((pixel[0] + 1, pixel[1]))
                                    
                else:
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(window, brushColor, pos, brushSize)

            

        pygame.display.update()
                


        

    """Create variables for brushColor and brushSize"""

    """Create a while loop"""

    """....Create a for loop to get the pygame events"""
    
    """........Check if the user presses a KEYDOWN"""

    """............Match the event.key to its case"""
    """............case 27 = Escape"""
    """............case 45 = Minus """
    """............case 48 = 0     """
    """............case 49 = 1     """
    """............case 61 = Plus  """
                
    """........Check if the mouse gets pressed"""

    """............Get the position of the mouse"""

    """............Draw a circle on the window, using brushColor, the mouse's position, and brushSize"""

    """....Update the display"""

main()
