import os
import shutil

class  organize:
    file_type={
       'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Programs': ['.py', '.cpp', '.java', '.js'],
    }


    def __init__(self,folder_path):
        self.folder_path=folder_path

    def checkfolder(self):
        if not os.path.exists(self.folder_path):
            return f'{self.folder_path} does not exists'
        
        for file in os.listdir(self.folder_path):
            file_path=os.path.join(self.folder_path,file)
            if os.path.isfile(file_path):
                ext=os.path.splitext(file_path)[1].lower()
                category=self.category(ext)
                self.move_file(file_path,category)

                
    @classmethod
    def category(cls,ext):
        for category,ext_list in cls.file_type.items():
            if ext in ext_list:
                return category
            
        return 'Others'
    
    def move_file(self,file_path,category):
        dest_folder=os.path.join(self.folder_path,category)
        os.makedirs(dest_folder,exist_ok=True)
        shutil.move(file_path,os.path.join(dest_folder, os.path.basename(file_path)))

    def __str__(self):
        return f"FileOrganizer working on: {self.folder_path}"
