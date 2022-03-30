"""
Lab 3_6. Notebook
"""
from datetime import datetime
from numpy import random


class Notebook():
    def __init__(self) -> None:
        self.notes = []
    
    def search(self, filter):
        if len(self.notes) != 0 :
            return [str(x) for x in self.notes if filter in x.tags]
        return "No notes with such tag"
    
    def new_note(self, memo, tags = ""):
        self.notes.append(Note(memo, tags))
    
    def find_note_by_id(self, note_id):
        try :
            return self.notes.index([x for x in self.notes if x.id == note_id][0])
        except ValueError:
            return "No notes with such id"
    
    def modify_memo(self, note_id, memo):
        to_change = self.find_note_by_id(note_id)
        self.notes[to_change].memo = memo
    
    def modify_tags(self, note_id, tags):
        to_change = self.find_note_by_id(note_id)
        self.notes[to_change].tags = tags

class Note():
    def __init__(self, memo, tags) -> None:
        self.memo = memo
        self.creation_date = datetime.now().strftime("%H:%M:%S")
        self.tags = tags
        self.id = str(random.randint(11111111, 99999999))
    
    def __repr__(self) -> str:
        return f"Note<{self.creation_date}_{self.id}>"


