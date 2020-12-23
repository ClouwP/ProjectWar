
players = 0
rounds = 0

setupbotums = ['nothin',['2 players',25,49,104,20,230],['3 players',25,49,104,130,230],['4 players',25,49,104,240,230],['Round 10',25,49,104,20,360],['Round 15',25,49,104,130,360],['Round 20',25,49,104,240,360]]

selectColor = [37,138,30]
noSelectColor = [25,49,104]


def draw():
    global setup_bar, setupbotums
    # SetupScreen Image's
    setup_bar = loadImage('Setup Screen left bar.jpg')
    
    
    image(setup_bar,0,0)
    
    #Players
    fill(setupbotums[1][1],setupbotums[1][2],setupbotums[1][3])
    rect(20,230,100,50)
    fill(255)
    textSize(18)
    text('2 Players',25,263)
    
    fill(setupbotums[2][1],setupbotums[2][2],setupbotums[2][3])
    rect(130,230,100,50)
    fill(255)
    textSize(18)
    text('3 Players',135,263)
        
    fill(setupbotums[3][1],setupbotums[3][2],setupbotums[3][3])
    rect(240,230,100,50)
    fill(255)
    textSize(18)
    text('4 Players',245,263)
    
    #Rounds
    fill(setupbotums[4][1],setupbotums[4][2],setupbotums[4][3])
    rect(20,360,100,50)
    fill(255)
    textSize(18)
    text('10 Rounds',25,393)  
      
    fill(setupbotums[5][1],setupbotums[5][2],setupbotums[5][3])
    rect(130,360,100,50)
    fill(255)
    textSize(18)
    text('15 Rounds',135,393)

    fill(setupbotums[6][1],setupbotums[6][2],setupbotums[6][3])
    rect(240,360,100,50)
    fill(255)
    textSize(18)
    text('20 Rounds',245,393)
