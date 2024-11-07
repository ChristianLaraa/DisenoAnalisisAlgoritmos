import tkinter as tk
def saludar():
    print('Hola, Buenos dias a todos')

ventana = tk.Tk() #Clase principal de Tk
ventana.title("ventana de prueba") #cambiar el tirulo de la ventana se llama la funcion con el punto "."
ventana.geometry("460x700") #modificar dimensiones de la ventana
etiqueta1 = tk.Label(ventana, text='Hola Mundo')
etiqueta1.pack() #se debe empaquetar para que se pueda visualizar
boton1 = tk.Button(ventana, text='Saluda', command=saludar)
boton1.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()
ventana.mainloop()
