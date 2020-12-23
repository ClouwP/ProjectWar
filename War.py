import objects

xAS = {1:560,2:650,3:740,4:830,5:920,6:1010,7:1100,8:1190}
yAS = {1:0,2:90,3:180,4:270,5:360,6:450,7:540,8:630}
Nieuw_position = (0,0)
posx = 0
posy = 0

tile = ['P.H',[1,830,90,'Mountain 1','No'],[2,1010,90,'Mountain 2','No'],[3,650,270,'Mountain 3','No'],
[4,1100,270,'Mountain 4','No'],[5,650,360,'Mountain 5','No'],[6,1100,360,'Mountain 6','No'],
[7,740,540,'Mountain 7','No'],[8,1010,540,'Mountain 8','No'],[9,830,0,'Mountain 9','River'],
[10,920,630,'Mountain 10','River'],[11,740,90,'Forest 11','No'],[12,920,90,'Forest 12','No'],
[13,650,180,'Forest 13','No'],[14,1100,180,'Forest 14','No'],[15,650,450,'Forest 15','No'],
[16,1100,450,'Forest 16','No'],[17,830,540,'Forest 17','No'],[18,920,540,'Forest 18','No'],
[19,560,270,'Forest 19','River'],[20,1190,360,'Forest 20','River'],[21,560,180,'Quarry 21','No'],
[22,830,180,'Quarry 22','No'],[23,920,180,'Quarry 23','No'],[24,1190,180,'Quarry 24','No'],
[25,560,450,'Quarry 25','No'],[26,830,450,'Quarry 26','No'],[27,920,450,'Quarry 27','No'],
[28,1190,450,'Quarry 28','No'],[29,1190,270,'Quarry 29','River'],[30,560,360,'Quarry 30','River'],
[31,740,180,'Fields 31','No'],[32,1010,180,'Fields 32','No'],[33,740,270,'Fields 33','No'],
[34,1010,270,'Fields 34','No'],[35,740,360,'Fields 35','No'],[36,1010,360,'Fields 36','No'],
[37,740,450,'Fields 37','No'],[38,1010,450,'Fields 38','No'],[39,920,0,'Fields 39','River'],
[40,830,630,'Fields 40','River'],[41,1010,0,'grass fields 41','No'],[42,740,0,'grass fields 42','No'],
[43,560,90,'grass fields 43','No'],[44,1190,90,'grass fields 44','No'],[45,560,540,'grass fields 45','No'],
[46,1190,540,'grass fields 46','No'],[47,1010,630,'grass fields 47','No'],[48,1190,0,'Rivers 48','No'],
[49,1100,0,'Rivers 49','No'],[50,650,0,'Rivers 50','No'],[51,560,0,'Rivers 51','No'],
[52,560,630,'Rivers 52','No'],[53,650,630,'Rivers 53','No'],[54,1100,630,'Rivers 54','No'],
[55,1190,630,'Rivers 55 ','No'],[56,830,270,'Gold Mine 56','No'],[57,920,270,'Gold Mine 57','No'],
[58,830,360,'Gold Mine 58','No'],[59,920,360,'Gold Mine 59','No'],[60,740,630,'Gold Mine 60','No'],[61,1100,90,'Village 1', 'No'],[62,650,90,'Village 2','No'],[63,1100,540,'Village 3','No'],[64,650,540,'Village 4','No']]



def draw():
    war_background = loadImage('War menu.jpg')
    
    image(war_background,0,0)
    textSize(20)
    text(str(len(objects.currentplayer.armypawnds)),170,158)
    text(str(len(objects.currentplayer.armypawnds) - objects.currentplayer.armyused),170,181)
    text(str(Nieuw_position),20,264)
    
    
    mounten1 = loadImage('mountain 1.jpg')
    mounten2 = loadImage('mountain 2.jpg')
    mounten3 = loadImage('mountain 3.jpg')
    mounten4 = loadImage('mountain 4.jpg')
    mounten5 = loadImage('mountain 5.jpg')
    mounten6 = loadImage('mountain 6.jpg')
    mounten7 = loadImage('mountain 7.jpg')
    mounten8 = loadImage('mountain 8.jpg')
    mounten9 = loadImage('mountain 9.jpg')
    mounten10 = loadImage('mountain 10.jpg')
    Forest11 = loadImage('Forest 11.jpg')
    Forest12 = loadImage('Forest 12.jpg')
    Forest13 = loadImage('Forest 13.jpg')
    Forest14 = loadImage('Forest 14.jpg')
    Forest15 = loadImage('Forest 15.jpg')
    Forest16 = loadImage('Forest 16.jpg')
    Forest17 = loadImage('Forest 17.jpg')
    Forest18 = loadImage('Forest 18.jpg')
    Forest19 = loadImage('Forest 19.jpg')
    Forest20 = loadImage('Forest 20.jpg')
    Quarry21 = loadImage('Quarry 21.jpg')
    Quarry22 = loadImage('Quarry 22.jpg')
    Quarry23 = loadImage('Quarry 23.jpg')
    Quarry24 = loadImage('Quarry 24.jpg')
    Quarry25 = loadImage('Quarry 25.jpg')
    Quarry26 = loadImage('Quarry 26.jpg')
    Quarry27 = loadImage('Quarry 27.jpg')
    Quarry28 = loadImage('Quarry 28.jpg')
    Quarry29 = loadImage('Quarry 29.jpg')
    Quarry30 = loadImage('Quarry 30.jpg')
    Fields31 = loadImage('Field 31.jpg')
    Fields32 = loadImage('Field 32.jpg')
    Fields33 = loadImage('Field 33.jpg')
    Fields34 = loadImage('Field 34.jpg')
    Fields35 = loadImage('Field 35.jpg')
    Fields36 = loadImage('Field 36.jpg')
    Fields37 = loadImage('Field 37.jpg')
    Fields38 = loadImage('Field 38.jpg')
    Fields39 = loadImage('Field 39.jpg')
    Fields40 = loadImage('Field 40.jpg')
    Grass41 = loadImage('Grass fields 41.jpg')
    Grass42 = loadImage('Grass fields 42.jpg')
    Grass43 = loadImage('Grass fields 43.jpg')
    Grass44 = loadImage('Grass fields 44.jpg')
    Grass45 = loadImage('Grass fields 45.jpg')
    Grass46 = loadImage('Grass fields 46.jpg')
    Grass47 = loadImage('Grass fields 47.jpg')
    River48 = loadImage('River 48.jpg')
    River49 = loadImage('River 49.jpg')
    River50 = loadImage('River 50.jpg')
    River51 = loadImage('River 51.jpg')
    River52 = loadImage('River 52.jpg')
    River53 = loadImage('River 53.jpg')
    River54 = loadImage('River 54.jpg')
    River55 = loadImage('River 55.jpg')
    gold56 = loadImage('Gold Mine 56.jpg')
    gold57 = loadImage('Gold Mine 57.jpg')
    gold58 = loadImage('Gold Mine 58.jpg')
    gold59 = loadImage('Gold Mine 59.jpg')
    gold60 = loadImage('Gold Mine 60.jpg')
    Village1 = loadImage('Village.jpg')
    
    #Mountain
    image(mounten1,tile[1][1],tile[1][2],90,90)
    image(mounten2,tile[2][1],tile[2][2],90,90)
    image(mounten3,tile[3][1],tile[3][2],90,90)
    image(mounten4,tile[4][1],tile[4][2],90,90)
    image(mounten5,tile[5][1],tile[5][2],90,90)
    image(mounten6,tile[6][1],tile[6][2],90,90)
    image(mounten7,tile[7][1],tile[7][2],90,90)
    image(mounten8,tile[8][1],tile[8][2],90,90)
    image(mounten9,tile[9][1],tile[9][2],90,90)
    image(mounten10,tile[10][1],tile[10][2],90,90)
    
    #Forest
    image(Forest11,tile[11][1],tile[11][2],90,90)
    image(Forest12,tile[12][1],tile[12][2],90,90)
    image(Forest13,tile[13][1],tile[13][2],90,90)
    image(Forest14,tile[14][1],tile[14][2],90,90)
    image(Forest15,tile[15][1],tile[15][2],90,90)
    image(Forest16,tile[16][1],tile[16][2],90,90)    
    image(Forest17,tile[17][1],tile[17][2],90,90)    
    image(Forest18,tile[18][1],tile[18][2],90,90)    
    image(Forest19,tile[19][1],tile[19][2],90,90)    
    image(Forest20,tile[20][1],tile[20][2],90,90)
    
    #Quarry
    image(Quarry21,tile[21][1],tile[21][2],90,90)
    image(Quarry22,tile[22][1],tile[22][2],90,90)     
    image(Quarry23,tile[23][1],tile[23][2],90,90)    
    image(Quarry24,tile[24][1],tile[24][2],90,90)    
    image(Quarry25,tile[25][1],tile[25][2],90,90)    
    image(Quarry26,tile[26][1],tile[26][2],90,90)    
    image(Quarry27,tile[27][1],tile[27][2],90,90)    
    image(Quarry28,tile[28][1],tile[28][2],90,90)    
    image(Quarry29,tile[29][1],tile[29][2],90,90)    
    image(Quarry30,tile[30][1],tile[30][2],90,90)
    
    #Fields
    image(Fields31,tile[31][1],tile[31][2],90,90)
    image(Fields32,tile[32][1],tile[32][2],90,90)
    image(Fields33,tile[33][1],tile[33][2],90,90)
    image(Fields34,tile[34][1],tile[34][2],90,90)
    image(Fields35,tile[35][1],tile[35][2],90,90)
    image(Fields36,tile[36][1],tile[36][2],90,90)
    image(Fields37,tile[37][1],tile[37][2],90,90)
    image(Fields38,tile[38][1],tile[38][2],90,90)    
    image(Fields39,tile[39][1],tile[39][2],90,90)
    image(Fields40,tile[40][1],tile[40][2],90,90)
    
    #Grass
    image(Grass41,tile[41][1],tile[41][2],90,90)
    image(Grass42,tile[42][1],tile[42][2],90,90)
    image(Grass43,tile[43][1],tile[43][2],90,90)    
    image(Grass44,tile[44][1],tile[44][2],90,90)
    image(Grass45,tile[45][1],tile[45][2],90,90)    
    image(Grass46,tile[46][1],tile[46][2],90,90)       
    image(Grass47,tile[47][1],tile[47][2],90,90)    
    image(River48,tile[48][1],tile[48][2],90,90)
    
    #River
    image(River49,tile[49][1],tile[49][2],90,90)
    image(River50,tile[50][1],tile[50][2],90,90)    
    image(River51,tile[51][1],tile[51][2],90,90)    
    image(River52,tile[52][1],tile[52][2],90,90)    
    image(River53,tile[53][1],tile[53][2],90,90)    
    image(River54,tile[54][1],tile[54][2],90,90)    
    image(River55,tile[55][1],tile[55][2],90,90)
    
    #GOLD
    image(gold56,tile[56][1],tile[56][2],90,90)    
    image(gold57,tile[57][1],tile[57][2],90,90)
    image(gold58,tile[58][1],tile[58][2],90,90)    
    image(gold59,tile[59][1],tile[59][2],90,90)    
    image(gold60,tile[60][1],tile[60][2],90,90)  
    #Village1
    image(Village1,tile[61][1],tile[61][2],90,90)
    image(Village1,tile[62][1],tile[62][2],90,90)
    image(Village1,tile[63][1],tile[63][2],90,90)
    image(Village1,tile[64][1],tile[64][2],90,90)
