import numpy as np
import cv2
import time
import uuid
import sys
import os
import datetime
from funcion import *


#Esto es una megaprueba.
def mainFunction():
    #Aqui tenemos todos los parametros para ajustar el conteo.
    #Nº de px. que debe tener un cuadrado antes de que lo consideremos candidato para el seguimiento.
    BLOB_SIZE = param
    #Facilidad para detectar los pequeños cambios entre el promedio y la escena,
    # Si el nº es más bajo detectará cambios más pequeños.
    THRESHOLD_SENSITIVITY = param2                                                                         
    #Con un numero más alto detectará los cambios con mayor facilidad,
    DEFAULT_AVERAGE_WEIGHT = param3   

    avg = None
    tracked_contornos = []
    w = None
    h = None
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    contadorCoches= 0
    cuentaCentro = 0
 
    
    #Definimos el codec y creamos el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('NuevoVideo.avi', fourcc, 20.0, (width,heigth))
    
  
    while(cap.isOpened()):
    #Llamamos a la función de redimensión para quie nos saque el frame redimensionado.
        grabbed, frame = redimensiona_frame()
        if grabbed == True:
            out.write(frame)
            text = "Carretera sin vehiculos"
        elif grabbed == False:
            print("Video finalizado")
            break
        

    # *********BLOQUE DE FILTROS DE IMAGEN********* 
        frame_time = time.time()
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        (_, _, grayFrame) = cv2.split(hsvFrame)
        grayFrame = cv2.GaussianBlur(grayFrame, (5,5), 0)

        if avg is None:
            # Set up the average if this is the first time through.
            avg = grayFrame.copy().astype("float")
            continue

        cv2.accumulateWeighted(grayFrame, avg, float(DEFAULT_AVERAGE_WEIGHT))
        #cv2.imshow("average", cv2.convertScaleAbs(avg))
        differenceFrame = cv2.absdiff(grayFrame, cv2.convertScaleAbs(avg))

        retval, thresholdImage = cv2.threshold(differenceFrame, int(THRESHOLD_SENSITIVITY), 201, cv2.THRESH_BINARY)
        thresholdImage = cv2.dilate(thresholdImage, None, iterations=2)

    # *********BLOQUE DE DETECCION DE CONTORNOS*********
        m, contornos, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #Filtro para no considerar las pequeñas manchas como vehiculos.
        contornos = filter(lambda c: cv2.contourArea(c) > int(BLOB_SIZE), contornos)

    # *********BLOQUE DE DETECCIÓN DE PIXELES PARA EL CONTEO*********
        for c in contornos:
            area = cv2.contourArea(c)
            #Buscamos las coordenadas para poder dibujar el rectangulo        
            (x, y, w, h) = cv2.boundingRect(c) 
            #A partir de aqui vamos a calcular el centroide.                                    
            centro = centroide(x,y,w,h)
            centroideX = centro[0]
            centroideY = centro[1]
            text = "Trafico ligero"
            
            cv2.rectangle(frame,(x, y), (x + w, y + h),(0,255,0),2)

            vehiculos2 = 'Vehiculos totales: '+str(contadorCoches)
        

            if (conteo(centroideY,300)):
                contadorCoches += 1                               
                
                #print(centroidY, "Numero coches: ",contadorCoches)
            
        #Dibujamos la linea que servirá para contar los vehículos.
        cv2.line(frame,(0,300),(740,300),(0,255,0),3) 
        cv2.putText(frame, "Vehiculos: {}".format(str(contadorCoches)), (10, 332),cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)
        
        cv2.putText(frame, "Estado de la carretera: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 50, 0), int(2))
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 50, 0), 1)                  

        #Mostramos el frame final y finalizamos ejecución.
        cv2.imshow("Seguimiento", frame)
        
    
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        

    
    cap.release()
    out.release()
    #cv2.destroyAllWindows()