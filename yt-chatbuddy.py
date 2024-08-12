from os import popen,system,path 
from subprocess import run
from pytchat import create
from time import sleep
#import obspython as obs
from random import choice
def tts(id):
    mic_id = popen("pactl list sinks short | grep anime | grep -o '^.'").read().split('\n')[0]
    print(len(mic_id))
    if len(mic_id) == 0:
        system("pactl load-module module-null-sink sink_name=anime sink_properties=device.description=anime")
        mic_id = popen("pactl list sinks short | grep anime | grep -o '^.'").read()
    else:
        print("anime voice channel exists")
    chat = create(video_id=id)
    while True:
        for c in chat.get().sync_items():
            msg = c.message.replace('"',"'")
            usr = c.author.name

            with open(f'{path.dirname(path.realpath(__file__))}/chat.txt','w') as txt:
                txt.write(msg)
            with open(f'{path.dirname(path.realpath(__file__))}/usr.txt','w') as txt:
                txt.write(f'{usr} says:')
            print(acc,tmp)
            print(f"{c.author.name}:\n {msg}")
            popen(f'espeak -d {mic_id} -a 200 -v en+f5 "{msg}"')


if __name__ == '__main__':
    link = input()
    tts(link.split("/")[-1].split("?")[0])
