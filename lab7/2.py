import pygame
pygame.init()

screen=pygame.display.set_mode((500, 500))
pygame.display.set_caption('Music')

clock=pygame.time.Clock()

done=False

playlist = list()
playlist.append ( "./bruno-major-easily.mp3" )
playlist.append ( "./The Weeknd ft. Daft Punk - Star-boy.mp3" )
playlist.append ( "./knowit.mp3" )


pygame.mixer.music.load(playlist.pop()) 
pygame.mixer.music.set_endevent(pygame.USEREVENT)    
pygame.mixer.music.play() 

image=list()
image.append("./easily500.jpg")
image.append("./starboy500.jpg")
image.append("./sexy500.jpg")

          
img=pygame.image.load(image.pop())


def nextsong():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

def prevsong():
    global playlist
    playlist = [playlist[-1]] + playlist[:-1]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

while not done:
    clock.tick(20)

    music_number=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pygame.mixer.music.stop()
                nextsong()
                image = image[1:] + [image[0]]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_RIGHT:
                pygame.mixer.music.stop()
                prevsong()
                image = [image[-1]] + image[:-1]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key==pygame.K_s:
                pygame.mixer.music.unpause()

        # if event.type == pygame.USEREVENT:    
        #     if len(playlist)>0:       
        #         pygame.mixer.music.queue(playlist.pop())
    
    screen.blit(img, (0, 0))
    pygame.display.flip()
pygame.quit()