import pyglet
import tree

game_window = pyglet.window.Window()

pts = []
segments_iterator = tree.main()

@game_window.event
def on_draw():
    game_window.clear()
    pyglet.graphics.draw(len(pts)/2, pyglet.gl.GL_LINES, ('v2f', tuple(pts)))

def update(dt):
    #global pts
    #pts = []
    for s in segments_iterator.next():
        pts.append( s.start.x)
        pts.append( s.start.y)
        pts.append( s.end.x)
        pts.append( s.end.y)

i = [0]

def capture_screen(dt):
    pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot_%s.png' %(i[0]))
    i[0] += 1

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 0.2)
    pyglet.clock.schedule_interval(capture_screen, 0.4)
    pyglet.app.run()
