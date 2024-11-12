# src/gui.py

import tkinter as tk
from tkinter import messagebox
from src.logico import TaskManager

class TaskManagerGUI:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo para ingresar el título de la tarea
        self.task_title_label = tk.Label(root, text="Título de la tarea:")
        self.task_title_label.pack()
        self.task_title_entry = tk.Entry(root, width=40)
        self.task_title_entry.pack()

        # Campo para ingresar la descripción de la tarea
        self.task_description_label = tk.Label(root, text="Descripción de la tarea:")
        self.task_description_label.pack()
        self.task_description_entry = tk.Entry(root, width=50)
        self.task_description_entry.pack()

        # Botón para agregar la tarea
        self.add_task_button = tk.Button(root, text="Agregar Tarea", command=self.add_task)
        self.add_task_button.pack()

        # Lista de tareas
        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.pack()

        # Botón para marcar la tarea como completada
        self.complete_task_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_task_button.pack()

        # Botón para eliminar la tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack()

        # Actualizar la lista de tareas al inicio
        self.update_tasks_listbox()

    def add_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get()
        if title:
            self.manager.add_task(title, description)
            self.update_tasks_listbox()
            self.task_title_entry.delete(0, tk.END)
            self.task_description_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "El título de la tarea no puede estar vacío.")

    def complete_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            self.manager.complete_task(selected_task)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selección inválida", "Seleccione una tarea para marcarla como completada.")

    def delete_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            self.manager.delete_task(selected_task)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Selección inválida", "Seleccione una tarea para eliminar.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.list_tasks():
            self.tasks_listbox.insert(tk.END, task)

    def get_selected_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            selected_task = self.manager.list_tasks()[selected_index]
            return selected_task.title
        except IndexError:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
