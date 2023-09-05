import tkinter as tk

i = 0
interval = 300

def reset():
	global i
	i = 0;
	word.config(text="")

def wpm_to_ms():
	global interval
	wpm = int(wpm_box.get())
	interval = int(1/(wpm/60)*1000)

def reader():
	global i, interval
	wpm_to_ms()
	text = entry.get(1.0, 'end')
	list = text.split()
	if (i < len(list)):
		word.config(text=list[i])
		i += 1
		window.after(interval, reader)
	return

window = tk.Tk()
window.geometry("400x400")
window.title("A faster Reader")
entry = tk.Text(window, relief="groove", height=8, wrap="word")
entry.pack(pady=10)
wpm_box = tk.Entry(window, width=6)
wpm_box.pack(pady=5)
tk.Button(window, text="go", command=reader).pack(pady=10)
tk.Button(window, text="reset", command=reset).pack(pady=2)
word = tk.Label(window, text="", font="arial 22")
word.pack(pady=20)

window.mainloop()