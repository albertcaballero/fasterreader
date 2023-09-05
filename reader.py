import tkinter as tk
import time

i = 0
speed = 1

def reset():
	global i
	i = 0;
	word.config(text="")

def get_speed(val):
	global speed
	speed = int(val)/1.73

def reader():
	global i, speed
	print (int(300*(1/speed)))
	text = entry.get(1.0, 'end')
	list = text.split()
	if (i < len(list)):
		word.config(text=list[i])
		i += 1
		window.after(int(300*(1/speed)), reader)
	return
	# if (i == len(list)):
	#  	i = 0

window = tk.Tk()
window.geometry("400x400")
window.title("A faster Reader")
entry = tk.Text(window, relief="groove", height=5, wrap="word")
entry.pack(pady=10)
tk.Button(window, text="go", command=reader).pack(pady=10)
tk.Button(window, text="reset", command=reset).pack(pady=2)
speed_scale = tk.Scale(window, orient="horizontal", command=get_speed, from_=1, to=5)
speed_scale.pack(pady=10)
word = tk.Label(window, text="")
word.pack(pady=10)

window.mainloop()