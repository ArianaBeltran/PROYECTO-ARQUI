import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conexión y creación de tabla si no existe
conn = sqlite3.connect("notas.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        contenido TEXT NOT NULL
    )
""")
conn.commit()

# Función para guardar nota
def guardar_nota():
    titulo = entry_titulo.get()
    contenido = text_contenido.get("1.0", tk.END)
    if titulo.strip() == "" or contenido.strip() == "":
        messagebox.showwarning("Advertencia", "Debe llenar ambos campos")
        return
    cursor.execute("INSERT INTO notas (titulo, contenido) VALUES (?, ?)", (titulo, contenido))
    conn.commit()
    entry_titulo.delete(0, tk.END)
    text_contenido.delete("1.0", tk.END)
    cargar_notas()

# Función para cargar notas en la lista
def cargar_notas():
    listbox_notas.delete(0, tk.END)
    cursor.execute("SELECT id, titulo FROM notas")
    for nota in cursor.fetchall():
        listbox_notas.insert(tk.END, f"{nota[0]}. {nota[1]}")

# Función para ver contenido de una nota
def ver_nota(event):
    seleccion = listbox_notas.curselection()
    if seleccion:
        item = listbox_notas.get(seleccion[0])
        nota_id = item.split(".")[0]
        cursor.execute("SELECT contenido FROM notas WHERE id=?", (nota_id,))
        contenido = cursor.fetchone()[0]
        text_contenido.delete("1.0", tk.END)
        text_contenido.insert(tk.END, contenido)

# Interfaz
ventana = tk.Tk()
ventana.title("Notas Personales")

entry_titulo = tk.Entry(ventana, width=40)
entry_titulo.pack(pady=5)

text_contenido = tk.Text(ventana, height=10, width=50)
text_contenido.pack(pady=5)

btn_guardar = tk.Button(ventana, text="Guardar Nota", command=guardar_nota)
btn_guardar.pack(pady=5)

listbox_notas = tk.Listbox(ventana, width=50)
listbox_notas.pack(pady=5)
listbox_notas.bind("<<ListboxSelect>>", ver_nota)

cargar_notas()
ventana.mainloop()

