widthImg=500
heightImg=500
j=0 #indice array pixel
i=0 #indice array frase
o=0
latopixel=50 #lunghezza lato di un pixels
grandezza_immagine=latopixel*10 # grandezza del lato dell'immagine
widthpixel=50
heightpixel=50


def setup():
    background(0)
    size(grandezza_immagine,grandezza_immagine) #grandezza immagine
    frase= input("Inserisci la frase")
    disegna()
    
#Finestra di input della frase
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def disegna():
    global img,r,g,b,mess,i,j,o
    img.loadPixels()
#Lunghezza del messaggio
    lunghezzatesto=len(messaggio)
    while(i<lunghezzatesto):
         if(i<lunghezzatesto):
             r=ord(messaggio[o])
         else:
             r=255
         if(o+1<lunghezzatesto):
             g=ord(messaggio[o+1]
         else:
             g=255
         if(o+2<lunghezzatesto):
             b=ord(messaggio[o+2]
         else:
             b=255
        o=o+3
        
        #Ciclo per mettere i colori all'interno dell'immagine
        for i in range(widthpixel):
            for j in range(heightpixel):
                
    
    
