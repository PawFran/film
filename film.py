class Film:
    def __init__(self, title = "", polish_title = "", year = 0, link = "", country = "", genre = ""):
        self.polish_title = polish_title
        self.year = year
        self.link = link
        self.title = title
        self.country = country
        self.genre = genre

    def __str__(self):
        s = "title: " + self.title
        s += ", polish_title: " + self.polish_title
        s += ", year: " + str(self.year)
        s += ", link: " + self.link
        s += ", country: " + str(self.country)
        s += ", genre: " + str(self.genre)

        return s


