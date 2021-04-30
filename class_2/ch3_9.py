class parent:
    def sing(self):
        print("sing a song")

class LuckyChild(parent):
    pass

luckyboy = LuckyChild()
luckyboy.sing()