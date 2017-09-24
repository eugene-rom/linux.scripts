import argparse, os, json, pafy, pydub

#argparse settings and some variables.
homepath='/home/{}'.format(os.environ['LOGNAME'])
profilepath=homepath+'/.mozilla/firefox/RANDOM.default/sessionstore-backups/recovery.js'

parser  =argparse.ArgumentParser()
parser.add_argument('-musicpath', default=homepath+'/Music')
parser.add_argument('-videopath', default=homepath+'/Videos')
parser.add_argument('-mp4', action='store_true')
parser.add_argument('-mp3', action='store_true')
parser.add_argument('-both', action='store_true')
parser.add_argument('-ytc',  action='store_true')#finds the currently opened YouTube page and downloads it.saves time
parser.add_argument('-yt')                                      #user gives a link to app. giox -yt <LINK> -mp3/-mp4/-both
parser=parser.parse_args()

#finds the currently opened YouTube page.
def findTheYoutube(profilepath):
    with open(profilepath, "r") as f:
        jdata = json.loads(f.read())

    for win in jdata.get("windows"):
        for tab in win.get("tabs"):
            i = tab.get("index") - 1
            if 'https://www.youtube.com' in tab.get("entries")[i].get("url"):
                print('[+] URL FOUND!')
                return tab.get('entries')[i].get('url')
            else:
                continue
#downloads the video.
def downloadYoutube(link):
    video=pafy.new(link)
    print('[?] DOWNLOADING THE {}'.format(video.title))
    if parser.mp4 or parser.both:
        videov=video.getbest()
        videov.download(filepath=parser.videopath, quiet=False)
    if parser.mp3 or parser.both:
        audio=video.getbestaudio()
        audio.download(filepath=parser.musicpath, quiet=False)
    print('[+] SUCCESSFULLY DOWNLOADED!')

    if parser.mp3 or parser.both:
        audioname=parser.musicpath+'/'+audio.title+'.'+audio.extension
        audiofile=pydub.AudioSegment.from_file(audioname, format=audio.extension)
        audiofile.export(parser.musicpath+'/'+audio.title+'.mp3', format='mp3')
        os.system('rm {}'.format('"'+audioname+'"'))
        print('[+] SUCCESSFULLY CONVERTED!')

if __name__=='__main__':
    if parser.ytc:
        downloadYoutube(findTheYoutube(profilepath))
    if parser.yt:
        downloadYoutube(parser.yt)
