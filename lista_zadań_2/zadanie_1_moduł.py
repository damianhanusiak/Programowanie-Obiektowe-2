import datetime


class Note(object):
    Id = 0

    def __init__(self, text, tag):
        Note.Id += 1
        self.ID = Note.Id
        self.tag = tag
        self.text = text
        self.data = datetime.datetime.now()

    def match(self, fraza):
        if (fraza in self.tag) or (fraza in self.text):
            return True
        else:
            return False

    def __str__(self):
        return f"\nId: {self.ID}\t\t\tData: {self.data}\n\tTag:\t\t\t{self.tag},\n\tText:\t\t\t{self.text}"


class Notebook(object):

    def __init__(self):
        self.notes = []

    def new_note(self, ob):
        self.notes.append(ob)

    def modify_text(self, id, text):
        for i in self.notes:
            if i.ID == id:
                i.text = text
                break

    def modify_tag(self, id, tag):
        for i in self.notes:
            if i.ID == id:
                i.tag = tag
                break

    def search(self, fraza):
        znalezione = []
        for i in self.notes:
            if i.match(fraza):
                znalezione.append(i)
        return znalezione

    def __str__(self):
        all = ""
        for i in self.notes:
            all += i.__str__()
        return all
