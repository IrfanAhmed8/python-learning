class student:
    def __init__(self,name,id,subjects,grades):
        self.name=name
        self.id=int(id)
        self.subjects=list(subjects)
        self.grades=dict(grades)

    def __str__(self):
     return (f"Name:{self.name},studentid:{self.id},subjects:{self.subjects},grades:{self.grades}")

