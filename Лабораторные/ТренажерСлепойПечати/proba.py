import tkinter as tk

# colors for certain characters
colormap = {'b':'blue', 'c':'cyan', 'g':'green', 'm':'magenta', 'o':'orange', 'p':'pink', 'r':'red', 'y':'yellow'}

def on_key(event):
    if event.char in colormap:
        # attach a tag (the character itself) if the character is in the colormap
        event.widget.tag_add(event.char, 'insert-1c')

root = tk.Tk()

text = tk.Text(root)
text.pack()
text.bind('<KeyRelease>', on_key) # on_key() will be executed when a key is pressed inside Text widget
# setup colors for certain characters using tag_config(...)
for c in colormap:
    text.tag_config(c, foreground=colormap[c])

root.mainloop()