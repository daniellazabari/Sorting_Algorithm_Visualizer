import pygame
import random
pygame.init()

class DrawInformation:
    # Colors
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    PINK = 239, 170, 196
    GREY = 107, 113, 126
    LIGHT_PINK = 255, 196, 209
    ORANGE = 255, 232, 225
    GREEN = 212, 220, 205
    BACKGROUND_COLOR = WHITE

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
    while run:
        clock.tick(60)
        # Draw and Display window
        pygame.display.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
    pygame.quit

if __name__ == "__main__":
    main()












