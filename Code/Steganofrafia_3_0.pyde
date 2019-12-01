larghezzaImg=500
altezzaImg=500

#Indici per scorrere l'array
i=0
j=0
o=0 
p=0 

larghezzapixel=500
altezzapixel=500

def setup():
    global img,mess,larghezzapixel,altezzapixel
    #Messaggio che compare dopo che si esegue il programma
    mess=input ("Inserisci la tua frase")
    size(500, 500)
    crea()
    
#Finestra di input per la frase
def input(message=""):
    from javax.swing import JOptionPane 
    return JOptionPane.showInputDialog (frame,message)

    
def crea():
    global img,r,g,b,mess,p,o,i,j
    img=createImage(larghezzaImg,altezzaImg,RGB)
    img.loadPixels() #Trasforma l'immagine in un array di pixels
    
    while i < (len(mess)): #scorre i caratteri della frase
        if (o<len(mess)):
            r=ord(mess[o])
        else:
            r=255 #se non c'è un colore si carica qui
        if (o+1<len(mess)):
            g=ord(mess[o+1])
        else:
            g=255
        if (o+2<len(mess)):
            b=ord(mess[o+2])
        else:
            b=255
        o=o+3
        
        #Ciclo per inserire i colori nell'immagine
        for i in range(larghezzapixel): #colonne
            for j in range(altezzapixel): #righe
                img.pixels[p+j+(larghezzaImg*i)]= color(r,g,b) # Metto a ogni pixel il suo colore
        p=p+larghezzapixel # Faccio 50 volte la stessa cosa
        
        
        
        print r
        print g
        print b
    img.updatePixels() #carico i pixels
    image(img,0,0)
