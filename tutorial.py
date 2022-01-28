from venv import create
import pygame
import random
pygame.init()

class DrawInformation:
    # Colors
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    PINK = 239, 170, 196
    LIGHT_PINK = 255, 196, 209
    ORANGE = 255, 215, 186
    GREEN = 212, 220, 205
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (173, 181, 189),
        (108, 117, 125),
        (73, 80, 87)
    ]

    

    # Padding
    SIDE_PAD = 100
    TOP_PAD = 150

    # lst is the list that we will sort
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        # Set up a drawing window
        self.window = pygame.display.set_mode((width, height))
        # Set a caption for the drawing window
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        # Calculate the width of each block based on the size of 
        # the screen and the number of blocks we will have
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        # Set drawing starting point 
        self.start_x = self.SIDE_PAD // 2

# Draw the screen
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()

# Draw the list that we are sorting
def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        # Draw rectangle blocks 
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))



# Generate initial list that contains n random integer elements 
# between min_val and max_val
def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n) :
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def main():
    run = True
    # Set a clock that regulates how quickly the loop runs
    clock = pygame.time.Clock()

    # Set display mode
    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)

        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.event != pygame.KEYDOWN:
                continue

            if pygame.event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)

    pygame.quit()

if __name__ == "__main__":
    main()












