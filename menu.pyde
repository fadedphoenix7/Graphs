start = False
opc_1 = False
opc_2 = False
posX1 = 100
posY1 = 300
posX2 = 100
posY2 = 75
colora = (255)

def setup():
    size(500,500)
    
def mouseClicked():
    global colora
    if(mouseX <= posX1+posX2 and mouseX >= posX1 and mouseY <= posY1+posY2 and mouseY >= posY1):
        if(colora == 255):
            colora = (0)
        else:
            colora = (255)
    
def draw():
    print(mouseX,mouseY)
    global colora
    background(122)
    stroke(0)
    fill(colora)
    rect(posX1, posY1, posX2, posY2)
    
