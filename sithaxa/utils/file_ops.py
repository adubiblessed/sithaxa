from pathlib import Path

class FileOperations:
    def __init__(self, **kwargs):
        self.file_path = kwargs.get("file_path", None)
        self.folder_path = kwargs.get("folder_path", None)
        self.folder_contents_list = []

    def read_file(self):
        try:
            if self.file_path is None:
                raise ValueError("file_path is not set.")
            path = Path(self.file_path)
            if not path.is_file():
                raise FileNotFoundError(f"The file {self.file_path} does not exist.")
            return path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def folder_contents(self):
        try:
            if self.folder_path is None:
                raise ValueError("folder_path is not set.")
            path = Path(self.folder_path)
            print(f"path: {path}")
            if not path.is_dir():
                raise NotADirectoryError(f"The folder {self.folder_path} does not exist.")
            if self.folder_path is not None:
                for item in path.iterdir():
                    self.folder_contents_list.append(item.name)
                
            return [item.name for item in path.iterdir()]
            
        except Exception as e:
            print(f"Error accessing folder: {e}")
            return None
        
    def write_file(self, content):
        try:
            if self.file_path is None:
                raise ValueError("file_path is not set.")
            path = Path(self.file_path)
            path.write_text(content, encoding="utf-8")
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False