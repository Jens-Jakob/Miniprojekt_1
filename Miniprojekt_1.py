
import pygame as pg
import math
import datetime as dt

pg.init()
screen = pg.display.set_mode((600,600))
screen.fill((255,255,255))
baggrund = (255,255,255)

angle = 0
start_point = (300,300)
    # 1 time punkter
length_1 = 200

    # 10 minutter 
length_3 = 175

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(baggrund)

    #Urskive fylde
    pg.draw.circle(screen,(232, 221, 14), (300, 300), (200))

    #Urskive 1 /cirkel
    pg.draw.circle(screen,(0, 0, 0), (300, 300), (204),width=5)

    # 10 minutter linjer
    for x in range(1,61):
        end_x = start_point[0] + length_1 * math.cos(math.radians(angle + x * 6))
        end_y = start_point[1] + length_1 * math.sin(math.radians(angle + x * 6))
        end_point = (end_x, end_y)
        pg.draw.line(screen, (0,0,0), start_point, end_point,2)

    # 10 minutters fylde
    pg.draw.circle(screen,(232, 221, 14), (300, 300), (185))

    # time linjer
    for i in range(1,13):
        end_x = start_point[0] + length_1 * math.cos(math.radians(angle + i * 30))
        end_y = start_point[1] + length_1 * math.sin(math.radians(angle + i * 30))
        end_point = (end_x, end_y)
        pg.draw.line(screen, (0,0,0), start_point, end_point,5)

    # time fylde
    pg.draw.circle(screen,(232, 221, 14), (300, 300), (175))

    s = dt.datetime.now().second
    m = dt.datetime.now().minute
    h = dt.datetime.now().hour
        # Sekundviser
    angle_sekund = s * 360/60 -90
    length_sekund = 160

        # Minutviser 
    angle_minut = m * 360/60 -90
    length_minut = 140

        # timeviser
    angle_hour = h * 360/12 -90
    length_hour = 100


    #time viser 
    h = dt.datetime.now().hour
    end_x = start_point[0] + length_hour * math.cos(math.radians(angle_hour))
    end_y = start_point[1] + length_hour * math.sin(math.radians(angle_hour))
    end_point = (end_x, end_y)
    pg.draw.line(screen, (0,0,0), start_point,end_point,4)
    

       # Minutviser 
    m = dt.datetime.now().minute
    end_x = start_point[0] + length_minut * math.cos(math.radians(angle_minut))
    end_y = start_point[1] + length_minut * math.sin(math.radians(angle_minut))
    end_point = (end_x, end_y)
    pg.draw.line(screen, (0,255,0), start_point,end_point,3)

    # Sekundviser
    end_x = start_point[0] + length_sekund * math.cos(math.radians(angle_sekund))
    end_y = start_point[1] + length_sekund * math.sin(math.radians(angle_sekund))
    end_point = (end_x, end_y)
    pg.draw.line(screen, (255,0,0), start_point,end_point,2)
    pg.display.flip()
