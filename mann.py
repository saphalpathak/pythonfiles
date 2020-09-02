from pygame import mixer
def apple(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    apple("audio.ogg","stop")
