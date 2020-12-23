import objects

def draw():
    bg=loadImage('Shop 1.jpg')
    background(bg)
    fill(255, 255, 255)
    textSize(40)
    text('\n'+'Wood: '+str(objects.currentplayer.wood)+'\n'+'iron: '+str(objects.currentplayer.iron)+'\n'+'Food: '+str(objects.currentplayer.food)+'\n'+'Workers: '+str(objects.currentplayer.workers)+'\n'+'Army ponds: '+str(objects.currentplayer.armypawnds)+'\n'+'Gold: '+str(objects.currentplayer.gold)+'\n'+'Stone: '+str(objects.currentplayer.stone),160,280)
    fill(255, 255, 255)
    textSize(55)
    text('Stone         '+str(objects.Shop.buystone)+'G'+'       '+str(objects.Shop.sellstone)+'G',800,150)
    text('Food         '+str(objects.Shop.buyfood)+'G'+'       '+str(objects.Shop.sellfood)+'G',800,300)
    text('Iron           '+str(objects.Shop.buyiron)+'G'+'       '+str(objects.Shop.selliron)+'G',800,450)
    text('Wood         '+str(objects.Shop.buyfood)+'G'+'       '+str(objects.Shop.sellfood)+'G',800,600)
