

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(BLUE,RED,GREEN,ORANGE)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    def __init__(self,x_point,y_point,width,height,color):
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color

        a_building=Building(100,random.randint(100,200),0,RED,6)
        building2=Building(0,300,random.randint(100,250),0,BLUE)

    def draw(self):
        
        pygame.draw.rect(screen,RED,(self.x_point,self.y_point,self.width,self.height))
       

    def move(self, speed):
        self.x_point += speed
        
       



class Scroller(object):
    
   
    def __init__(self, width, height, base, colors, speed):
        self.width=width
        self.height=height
        self.base=base
        self.colors=colors
        self.speed=speed
        self.list1=[]

        self.combined_width=0

    def create_buildings(self):
        combined_width = 0 
        while combined_width <= self.width:
            self.add_building(combined_width)
            combined_width+= self.list1[-1].width
   

   

    def create_building(self, x_location):
        width=random.randint(10,60)
        building1=Building(x_location,random.randint(0,300),random.randint(-80,-200),WHITE)

        self.list_.append(building1)
        

    
    def draw_buildings(self):
        for current_building in self.building_list:
            current_building.draw()

    
        
    def draw(self):
        screen
        pygame.draw.rect(screen,RED,(0,random.randint(100,400),150,200))




    def move_buildings(self):
        for current_building in self.building_list:
            current_building.move(2)

            if self.building_list[-1].x_point> SCREEN_WIDTH:
                self.building_list.remove(sellf.building_list[-1])
            if self.building_list[0].x_point > 0:
                width=random.randint(10,60)
                x_location=self.building_list[0].x_point=width
                building=building(x_location,300,width.random.randint(-200,-800),WHITE)
                self.building_list.insert(0,building)

        # if last_building.x_point > 800:
        #     self.building_list.remove(last_building)
        # if  first_building.x_location < 0:
        #     self.create_building


            

        # self.building1.move(speed)
        # a_building=Building(100,random.randint(100,200),0,RED,6)
        # building2=Building(0,300,random.randint(100,250),0,BLUE)
        
        

       
    
        



        FRONT_SCROLLER_COLORS = (0,0,30)
        MIDDLE_SCROLLER_COLORS= (30,30,100)
        BACK_SCROLLER_COLORS = (50,50,150)
        BACKGROUND_COLORS = (17, 9, 89)

        front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
        middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
        back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    # --- Drawing code should go here
    # build.draw()
    # build.move(5)
    # build.draw()
    # build.move(5)


    pygame.draw.rect(screen,RED,(0,random.randint(100,400),150,200))
   
    # back_scroller.create.draw_buildings()
    # back_scroller.create.move_buildings()
    # middle_scroller.create.draw_buildings()
    # # middle_scroller.move_buildings()
    # # front_scroller.draw_buildings()
    # # front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
