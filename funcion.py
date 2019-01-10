import cv2


RESIZE_RATIO = 0.6


#le pasamos el archivo de texto que vamos a leer, con "with" para que python automaticamente
# pueda cerrar el archivo cuando no se este usando, leemos linea por linea el documento.
with open ('C:/PROYECTO FINAL/configuracion.txt', encoding = 'utf-8') as a_file:
    rutaVideo = a_file.readline().strip()
    param = a_file.readline().strip()
    param2 = a_file.readline().strip()
    param3 = a_file.readline().strip()   
    

#Lectura de la ruta especifica 
cap = cv2.VideoCapture(rutaVideo)


def redimensiona_frame():
    " Grabs a frame from the video capture and resizes it. "
    rval, frame = cap.read()
    if rval:
        (h, w) = frame.shape[:2]
        frame = cv2.resize(frame, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
        
        #print("Esto vale h: ", h, "Esto vale w: ", w)
    return rval, frame

#Funcion realizada para el conteo
def conteo(y, ent):
    if (ent-y<11 and y<ent):
        return 1
    else:
        return 0

#Hayar centroide de los rectangulos (Funciona mejor con el otro metodo)
def centroide(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1

    return (cx, cy)


#Otra forma de sacar el centroide de los rectangulos.
    #center = (int(x+w/2), int(y+h/2))