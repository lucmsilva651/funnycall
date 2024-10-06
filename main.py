import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from pyfiglet import Figlet
import os

# print to terminal (idk why but ill do a figlet here)
f = Figlet(font='standard')
print(f.renderText('lucmsilva'))

print("funnyCall - Made by Lucas Gabriel (lucmsilva)")
print("https://github.com/lucmsilva651/funnycall\n")

def call_boykisser():
    pygame.mixer.music.load('assets/mp3/1928491298.mp3')
    pygame.mixer.music.play()
    messagebox.showinfo("Call: boykisser", "boykisser!")
    print("boykisser!")
    dialog_window = tk.Toplevel(root)
    dialog_window.title("boykisser")
    gif_path = 'assets/gif/1928491298.gif'
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.size
    label = tk.Label(dialog_window, image=None)
    label.pack()
    frames = gif.n_frames
    for i in range(frames):
        gif.seek(i)
        frame = gif.copy().resize((gif_width, gif_height))
        frame_image = ImageTk.PhotoImage(frame)
        label.configure(image=frame_image)
        label.image = frame_image
        dialog_window.update()
        dialog_window.after(100)

def call_fspkchinese():
    pygame.mixer.music.load('assets/mp3/8261562652.mp3')
    pygame.mixer.music.play()
    messagebox.showinfo("Call: frog speaking chinese", "你以下業務出現違規異常，了解詳情請按0， 由華語客服為你服務")
    print("你以下業務出現違規異常，了解詳情請按0， 由華語客服為你服務")
    dialog_window = tk.Toplevel(root)
    dialog_window.title("frog speaking chinese")
    gif_path = 'assets/gif/8261562652.gif'
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.size
    label = tk.Label(dialog_window, image=None)
    label.pack()
    frames = gif.n_frames
    for i in range(frames):
        gif.seek(i)
        frame = gif.copy().resize((gif_width, gif_height))
        frame_image = ImageTk.PhotoImage(frame)
        label.configure(image=frame_image)
        label.image = frame_image
        dialog_window.update()
        dialog_window.after(45)

def button_click(number):
    current_number = entry.get()
    new_number = current_number + str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_number)
    if new_number == '1928491298':
        call_boykisser()
    if new_number == '8261562652':
        call_fspkchinese()
        
def clear_number():
    entry.delete(0, tk.END)
    
def create_button(frame, number):
    button = tk.Button(frame, text=str(number), width=5, height=2,
                       command=lambda: button_click(number))
    button.pack(side=tk.LEFT)

pygame.mixer.init()
root = tk.Tk()
root.title("funnyCall")
entry = tk.Entry(root, width=45)
entry.pack()
button_frame = tk.Frame(root)
button_frame.pack()
for number in range(0, 10):
    create_button(button_frame, number)
root.mainloop()
