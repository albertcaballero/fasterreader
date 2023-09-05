import tkinter as tk

def start():
	text = entry.get()
	print (text)

window = tk.Tk()
window.geometry("400x400")
window.title("A faster Reader")
window.configure(bg='green')
entry = tk.Entry(window, relief="groove", background="blue")
entry.pack(pady=10)
tk.Button(window, text="go", command=start).pack(pady=10)

window.mainloop()