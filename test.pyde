nodo = 0
busqueda = False
distances = 0
number = -1
cord1 = 0
cord2 = 0
process = False
linea = 0
mC = False
j = 0
aristas = [] 
n = 0 
vInit = 0
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


class vertice(object):

    def __init__(self,xcord,ycord,number,colors):
        self.xcord = xcord
        self.ycord = ycord
        self.number = number
        self.colors = colors
        
    def display(self):
        stroke(0)
        fill(self.colors)
        ellipse(self.xcord,self.ycord,30,30)
        fill(255)
        text(self.number,self.xcord,self.ycord)
        
    def on(self,i):
        global nodo,cord1,cord2,linea,grafo,process,cordAx,cordAy,aristas,n,busqueda,vInit
        disX = self.xcord - mouseX
        disY = self.ycord - mouseY
        if(graph):
            if (disX <= 15 and disX >= -15 and disY <= 15 and disY >= -15):
                if(process == False):
                    self.colors = color(100, 48, 135)    
                
                if (mousePressed and (mouseButton == LEFT) and process == False):
                    self.xcord = mouseX
                    self.ycord = mouseY
                    for l in aristas:
                        if(l[1] == i):
                            l[0].move(1)
                            
                        if(l[2] == i):
                            l[0].move(2)
                    
                if (mousePressed and (mouseButton == RIGHT) and process == False):
                    process = True
                    self.colors = color(150,150,135)
                    cordAx = self.xcord
                    cordAy = self.ycord
                    nodo = i
                    grafo[i][2] += 1
                    
                if (keyPressed and (key == 'a') and process == False):
                    grafo.remove(grafo[j])
                    matrizGrafo.remove(matrizGrafo[j])
                    l = -1
                    while(l != len(aristas)):
                        l += 1
                        if(l < len(aristas)):
                            if(aristas[l][1] == j):
                                aristas.remove(aristas[l])
                                l = -1
                            elif(aristas[l][2] == j):
                                aristas.remove(aristas[l])
                                l = -1
                    return True
                
                if(keyPressed and (key == 'f') and process == False):
                    process = True
                    busqueda = True
                    self.colors = color(200,100,200)
                    vInit = i
                    
                if(keyPressed and (key == 'd') and process == False):  
                    process = True 
                    colores()   
    
                
            else:
                if(process == False):
                    self.colors = color(245, 0, 135)
                    
        if(tree):
            if (disX <= 15 and disX >= -15 and disY <= 15 and disY >= -15):
                if(process == False):
                    self.colors = color(100, 48, 135)    
                
                if (mousePressed and (mouseButton == LEFT) and process == False):
                    self.xcord = mouseX
                    self.ycord = mouseY
                    for l in aristas:
                        if(l[1] == i):
                            l[0].move(1)
                            
                        if(l[2] == i):
                            l[0].move(2)
                            
                if (mousePressed and (mouseButton == RIGHT) and process == False):
                    process = True
                    self.colors = color(150,150,135)
                    cordAx = self.xcord
                    cordAy = self.ycord
                    nodo = i
                 
                if (keyPressed and (key == 'a') and process == False):
                    arbol.remove(arbol[j])
                    l = -1
                    while(l != len(aristas)):
                        l += 1
                        if(l < len(aristas)):
                            if(aristas[l][1] == j):
                                aristas.remove(aristas[l])
                                l = -1
                            elif(aristas[l][2] == j):
                                aristas.remove(aristas[l])
                                l = -1
                    return True   
                
                if(keyPressed and (key == 'p') and process == False):  
                    process = True 
                    busquedaBinaria(i)                    
            else:
                if(process == False):
                    self.colors = color(245, 0, 135)   
                
    def processLook(self,i):
        global nodo,cord1,cord2,linea,grafo,process,cordAx,cordAy,n,aristas,matrizGrafo,busqueda
        disX = self.xcord - mouseX
        disY = self.ycord - mouseY
        
        if (disX <= 15 and disX >= -15 and disY <= 15 and disY >= -15):
            self.colors = color(200,100,200)
            
            if(keyPressed and (key == 'g')):
                look(i,vInit)
                process = False
                busqueda = False
                            
        else:
            if(process == False):
                self.colors = color(245, 0, 135)
            
    def onProcess(self,i):
        global nodo,cord1,cord2,linea,grafo,process,cordAx,cordAy,n,aristas,matrizGrafo,graph,tree,arbol
        disX = self.xcord - mouseX
        disY = self.ycord - mouseY
        if(graph):
            if (disX <= 15 and disX >= -15 and disY <= 15 and disY >= -15):
                self.colors = color(150,150,135)
                
                if(keyPressed and (key == 'b')):
                    distance = 0
                    aristas.append([arista(self.xcord,self.ycord,color(255),distance),nodo,i,number,distance])
                    process = False
                    matrizGrafo[i][nodo] += 1
                    matrizGrafo[nodo][i] += 1
                    grafo[i][2] += 1
                                
            else:
                if(process == False):
                    self.colors = color(245, 0, 135)
        if(tree):        
            if (disX <= 15 and disX >= -15 and disY <= 15 and disY >= -15):
                self.colors = color(150,150,135)
                distance = 0
                if(keyPressed and (key == 'b')):
                    aristas.append([arista(self.xcord,self.ycord,color(255),distance),nodo,i])
                    process = False
                 
            else:
                if(process == False):
                    self.colors = color(245, 0, 135)
                    
class arista(object):
    def __init__(self,xcord,ycord,colors,distance):
        self.xcord = xcord
        self.ycord = ycord
        self.colors = colors
        self.xpos = cordAx
        self.ypos = cordAy
        self.distance = distance
    
    def display2(self,i):
        global aristas,distances
        stroke(self.colors)
        line(self.xcord,self.ycord,self.xpos,self.ypos)
        x = int((self.xcord + self.xpos)/2)
        y = int((self.ycord + self.ypos)/2)
        distances =  int((sqrt(((self.xcord - self.xpos)**2) + ((self.ycord - self.ypos)**2)))/6)
        self.distance = distances
        fill(200)
        textSize(15)
        text(self.distance,x,y)
        
    def move(self,vec):
        if(vec == 1):
            self.xpos = mouseX
            self.ypos = mouseY
            
        if(vec == 2):
            self.xcord = mouseX
            self.ycord = mouseY
                
''' 
grafo conttiene los vertices

matrizGrafo es la matriz del grafo
'''        
grafo = []
matrizGrafo = []

'''
arbol, matriz del arbol
'''
arbol = []
def busquedaBinaria(buscando):
    global arbol,process
    ruta = []
    raiz = arbol[0][1]
    #print(1)
    q = 0
    encontrado = True
    while(encontrado):
        print(raiz,arbol[buscando][1])
        if(arbol[buscando][1] == raiz):
            ruta.append(raiz)
            print(ruta)
            encontrado = False
        if(arbol[buscando][1] > raiz):
            for i in aristas:
                print(i[1],q)
                if(i[1] == q):
                    if(arbol[i[2]][1] > raiz):
                        ruta.append(raiz)
                        raiz = arbol[i[2]][1]
                        q = i[2]
                        
                if(i[2] == q):
                    if(arbol[i[1]][1] > raiz):
                        ruta.append(raiz)
                        raiz = arbol[i[1]][1]
                        q = i[1]
        if(arbol[buscando][1] < raiz):
            for i in aristas:
                if(i[1] == q):
                    if(arbol[i[2]][1] < raiz):
                        ruta.append(raiz)
                        raiz = arbol[i[2]][1]
                        q = i[2]
                        
                if(i[2] == q):
                    if(arbol[i[1]][1] < raiz):
                        ruta.append(raiz)
                        raiz = arbol[i[1]][1]
                        q = i[1]
    process = False    
        
        
def colores():
    global process,grafo,aristas
    mColor = []
    vColor = []
    for i in grafo:
        mColor.append([i[1],i[2]])

    for i in range(0,len(mColor)):
        for j in range(0,len(mColor)-1):
            if(mColor[j][1] < mColor[j+1][1]):
                temp = mColor[j]
                mColor[j] = mColor[j+1]
                mColor[j+1] = temp
    
    print(mColor)
    for i in mColor:
        colorss  = 0
        for j in aristas:
            if(i[0] == j[1]):
                if(estaz(j[2],vColor,colorss) == False):
                    colorss += 1

            if(i[0] == j[2]):
                if(estaz(j[1],vColor,colorss) == False):
                    colorss += 1
        vColor.append([i[0],colorss])
    print(vColor)
    
    process = False       

def estaz(x,vColor,colorss):
    for i in vColor:
        if((x == i[0] and i[1] == colorss) or x == i[0]):
            return False
    return True
    
def look(vFinal,vInit):
    global nodosA,grafos,nodosB
    result = True
    nodosBusqueda = ''
    totalD = 0
    nodosA = []
    nodosB = []
    asd = 0
    nodoRefence = vInit
    x = 0

    for i in aristas:
            if(i[1] == grafo[vInit][1] and estai(i[2])):
                nodosA.append([i[4],[i[2],grafo[vInit][1]]])
                nodosB.append(grafo[vInit][1])
                
            if(i[2] == grafo[vInit][1] and estai(i[1])):
                nodosA.append([i[4],[i[1],grafo[vInit][1]]])
                nodosB.append(grafo[vInit][1])
    j = 0
    sigue = True
    while(sigue):
        for i in aristas:
            print(nodosA[j][1][0])
            if(i[1] == nodosA[j][1][0] and estai(i[2])):
                nodosA.append([i[4]+ nodosA[j][0],[i[2],nodosA[j][1]]])
                nodosB.append(nodosA[j][1][0])
                
            if(i[2] == nodosA[j][1][0] and estai(i[1])):
                nodosA.append([i[4]+ nodosA[j][0],[i[1],nodosA[j][1]]])
                nodosB.append(nodosA[j][1][0])
                
            if(nodosA[j][1][0] == vFinal):
                sigue = False
        j += 1
    temp = 99999
    pos = -1
    for i in range(len(nodosA)):
        if(nodosA[i][0] < temp and nodosA[i][1][0] == vFinal):
            pos = i
            temp  = nodosA[j][0]
            
    print('El camino menor es',nodosA[pos][1],' distancia: ',nodosA[pos][0])
                            
    
def estai(buscando):
    for j in nodosB:
        if(j == buscando):
            return False
    return True
        
def mouseClicked():
    global graph, matrizGrafo, grafo,aristas,number,tree
    if(graph):
        if(key == 'x'):
            graph = False
            grafo = []
            matrizGrafo = []
            aristas = []
            number = -1
        if(process == False):
            global number,grafo,mC,matrizGrafo
            x = mouseX
            y = mouseY 
            number += 1
            matrizGrafo.append([0]*number)
            for i in range(len(matrizGrafo)):
                matrizGrafo[i].append(0*number)
            grafo.append([vertice(x,y,number,color(245, 0, 135)),number,0])
            mC = True 
    if(tree):
        global number,arbol
        if(key == 'z'):
                tree = False
                arbol = []
                aristas = []
                
        if(process == False):
            x = mouseX
            y = mouseY 
            number += 1
            value = int(random(100))
            arbol.append([vertice(x,y,value,color(245, 0, 135)),value])
            mC = True 


def setup():
    size(900,600)      
                        
def draw():
    global posX1, posX2, posY1, posY2, start,graph,tree,textG,textT,mC,j,number,process
    
    if(graph == False and tree == False):
        background(65, 151, 217)  
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
        if(mouseX <= 200 and mouseX >= 100 and mouseY <= 375 and mouseY >= 300):
            fill(120)
            stroke(0)
            rect(100, 300, 100, 75)
            fill(0)
            textSize(20)
            text(textG, 120, 340)
            
            if(mousePressed):
                graph = True
    
        if(mouseX <= 420 and mouseX >= 320 and mouseY <= 375 and mouseY >= 300):
            fill(120)
            stroke(0)
            rect(320, 300, 100, 75)
        #Texto de la segunda opción
            fill(0)
            textSize(20)
            text(textT, 350, 340)
            if(mousePressed):
                tree = True
                
    if(graph):       
        background(2)
        textSize(20)
        noStroke()
        fill(255)
        text("Click para crear vertice",0,20)
        text("Click derecho para mover vertice",0,40)
        text("Click izquierdo y tecla: B para crear arista",0,60)
        text("Tecla: A para borrar vertice",0,80)
        text("Tecla: F  y tecla: G Ruta mas corta",0,100)
        text("Tecla: D para grafo colorado",0,120)
        
        
        if(mC):
            for i in grafo:
                i[0].display()
                
        for i in range(0,len(grafo)):
            j = i
            if(i < len(grafo)):
                if(grafo[i][0].on(i)):
                    number -=1
                    for h in range(len(matrizGrafo)):
                        matrizGrafo[h].pop(i)
                    break
            
        for i in range(len(aristas)):
            aristas[i][0].display2(i)
            aristas[i][4] = distances
            
        if (process == True and busqueda == False):
            for i in range(len(grafo)):
                grafo[i][0].onProcess(i)
                
        if (process == True and busqueda  == True):
            for i in range(len(grafo)):
                grafo[i][0].processLook(i)
                
    if(tree):       
        background(2)
        if(mC):
            for i in arbol:
                i[0].display()
                
        for i in range(0,len(arbol)):
            j = i
            arbol[i][0].on(i)
            
            
        if (process == True):
            for i in range(len(arbol)):
                arbol[i][0].onProcess(i)
                
        for i in range(len(aristas)):
            aristas[i][0].display2(i)

                
                                
                                                
'''
Comentarios finales

1.En arboles, se dejo la distancia entre nodos para ahorrar codigo

2. Para salir de grafos es x y click, y persionar otra tecla
3. Para salir de arboles es z y click y presionar otra tecla
para buscar en un arbol la ruta a un nodo ordenado, es sobre el nodo a buscar y la letra P


'''                
