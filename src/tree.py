from euclid import Vector2
import math

def rotate_vec2(vector, angle_degrees):
        radians = math.radians(angle_degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = vector.x*cos - vector.y*sin
        y = vector.x*sin + vector.y*cos
        return Vector2(x, y)

class Segment(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vector = self.end - self.start

    def rotate( self, angle ):
        vector = rotate_vec2(self.vector, angle)
        end = self.start + vector
        return Segment( self.start, end)

    def __repr__(self):
        return "Segment(start:%s, end:%s)" %(self.start, self.end)

    def split( self, percentage ):
        """
            takes a segment (a namedtuple with start, end, vector attribute)
            return 2 segments
        """
        split_point =  self.start + (self.vector * percentage)
        before = Segment(self.start, split_point)
        after  = Segment(split_point, self.end)
        return before, after


def step(segments, angle):
    processed = []
    to_process = []
    #for each segment:
    for segment in segments:
        #cut the segment at 2/3
        bottom, top = segment.split( 1/4.)
        #consider this bottom part processed.
        processed.append( bottom )
        #the top 1/3 replace it with two new segments:
        #- the first is angled to the left
        left_branch = top.rotate(angle)
        #- the second is angled to the right.
        right_branch = top.rotate(-angle)
        #put the first and second segment to be processed
        to_process.append( left_branch )
        to_process.append( right_branch )
    return processed, to_process

def repeat(start, nb, angle):
    segments = [start]
    while True:
        processed, to_process = step( segments, angle )
        segments = to_process
        yield processed

def main():
    start = Segment( Vector2(300,0), Vector2(300,600) )
    segments_iterator = repeat(start, 3, 35.0)
    return segments_iterator

if __name__ == "__main__":
    main()


