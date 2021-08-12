import os, re, site
from random import choice
from subprocess import Popen, run

import filetype as ft

from sl4ng import pop, show, getsource, shuffle, flatten, freq
from filey import Place, Library, forbiddens, ffplay, shortcuts as commons, convert, files
from pyperclip import copy, paste
from pprint import pprint 


this = __file__
here = os.path.dirname(this)
settings_file = os.path.join(here, "settings.json")
lockouts = [
    'NTUSER.DAT',
    "ntuser.dat.LOG1",
    'ntuser.dat.LOG2',
]
mysh = shuffle(files(r"C:\Users\Kenneth\Documents\bounces\orchidean"))

def load_settings():
    global settings, defaultdir, settings_file
    import json
    if os.path.exists(settings_file):
        # settings = json.load(settings_file)
        with open(settings_file, "r") as fob:
            return json.load(fob)
    return {}
def save_settings():
    global settings
    import json
    with open(settings_file, "w") as fob:
        json.dump(settings, fob)
    
settings = load_settings()
defaultdir = d if (d:=settings.get("default_directory")) else os.getcwd()
      
# if :
#     load_settings()
# os.chdir("f:/ytdls")
os.chdir(defaultdir)
pwd = Place(os.getcwd())

def get_formats(walk=False) -> dict:
    formats = {
        "audio": [],
        "video": [],
        "other": []
    }
    # exts = lambda: [*val for val in formats.values()]
    exts = lambda: flatten(formats.values())
    itr = files(os.getcwd()) if walk else os.listdir()
    for file in filter(lambda x: not x in lockouts, filter(os.path.isfile, itr)):
        if not (ext:=os.path.splitext(file)[1]) in exts():
            kind = ""
            if ext == ".m4a":
                kind = "audio"
            elif ext == ".part":
                kind = "other"
            elif ft.audio_match(file):
                kind = "audio"
            elif ft.video_match(file):
                kind = "video"
            else:
                kind = "other"
            formats[kind].append(ext)
    return formats
formats = get_formats()
play_once = lambda path: [print(path), ffplay(path, loop=0)]

def ff(path=None):
    path = cpr() if isinstance(path, type(None)) else path
    while 1:
        while not len(input("Play?\n\t")):
            path = cpr()
        ffplay(path, loop=0)
        if len(input("Delete?\n\t")):
            rm(path)
        elif len(input("Sample?\n\t")):
            smp(path)
        path = cpr()

def rm(path=None):
    path = paste() if isinstance(path, type(None)) else path
    os.remove(path)

def smp(path=None):
    path = paste() if isinstance(path, type(None)) else path
    os.rename(path, os.path.join("samples", path))

def cpr():
    ext = lambda path: os.path.splitext(path)[1]
    # name = choice([*filter(os.path.isfile, os.listdir())])
    # name = choice([*filter(ft.audio_match, filter(os.path.isfile, os.listdir()))])
    # while not ft.audio_match(name:=choice([*filter(os.path.isfile, os.listdir())])):
    while not ext(name:=choice([*filter(os.path.isfile, os.listdir())])) in formats["audio"]:
        pass
    copy(name)
    print(name)
    return name

root = Place(commons['home'])

musearch = Library(
    root['music'],
    root['downloads']['music'],
)

def clear() -> None:
    Popen('clear')
    sleep(.2)
def cls() -> None:
    clear()
    show(map(repr, cd), head=False, tail=False)
def cd(path:str=None) -> None:
    global pwd, formats
    if isinstance(path, type(None)):
        path = os.getcwd()
    os.chdir(path)
    pwd.path = path
    formats = get_formats()


pat = re.compile('^\.|^ntuser.dat|^_', re.I)



def findartists(artists):
    if artists=='*':
        for d in musearch:
            d = Place(d) 
            if re.match('videos', d.name, re.I):
                for f in d['music']['singles'].leaves:
                    if re.match('audio|video', f.kind, re.I):
                        yield f.path
            else:
                for p in d:
                    for f in p.leaves:
                        if not re.match('some assembly required|123 mix', f.path, re.I):
                            if re.match('audio|video', f.kind, re.I):
                                yield f.path
    else:
        rei = 0 if any(map(str.isupper, artists)) else re.I
        sep = max(forbiddens.replace('/', '')+',', key=lambda c: freq(c, artists))
        pat = '|'.join(re.escape(i.strip().replace('/', os.sep)) for i in artists.split(sep))
        print(pat+'\n\n')
        for d in musearch:
            d = Place(d) 
            for f in d.leaves:
                if re.search(pat, f.path, rei):
                    yield f.path
    
def playlist(artists:str, shuf:int=1, rep:int=float('inf')):
    """
    Create a playlist from the results of a search
    """
    results = filter(ft.audio_match, findartists(artists))
    playlist = sorted(results)
    tracks = (playlist, shuffle(playlist))[shuf]
    
    play(tracks, shuf=shuf, rep=rep)
    
def playfrom(path:str, shuf:int=1, rep:int=float('inf')):
    """
    Create a playlist from a directory
    """
    results = filter(ft.audio_match, files(path))
    playlist = sorted(results)
    tracks = (playlist, shuffle(playlist))[shuf]
    
    play(tracks, shuf=shuf, rep=rep)
    
def play(tracks:list[str], shuf:int=1, rep:int=float('inf'), hide=True):
    print(f"{shuf=}\n{rep=}")
    if len(tracks):
        show(tracks, enum=True)
        while rep+1:
            ffplay(tracks, randomize=False, loop=False, hide=hide)
            rep -= 1
    else:
        raise Exception("Nothing was found")




if __name__ == '__main__':
    mysh = {
        r"C:\Users\Kenneth\Documents\bounces\orchidean\bisto_75^1_10_2_38-crashed1_15.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\06 The Delusion Of Liberty.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\01 jesslem-juliet-selfmaster-jesslemusics@gmail.com.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\broken_wagon_49.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\01 Klaar.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\01 Everything Is Rationable.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\New folder\mount kimbie - marilyn edit.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\New folder\cd_music-plot-sb_anthem-edit-12.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\harry_griffiths-distilled-edit_31.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\01 Oh.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\fakie blips_22-crshrcvr_2-short.mp3",
        r"C:\Users\Kenneth\Documents\bounces\orchidean\bleeding_heart-master.mp3",
    }
    mysh = shuffle(mysh)
    
    
    artists = r'floating points: pangaea: luso'
    artists = 'alice coltrane, aging, yussef kamaal, floating points, taylor mcferrin, filoxiny'.replace(',',':')
    artists = "doorbells/ambitions: automine:elephantitis:charles"
    artists = 'music for the uninvited'
    artists = 'crooklyn: melanie'
    artists = 'thaw cycle.mp3: passed tomorrows: wait for you'
    # artists = ""
    # artists = 'saturn' #need a new rip
    # artists = 'getaway: qadir'
    
    # artists = "ascension:noyce/over"
    # artists = "ascension:noyce/over"
    # artists = "albums"
    # artists = "crywank"
    # artists = "charles"
    # artists = "ryan patrick maguire"
    # artists = 'spaceape: milo: slowthai'
    # artists = 'empty 9-volts'
    # artists = 'gold panda,noyce/over,elan tamara,airhead/wait,empty 9-volts,believe - ep, mernau/traces, rahhh/ones,plastic dreams,clark,noyce/devil,noyce/moment,floating points'.replace(',',':')
    
    # artists = 'airhead'.replace(',',':')
    # artists = 'spaceape:  space ape'
    # artists = 'animal collective'
    # artists = 'router:sorcerer'
    # artists = 'aging'
    # artists = 'kode9, las, gantz, loom, objekt, the nativist, unitz, tnght, the chain, tessela'.replace(',',':')
    # artists = 'chaos in the cbd, henry wu, french fries, floating points, pangaea, pearson sound, anz, tyler straub, the chain, spectrasoul, spherique'.replace(',',':')
    artists = r'evenings,gold panda,dominic pierce, alix perez,mernau,youandewan,rahhh,noyce,jafu,kenny segal,taylor mcferrin,floating points,pangaea'.replace(',',':')
    artists = r'dbridge: alix perez: tyler straub'
    artists = 'ascension'
    # artists = 'weirddough:tropes'
    # artists = 'dreamgirl: king krule'
    artists = 'krule'
    artists = 'man_alive'
    # artists = 'ooz'
    # artists = 'dum surfer'
    # playlist(artists)
    
    # results = [*files(r"C:\Users\Kenneth\Downloads\music\drivies\Dsve-20210618T062958Z-001\Dsve\Porcelain")]
    # results = [r"C:\Users\Kenneth\Downloads\music\drivies\Dsve-20210618T062958Z-001\Dsve\Porcelain\03 Porcelain.mp3"]
    # play(results)

    
