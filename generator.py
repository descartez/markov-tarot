import markovify

class Character:
    def __init__(self):
        self.name = ""
        self.bio = ""

    def create_bio(self, name, bio):
        self.name = name
        self.bio = bio

    def create_model(self, file):
        with open(file) as f:
            text = f.read()
        self.model = markovify.Text(text)

    def speak_bio(self):
        print("-"*15)
        print(self.name)
        print(self.bio)
        print("-"*15)

    def speak_tweet(self):
        print(self.model.make_short_sentence(140))

lovecraft = Character()
lovecraft.create_bio("H.P. Lovecraft", "A xenophobic creepy writer.")
lovecraft.create_model("hp_lovecraft_mountains_of_madness.txt")
lovecraft.speak_bio()
lovecraft.speak_tweet()

gaiman = Character()
gaiman.create_bio("Neil Gaiman", "An excellent, empathetic man and writer.")
gaiman.create_model("neil_gaiman_click_clack.txt")
gaiman.speak_bio()
gaiman.speak_tweet()