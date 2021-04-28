# 객체지향_2
class SuperMario:
    def __init__(self):
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20

mario_p1 = SuperMario()
mario_p2 = SuperMario()
mario_p1.forward()
mario_p2.forward()
print(mario_p1.pos,mario_p2.pos)