BacgroundW = 0
def draw():
    global Start_side_Bar, Start_background, BacgroundW
        # WelcomeScreen Image's
    Start_side_Bar = loadImage('Start Screen Left Bar.jpg')
    Start_background = loadImage('david-edwards-kenden-001.jpg')
    
    tint(200)
    image(Start_background,BacgroundW,0)
    tint(255)
    image(Start_side_Bar,0,0)
    
    if BacgroundW > -700:
        BacgroundW -= 1
    else:
        BacgroundW = 0
