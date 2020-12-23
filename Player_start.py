import objects

def draw():
    global Shop
    bg=loadImage('beginround.png')
    bg.resize(1280,720)
    background(bg)
    fill(255, 255, 255)
    textSize(55)
    textAlign(CENTER,CENTER)
    text('Player '+ objects.currentplayer.number+' |'+' Round'+str(objects.round),640,350)
