import math
from turtle import width
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
    GREEN = 212, 255, 205
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (173, 181, 189),
        (108, 117, 125),
        (73, 80, 87)
    ]

    # Fonts
    FONT = pygame.font.SysFont('georgia', 25) # Regular font
    LARGE_FONT = pygame.font.SysFont('georgia', 35) # Large font

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
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        # Set drawing starting point 
        self.start_x = self.SIDE_PAD // 2

# Draw the screen
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Display text on the screen
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(title, ((draw_info.width - title.get_width())/2, 5))
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, ((draw_info.width - controls.get_width())/2, 45))
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Buble Sort | Q - Quick Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, ((draw_info.width - sorting.get_width())/2, 75))


    draw_list(draw_info)
    pygame.display.update()

# Draw the list that we are sorting
def draw_list(draw_info, color_positions={}, clear_bg= False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)


    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        # Draw rectangle blocks
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


# Generate initial list that contains n random integer elements 
# between min_val and max_val
def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n) :
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def bubble_sort(draw_info, ascending= True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.PINK}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending= True):
    lst = draw_info.lst
    for i in range (1, len(lst)):
        cur = lst[i]

        while True:
            # Condition for swapping when sorting in ascending order 
            ascending_sort = i > 0 and lst[i-1] > cur and ascending
             # Condition for swapping when sorting in descending order 
            descending_sort = i > 0 and lst[i-1] < cur and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = cur
            draw_list(draw_info, {i - 1 : draw_info.GREEN, i: draw_info.PINK}, True)
            yield True
    
    return lst

def quick_sort(draw_info, ascending= True):
   lst = draw_info.lst

   for i in range(1, len(lst)):
       pivot = lst[i]
       j = i - 1
       # Condition for swapping when sorting in ascending order 
       ascending_sort = j >= 0 and lst[j] < pivot and ascending
       # Condition for swapping when sorting in descending order 
       descending_sort = j >= 0 and lst[j] < pivot and not ascending
       while True:
        if not ascending_sort and not descending_sort:
            break
        



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
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(55)
        
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # If no key is pressed- continue
            if event.type != pygame.KEYDOWN:
                continue
            
            # If "r" key is pressed- reset the list
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            
            # Else if space key is pressed- start sorting  
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            
            # Else if "a" key is pressed- sort in ascending order  
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            
            # Else if "d" key is pressed- sort in descending order  
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            
            # Else if space key is pressed- start sorting  
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = 'Bubble Sort'
            
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = 'Insertion Sort'

            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = 'Quick Sort'

    pygame.quit()

if __name__ == "__main__":
    main()












