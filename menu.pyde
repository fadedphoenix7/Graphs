start = False
graph = False
tree = False
posX1=100
posY1=300
posX2=100
posY2=75
posX3=320
posY3=300
posX4=100
posY4=75
textD="Select an option:"
textG="Graph"
textT="Tree"

def setup():
    size(500,500)
    background(65, 151, 217)
    
def mouseClicked():
    global start
    xC = mouseX
    yC = mouseY
    start = True

def draw():
    global posX1, posX2, posY1, posY2, start
    #Descripción
    fill(0)
    textSize(30)
    text(textD, 150, 100)
    #primera opción
    fill(255)
    stroke(0)
    rect(100, 300, 100, 75)
    #Texto del primera opción 
    fill(0)
    textSize(20)
    text(textG, 120, 340)
    #Segunda opción
    fill(255)
    stroke(0)
    rect(320, 300, 100, 75)
    #Texto de la segunda opción
    fill(0)
    textSize(20)
    text(textT, 350, 340)
    if(start):
        if(mouseX <= posX1+posX2 and mouseX >= posX1 and mouseY <= posY1+posY2 and mouseY >= posY1):
            graph = True

        if(mouseX <= posX3+posX4 and mouseX >= posX3 and mouseY <= posY3+posY4 and mouseY >= posY3):
            tree = True
        start=False
        
