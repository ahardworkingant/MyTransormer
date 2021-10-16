class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.Name = name
        self.Typing = typing
        self.Reflection = reflection
        self.Year = year
    def is_dynamic(self):
        if self.Typing == "Dynamic":
            return True
        else:
            return False
    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.Name, self.Typing, self.Reflection, self.Year)


