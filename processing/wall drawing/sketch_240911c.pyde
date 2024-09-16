def setup():
    size(600,600)
    
def draw():
    pass
    
def keyPressed():
    if key == "1":
        for i in range(0,24):
            stroke(255,255,255)
            line(300,300,random(0,600),random(0,600))
        
    if key == "2":
        for i in range(0,12):
            stroke(255,255,255)
            line(0,300,random(0,600),random(0,600))
            line(300,0,random(0,600),random(0,600))
            line(300,600,random(0,600),random(0,600))
            line(600,300,random(0,600),random(0,600))
    
    if key == "3":
        for i in range(0,12):
            stroke(255,255,255)
            line(0,0,random(0,600),random(0,600))
            line(600,0,random(0,600),random(0,600))
            line(0,600,random(0,600),random(0,600))
            line(600,600,random(0,600),random(0,600))
            
    if key == "4":
        background(0)
            
            
        
        
