import os
import shutil
import eyed3

folder = os.listdir('ms')
sp = []

for i in folder:
    sp += [i.title().split('.')[0]]

for i in sp:
    shutil.copy2(f'ms/{i}.mp3', f'ms/{i.split(" - ")[1]}.mp3')
    os.remove(f'ms/{i}.mp3')
    treck = eyed3.load(f'ms/{i.split(" - ")[1]}.mp3')
    print(treck)
    treck.tag.artist = f'ms/{i.split(" - ")[0]}'
    treck.tag.save()