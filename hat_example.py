class Hat(object):

    def __init__(self, pattern, color):
        self.pattern = pattern
        self._color = color
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._price = value

    def __str__(self):
        return "Let's make a %s %s" % (self.color, self.pattern)

class Chullo(Hat):
   
    def __init__(self, pattern, color):
        Hat.__init__(self, pattern, color)
        self.has_earflaps = True

llama = Chullo("Knitty.com Swell", "blue")
print(llama)
print(llama.color)
print(llama.has_earflaps)
