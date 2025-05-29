import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import os
import subprocess
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_text(position, text_string):
    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(text_string, True, (255, 255, 255, 255), (0, 0, 0, 255))
    text_data = pygame.image.tostring(text_surface, 'RGBA', True)
    glRasterPos3d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def draw_cube():
    glBegin(GL_QUADS)

    # Front face
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Back face
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Left face
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    # Right face
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Top face
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom face
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glEnd()


def main_menu():
    root = tk.Tk()
    root.title("Main Menu")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky="nsew")

    ttk.Label(main_frame, text="Welcome to the main menu!").grid(row=0, column=0, columnspan=2)

    open_apps_button = ttk.Button(main_frame, text="Open Apps", command=open_apps)
    open_apps_button.grid(row=1, column=0)



    options_button = ttk.Button(main_frame, text="Options")
    options_button.grid(row=1, column=1)

    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=2, column=0, columnspan=2)

    root.mainloop()

def open_apps():
    root = tk.Tk()
    root.title("Open Apps")

    apps = [
        "Timer",
        "Text Editor",
        "Calculator",
        "To-Do List",
    ]
    apps_frame = ttk.Frame(root, padding="10")
    apps_frame.grid(row=0, column=0, sticky="nsew")

    for i, app in enumerate(apps):
        ttk.Button(apps_frame, text=app, command=lambda app=app: open_app(app)).grid(row=i, column=0)


    root.mainloop()

def open_app(app):
    if app == "Timer":
        # open .exe
        try:
            os.startfile("timer.exe")
        except FileNotFoundError:
            messagebox.showerror("Error", "Timer not found")
            return
    elif app == "Text Editor":
        try:
            os.startfile("text_editor.exe")
        except FileNotFoundError:
            messagebox.showerror("Error", "Text Editor not found")
            return
    elif app == "Calculator":
        try:
            os.startfile("calculator.exe")
        except FileNotFoundError:
            messagebox.showerror("Error", "Calculator not found")
            return
    elif app == "To-Do List":
        try:
            os.startfile("todo_list.exe")
        except FileNotFoundError:
            messagebox.showerror("Error", "To-Do List not found")
            return



def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    start_time = pygame.time.get_ticks()
    while True:
        current_time = pygame.time.get_ticks()
        if current_time - start_time > 10000:
            pygame.quit()
            main_menu()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main_menu()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)
        draw_cube()
        draw_text((-0.5, 0.5, 0.5), "3D Animated Intro")
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()
    main_menu()

main()


