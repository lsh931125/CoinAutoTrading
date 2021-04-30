class parent:
    def sing(self):
        print("sing a song")

class LuckyChild(parent):
    def dance(self):
        print("shuffle dance")

luckyboy = LuckyChild()
luckyboy.sing()
luckyboy.dance()