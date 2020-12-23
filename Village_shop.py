import objects
def draw():
    bg=loadImage('Shop 2.png')
    background(bg)
    fill(255, 255, 255)
    textSize(40)
    textAlign(LEFT)
    text('\n'+'Wood: '+str(objects.currentplayer.wood)+'\n'+'iron: '+str(objects.currentplayer.iron)+'\n'+'Food: '+str(objects.currentplayer.food)+'\n'+'Workers: '+str(objects.currentplayer.workers)+'\n'+'Army pawnds: '+str(objects.currentplayer.armypawnds)+'\n'+'Stone: '+str(objects.currentplayer.stone)+'\n'+'Base: '+str(objects.currentplayer.expansion),20,100)
    
    fill(255, 255, 255)
    textSize(38)
    text('Army'+'\n'+'Pawnds',510,135)
    text('Workers',510,310)
    text('City',515,460)    
    
    text(str(objects.Shop.buyarmypawnds[0])+' Iron,'+str(objects.Shop.buyarmypawnds[2])+' Food',810,160)
    text(str(objects.Shop.buyworkers[0])+' Wood,'+str(objects.Shop.buyworkers[2])+' Food',810,320)
    textSize(36)
    text(str(objects.Shop.buyexpansion[0])+' Stone,'+str(objects.Shop.buyexpansion[2])+' Wood,'+'\n'+str(objects.Shop.buyexpansion[4])+' Iron',810,440)
 
