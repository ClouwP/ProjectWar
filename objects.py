round=1

class Player:
    def __init__(self,number,location):
        self.number=str(number)
        self.location = location
        self.wood=0
        self.iron=0
        self.food=0
        self.workers=2
        self.workers_used=0
        self.armypawnds= {}
        self.armyused = 0
        self.stone=0
        self.gold=0
        self.expansion='Town'
        
        def recours(self,item):
            if item == 'Iron':
                self.iron += 1
            elif item == 'Wood':
                self.wood += 1
            elif item == 'Stone':
                self.stone += 1
            elif item == 'Food':
                self.food += 1
            elif item == 'Gold':
                self.gold += 1        
class Shop:
    global currentplayer
    def __init__(self):
        self.buywood=4
        self.buyiron=4
        self.buyfood=4
        self.buystone=4
        self.buygold=1
        self.buyworkers=[2,'w',1,'f'] #'2 Wood,2 Food'
        self.buyexpansion=[4,'s',3,'w',3,'i'] #'4 Stone, 3 Wood, 3 Iron'
        self.buyarmypawnds=[2,'i',1,'f']#'2 Iron,1 Food'
        
        self.sellwood=1
        self.selliron=1
        self.sellfood=1
        self.sellstone=1
         
        
        
    
         
#dit was gewoon een test maar normaal moet je input krijgen bij setup en dan gaat ie in de for loop spelers maken
player1=Player('1',[1100,90])
player2=Player('2',[650,90])    
player3=Player('3',[1100,540])
player4=Player('4',[650,540])
currentplayer=player1
Shop=Shop()
