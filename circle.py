from PIL import Image, ImageDraw
import math

img = Image.new(mode='RGB', size=(16000, 16000), color='white')
draw = ImageDraw.Draw(img)

def middle(p1, p2):
	return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

class Triangle:
	p1 = None
	p2 = None
	p3 = None
	iteration = None

	def __init__(self, p1, p2, p3, iteration = 0):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		
		self.m1 = middle(self.p2, self.p3)
		self.m2 = middle(self.p1, self.p3)
		self.m3 = middle(self.p1, self.p2)
		
		self.iteration = iteration

	def draw(s):		
		draw.line((s.m1, s.m2), fill='black', width=0)
		draw.line((s.m2, s.m3), fill='black', width=0)
		draw.line((s.m3, s.m1), fill='black', width=0)

	def new(s):
		if(s.iteration > 0):
			return [Triangle(s.p1, s.m2, s.m3, s.iteration - 1), 
					Triangle(s.p2, s.m1, s.m3, s.iteration - 1),
					Triangle(s.p3, s.m1, s.m2, s.iteration - 1)]
		else:
			return []

q = [Triangle((0, 15999), (15999, 15999), (8000, 0), 7)]

draw.line((q[0].p1, q[0].p2), fill='black', width=0)
draw.line((q[0].p2, q[0].p3), fill='black', width=0)
draw.line((q[0].p3, q[0].p1), fill='black', width=0)

for t in q:
	t.draw()
	q += t.new()	

#for x in range(0, img.width):
#	for y in range(0, img.height):
#		if math.sqrt((x - 200) * (x - 200) + (y - 200) * (y - 200)) < 150:
#			img.putpixel((x, y), (0, 0, 0, 255))

img.save("triangle.png")
#img.show()
