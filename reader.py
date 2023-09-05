import tkinter as tk

def reader(list):
	i = 0
	print (len(list))
	while (i < len(list)):
		word.config(text=list[i])
		print (list[i])
		i += 1

def start():
	text = entry.get()
	print (text)
	list = text.split()
	reader(list)

window = tk.Tk()
window.geometry("400x400")
window.title("A faster Reader")
window.configure(bg='green')
entry = tk.Entry(window, relief="groove", background="blue")
entry.pack(pady=10)
tk.Button(window, text="go", command=start).pack(pady=10)
word = tk.Label(window, text="")
word.pack(pady=10)

window.mainloop()