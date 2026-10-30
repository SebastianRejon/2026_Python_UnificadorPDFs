import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter, PdfReader
#
ruta_entrada=r"C:\Users\sebastian.rejon\Desktop\Nueva carpeta"
ruta_salida=r"C:\Users\sebastian.rejon\Desktop\salidaPDF\completito.pdf"
nombre_salida="completito.pdf"
archivos=[]
#
def captura_archivos():
    for nombre in os.listdir(ruta_entrada):
        ruta_completa=os.path.join(ruta_entrada, nombre)
        if os.path.isfile(ruta_completa):
            archivos.append(ruta_completa)          

# itero para unir
# doble bucle para archivos con hojas dentro
def mergear():
    escritor=PdfWriter()
    for archivo in archivos:    
        lector=PdfReader(archivo)
        for hoja in lector.pages:
            escritor.add_page(hoja)

    # guardo el compilado
    with open(ruta_salida, "wb") as f:
        escritor.write(f)        
    print("fijate si salio!!!!")
#
def gui():
    ventana=tk.Tk()
    ventana.title="Unficador PDF's"
    ventana.geometry("600x200")
    
    ventana.mainloop()
#principal
gui()
captura_archivos()
mergear()
 