if(label_name == 'ss'):
    song = pyglet.media.load('C:/Users/jji19/심민정.m4a')
    print('play start (duration: ',song.duration,')')
    song.play()
    time.sleep(song.duration)
    print('play end')
elif label_name == 'jjy':
    song = pyglet.media.load('C:/Users/jji19/jjy.m4a')
    print('play start (duration: ',song.duration,')')
    song.play()
    time.sleep(song.duration)
    print('play end')
elif label_name == 'Michael':
    song = pyglet.media.load('C:/Users/jji19/마이클씨.m4a')
    print('play start (duration: ',song.duration,')')
    song.play()
    time.sleep(song.duration)
    print('play end')
elif label_name == 'owner':
    song = pyglet.media.load('C:/Users/jji19/owner.m4a')
    print('play start (duration: ',song.duration,')')
    song.play()
    time.sleep(song.duration)
    print('play end')
else:
    pass
