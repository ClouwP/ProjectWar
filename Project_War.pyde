import Guide_screen, Setup_screen, Start_screen, Test_screen, Player_menu, Player_start, Recourcs_shop, Shop_choose, Village_shop, next_player, objects, workers, War


gameScreen = 16



def setup():
    size(1280,720)

def draw():

    
    
    if gameScreen == 0:
        Start_screen.draw()
    elif gameScreen == 1:
        Setup_screen.draw()
    elif gameScreen == 10:
        Player_start.draw()
    elif gameScreen == 11:
        Player_menu.draw()
    elif gameScreen == 12:
        Shop_choose.draw()
    elif gameScreen == 13:
        Recourcs_shop.draw()
    elif gameScreen == 14:
        Village_shop.draw()
    elif gameScreen == 15:
        workers.draw()
    elif gameScreen == 16:
        War.draw()
    elif gameScreen == 25:
        Test_screen.draw()   
    



def mousePressed():
    global gameScreen, setupbotums, selectColor, players, rounds, workers,recours_blok1,recours_blok2, recours_choose, color1, color2
#*******************************************************************************************************************************************#    
    if gameScreen == 0:
        if 10 < mouseX < 350 and 400 < mouseY < 490:
            gameScreen = 1

#*******************************************************************************************************************************************#
    elif gameScreen == 1:
        #player butmus
        if Setup_screen.setupbotums[1][4] < mouseX < Setup_screen.setupbotums[1][4] + 100 and Setup_screen.setupbotums[1][5] < mouseY < Setup_screen.setupbotums[1][5] + 50:
             Setup_screen.setupbotums[1][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[1][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[1][3] = Setup_screen.selectColor[2]
             
             Setup_screen.setupbotums[2][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[2][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[2][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[3][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[3][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[3][3] = Setup_screen.noSelectColor[2]
             Setup_screen.players = 2
             
        elif Setup_screen.setupbotums[2][4] < mouseX < Setup_screen.setupbotums[2][4] + 100 and Setup_screen.setupbotums[2][5] < mouseY < Setup_screen.setupbotums[2][5] + 50:
             Setup_screen.setupbotums[2][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[2][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[2][3] = Setup_screen.selectColor[2]
             Setup_screen.players = 3
             
             Setup_screen.setupbotums[1][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[1][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[1][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[3][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[3][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[3][3] = Setup_screen.noSelectColor[2]
             
        elif Setup_screen.setupbotums[3][4] < mouseX < Setup_screen.setupbotums[3][4] + 100 and Setup_screen.setupbotums[3][5] < mouseY < Setup_screen.setupbotums[3][5] + 50:
             Setup_screen.setupbotums[3][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[3][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[3][3] = Setup_screen.selectColor[2]
             Setup_screen.players = 4
             
             Setup_screen.setupbotums[1][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[1][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[1][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[2][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[2][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[2][3] = Setup_screen.noSelectColor[2]
             
        
        #rounds butmus
        elif Setup_screen.setupbotums[4][4] < mouseX < Setup_screen.setupbotums[4][4] + 100 and Setup_screen.setupbotums[4][5] < mouseY < Setup_screen.setupbotums[4][5] + 50:
             Setup_screen.setupbotums[4][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[4][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[4][3] = Setup_screen.selectColor[2]
             Setup_screen.rounds = 10
             
             Setup_screen.setupbotums[5][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[5][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[5][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[6][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[6][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[6][3] = Setup_screen.noSelectColor[2]
             
        elif Setup_screen.setupbotums[5][4] < mouseX < Setup_screen.setupbotums[5][4] + 100 and Setup_screen.setupbotums[5][5] < mouseY < Setup_screen.setupbotums[5][5] + 50:
             Setup_screen.setupbotums[5][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[5][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[5][3] = Setup_screen.selectColor[2]
             Setup_screen.rounds = 15
            
             Setup_screen.setupbotums[4][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[4][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[4][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[6][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[6][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[6][3] = Setup_screen.noSelectColor[2]
             
        elif Setup_screen.setupbotums[6][4] < mouseX < Setup_screen.setupbotums[6][4] + 100 and Setup_screen.setupbotums[6][5] < mouseY < Setup_screen.setupbotums[6][5] + 50:
             Setup_screen.setupbotums[6][1] = Setup_screen.selectColor[0]
             Setup_screen.setupbotums[6][2] = Setup_screen.selectColor[1]
             Setup_screen.setupbotums[6][3] = Setup_screen.selectColor[2]
             Setup_screen.rounds = 20
             
             Setup_screen.setupbotums[4][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[4][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[4][3] = Setup_screen.noSelectColor[2]
             
             Setup_screen.setupbotums[5][1] = Setup_screen.noSelectColor[0]
             Setup_screen.setupbotums[5][2] = Setup_screen.noSelectColor[1]
             Setup_screen.setupbotums[5][3] = Setup_screen.noSelectColor[2]

        elif Setup_screen.rounds > 0 and Setup_screen.players > 0:
            if 10 < mouseX < 350 and 500 < mouseY < 690:
                gameScreen = 10    
#*******************************************************************************************************************************************#

    elif gameScreen == 10:
        if 470<mouseX<810 and 400<mouseY<492:
            gameScreen = 11  
#*******************************************************************************************************************************************# ROuds bijwerlen
    
    elif gameScreen==11:
        if 10<mouseX<350 and 110<mouseY<202: # verkeerde x en y voor de knop
            gameScreen= 12
        elif 10<mouseX<350 and 250<mouseY<300:
            gameScreen = 15
        elif 10<mouseX<350 and 390<mouseY<440:
            gameScreen = 16
        elif 10<mouseX<350 and 550<mouseY<640: # verkeerde x en y voor de knop
            objects.currentplayer.workers_used = 0
            if objects.currentplayer== objects.player1 and Setup_screen.players >=2 :
                objects.currentplayer= objects.player2
            elif objects.currentplayer== objects.player2 and Setup_screen.players >=3 :
                objects.currentplayer= objects.player3
            elif objects.currentplayer== objects.player3 and Setup_screen.players >=4 :
                objects.currentplayer=objects.player4
            else:
                objects.round+=1
                objects.currentplayer=objects.player1
            gameScreen=10
#*******************************************************************************************************************************************#

    elif gameScreen==12: #hier staan alle shop buttons (verkeerde x en y)
        if 10<mouseX<350 and 110<mouseY<202: # verkeerde x en y voor de knop
            gameScreen=13
        elif 10<mouseX<350 and 250<mouseY<343: # verkeerde x en y voor de knop
            gameScreen=14
        elif 10<mouseX<350 and 550<mouseY<640: # verkeerde x en y voor de knop
            gameScreen=11 
    
 #*******************************************************************************************************************************************#
   
    
    elif gameScreen==13:    
        if 800<mouseX<900 and 100<mouseY<200: #buy stone
            if objects.currentplayer.gold>=4:
                objects.currentplayer.stone+=1
                objects.currentplayer.gold-=4
        elif 1000<mouseX<1100 and 100<mouseY<200: #sell stone
            if objects.currentplayer.stone>=1:
                vcurrentplayer.stone-=1
                vcurrentplayer.gold+=1
        elif 800<mouseX<900 and 253<mouseY<353: #buy food
            if objects.currentplayer.gold>=4:
                objects.currentplayer.food+=1
                objects.currentplayer.gold-=4
        elif 1000<mouseX<1100 and 253<mouseY<353: #sell food
            if objects.currentplayer.food>=1:
                objects.currentplayer.food-=1
                objects.currentplayer.gold+=1
        elif 800<mouseX<900 and 400<mouseY<500: #buy iron
            if objects.currentplayer.gold>=4:
                objects.currentplayer.iron+=1
                objects.currentplayer.gold-=4
        elif 1000<mouseX<1100 and 400<mouseY<500: #sell iron
            if objects.currentplayer.iron>=1:
                objects.currentplayer.iron-=1
                vcurrentplayer.gold+=1
        elif 800<mouseX<900 and 553<mouseY<653: #buy wood
            if objects.currentplayer.gold>=4:
                objects.currentplayer.wood+=1
                objects.currentplayer.gold-=4 
        elif 1000<mouseX<1100 and 553<mouseY<653: #buy wood
            if objects.currentplayer.wood>=1:
                objects.currentplayer.wood-=1
                objects.currentplayer.gold+=1
        elif 10<mouseX<350 and 550<mouseY<640: # verkeerde x en y voor de knop
            gameScreen=11 
    
    elif gameScreen==14:
        if 10<mouseX<350 and 550<mouseY<640: # verkeerde x en y voor de knop
            gameScreen=11 
        elif 800<mouseX<1100 and 100<mouseY<200 and (objects.currentplayer.expansion=='Town' and objects.currentplayer.armypawnds<2 or objects.currentplayer.expansion=='City' and objects.currentplayer.armypawnds<5 ): #buy army 
            if objects.currentplayer.iron>=2 and objects.currentplayer.food>=1:
                objects.currentplayer.armypawnds+=1
                objects.currentplayer.iron-=2
                objects.currentplayer.food-=1
        elif 800<mouseX<1100 and 250<mouseY<350: #Worker kopen button
            if objects.currentplayer.wood>=2 and objects.currentplayer.food>=1:
                objects.currentplayer.workers+=1
                objects.currentplayer.wood-=2
                objects.currentplayer.food-=1
        elif 800<mouseX<1100 and 400<mouseY<500: #Village expansion
            if objects.currentplayer.expansion=='Town' and objects.currentplayer.stone>=4 and objects.currentplayer.wood>=3 and objects.currentplayer.iron>=3  :
                objects.currentplayer.expansion='City'
                objects.currentplayer.stone-=4
                objects.currentplayer.wood-=3
                objects.currentplayer.iron-=3    
    
#*******************************************************************************************************************************************#
    elif gameScreen==15:
        start = 1
        start2 = 1
        if 20<mouseX<360 and 550 <mouseY< 640:
            gameScreen=11
        
        if 20<mouseX<125 and 460 <mouseY< 492:
            if workers.recours_choose != 'none' and objects.currentplayer.workers_used < objects.currentplayer.workers:
                objects.currentplayer.workers_used += 1
                if workers.recours_choose == 'Iron':
                    objects.currentplayer.iron += 1
                elif workers.recours_choose == 'Wood':
                    objects.currentplayer.wood += 1
                elif workers.recours_choose == 'Stone':
                    objects.currentplayer.stone += 1
                elif workers.recours_choose == 'Food':
                    objects.currentplayer.food += 1
                elif workers.recours_choose == 'Gold':
                    objects.currentplayer.gold += 1        
        
        while start <= 64:
            if workers.tile[start][1] < mouseX < workers.tile[start][1] + 90 and workers.tile[start][2] < mouseY < workers.tile[start][2] + 90:
                start2 = start
                workers.color1 = workers.deselsct 
                workers.color2 = workers.deselsct
                if workers.tile[start][4] == 'River':
                    workers.choose = workers.tile[start][3] + ' with a river'
                    if workers.tile[start][3][0:-1] == 'Mountain ':
                        workers.recours_blok1 = 'Iron'
                        workers.recours_blok2 = 'Food'

                    elif workers.tile[start][3][0:-2] == 'Forest ':
                        workers.recours_blok1 = 'Wood'
                        workers.recours_blok2 = 'Food'
                   
                    elif workers.tile[start][3][0:-2] == 'Quarry ':
                        workers.recours_blok1 = 'Stone'
                        workers.recours_blok2 = 'Food'   
             
                    elif workers.tile[start][3][0:-2] == 'Fields ':
                        workers.recours_blok1 = 'Food'
                        workers.recours_blok2 = 'Food'  
                                  
                    break
                else:
                    workers.choose = workers.tile[start][3]
                    if workers.tile[start][3][0:-1] == 'Mountain ':
                        workers.recours_blok1 = 'Iron'
                        workers.recours_blok2 = 'None'
                    elif workers.tile[start][3][0:-2] == 'Forest ':
                        workers.recours_blok1 = 'Wood'
                        workers.recours_blok2 = 'None'
                    elif workers.tile[start][3][0:-2] == 'Quarry ':
                        workers.recours_blok1 = 'Stone'
                        workers.recours_blok2 = 'None'   
                    elif workers.tile[start][3][0:-2] == 'Fields ':
                        workers.recours_blok1 = 'Food'
                        workers.recours_blok2 = 'None'    
                    elif workers.tile[start][3][0:-2] == 'grass fields ':
                        workers.recours_blok1 = 'None'
                        workers.recours_blok2 = 'None'                         
                    elif workers.tile[start][3][0:-2] == 'Rivers ':
                        workers.recours_blok1 = 'Food'
                        workers.recours_blok2 = 'None'                              
                    elif workers.tile[start][3][0:-2] == 'Gold Mine ':
                        workers.recours_blok1 = 'Gold'
                        workers.recours_blok2 = 'None'                                   
                                            
                    break
                
            elif 480 < mouseX < 480 + 60 and 180 < mouseY < 180 + 60:
                workers.choose = 'Village 1'
                workers.recours_blok1 = 'None'
                workers.recours_blok2 = 'None'
                break
            elif 760 < mouseX < 760 + 60 and 180 < mouseY < 180 + 60:
                workers.choose = 'Village 2'
                workers.recours_blok1 = 'None'
                workers.recours_blok2 = 'None'
                break
            elif 480 < mouseX < 480 + 60 and 480 < mouseY < 480 + 60:
                workers.choose = 'Village 3'
                workers.recours_blok1 = 'None'
                workers.recours_blok2 = 'None'
                break
            elif 760 < mouseX < 760 + 60 and 480 < mouseY < 480 + 60:
                workers.choose = 'Village 4'
                workers.recours_blok1 = 'None'
                workers.recours_blok2 = 'None'
                break
            else:
                start += 1
        if 20 < mouseX < 120 and  360 < mouseY < 390 and workers.recours_blok1 == 'Iron':
                                workers.recours_choose = 'Iron'
                                workers.color1 = workers.selectc
                                workers.color2 = workers.deselsct
        elif 20 < mouseX < 120 and  360 < mouseY < 390 and workers.recours_blok1 == 'Wood':
                                workers.recours_choose = 'Wood' 
                                workers.color1 = workers.selectc
                                workers.color2 = workers.deselsct
        elif 20 < mouseX < 120 and  360 < mouseY < 390 and workers.recours_blok1 == 'Stone':
                                workers.recours_choose = 'Stone'
                                workers.color1 = workers.selectc 
                                workers.color2 = workers.deselsct
                                                                
        elif 20 < mouseX < 120 and  360 < mouseY < 390 and workers.recours_blok1 == 'Food':
                                workers.recours_choose = 'Food' 
                                workers.color1 = workers.selectc
                                workers.color2 = workers.deselsct
        elif 20 < mouseX < 120 and  360 < mouseY < 390 and workers.recours_blok1 == 'Gold':
                                workers.recours_choose = 'Gold'
                                workers.color1 = workers.selectc
                                workers.color2 = workers.deselsct
                                                        
        elif 130 < mouseX < 230 and  360 < mouseY < 390 and workers.recours_blok2 == 'Food':
                                workers.recours_choose = 'Food' 
                                workers.color2 = workers.selectc
                                workers.color1 = workers.deselsct     
       
#*******************************************************************************************************************************************#
    elif gameScreen==16:
        start = 1
        while start <= 64:
            if workers.tile[start][1] < mouseX < workers.tile[start][1] + 90 and workers.tile[start][2] < mouseY < workers.tile[start][2] + 90:
                xnumber = 1
                while xnumber <= 8:
                    ynumber = 1
                    if War.tile[start][1] == War.xAS[xnumber]:
                        War.posx = xnumber
                    while ynumber <= 8:
                        if War.tile[start][2] == War.yAS[ynumber]:
                            War.posy = ynumber
                        ynumber += 1
                    xnumber += 1
                War.Nieuw_position = [War.posx,War.posy]
                break
            elif 480 < mouseX < 480 + 60 and 180 < mouseY < 180 + 60:
                xnumber = 1
                while xnumber <= 8:
                    ynumber = 1
                    if War.tile[start][1] == War.xAS[xnumber]:
                        War.posx = xnumber
                    while ynumber <= 8:
                        if War.tile[start][2] == War.yAS[ynumber]:
                            War.posy = ynumber
                        ynumber += 1
                    xnumber += 1
                War.Nieuw_position = [War.posx,War.posy]
                break
                
            elif 760 < mouseX < 760 + 60 and 180 < mouseY < 180 + 60:
                xnumber = 1
                while xnumber <= 8:
                    ynumber = 1
                    if War.tile[start][1] == War.xAS[xnumber]:
                        War.posx = xnumber
                    while ynumber <= 8:
                        if War.tile[start][2] == War.yAS[ynumber]:
                            War.posy = ynumber
                        ynumber += 1
                    xnumber += 1
                War.Nieuw_position = [War.posx,War.posy]
                break
                
            elif 480 < mouseX < 480 + 60 and 480 < mouseY < 480 + 60:
                xnumber = 1
                while xnumber <= 8:
                    ynumber = 1
                    if War.tile[start][1] == War.xAS[xnumber]:
                        War.posx = xnumber
                    while ynumber <= 8:
                        if War.tile[start][2] == War.yAS[ynumber]:
                            War.posy = ynumber
                        ynumber += 1
                    xnumber += 1
                War.Nieuw_position = [War.posx,War.posy]
                break
                
            elif 760 < mouseX < 760 + 60 and 480 < mouseY < 480 + 60:
                xnumber = 1
                while xnumber <= 8:
                    ynumber = 1
                    if War.tile[start][1] == War.xAS[xnumber]:
                        War.posx = xnumber
                    while ynumber <= 8:
                        if War.tile[start][2] == War.yAS[ynumber]:
                            War.posy = ynumber
                        ynumber += 1
                    xnumber += 1
                War.Nieuw_position = [War.posx,War.posy]
                break
            start += 1
                
