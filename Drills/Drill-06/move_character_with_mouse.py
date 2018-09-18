from pico2d import*

KPU_WIDTH, KPU_HEIGHT = 1280,1024

def handle_events():
    global running
    global x,y
    global dir
    
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x,y = KPU_WIDTH//2,KPU_HEIGHT//2
frame = 0
dir = 0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH //2, KPU_HEIGHT //2)
    character.clip_draw(frame*100,100*dir,100,100,x,y)
    update_canvas()
    frame = (frame+1)%8
    delay(0.02)
    handle_events()