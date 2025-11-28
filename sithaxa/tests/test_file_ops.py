import os
from pathlib import Path
from sithaxa.utils.file_ops import FileOperations, FolderMapping


def test_read_file(tmp_path):
    # Create a temporary file
    test_file = os.path.join(tmp_path, "test.txt")
    file = FileOperations(file_path=test_file)
    test_content = "Hello, Sithaxa!"
    file.write_file(test_content)

    # Test reading the file
    content = file.read_file()
    if content == test_content:
        print("test_read_file: PASSED")
    else:
        print("test_read_file: FAILED")
    assert content == test_content


def test_folder_contents(tmp_path):
    test_folder = tmp_path
    folder = FileOperations(folder_path=test_folder)
    print(folder.folder_contents())
    # print(test_folder)
    # print(folder.folder_contents_list)


def test_folder_mapping(tmp_path):
    # Create a temporary folder structure
    subfolder = os.path.join(tmp_path, "subfolder")
    os.makedirs(subfolder)
    test_file1 = os.path.join(tmp_path, "file1.txt")
    test_file2 = os.path.join(subfolder, "file2.txt")
    with open(test_file1, "w") as f:
        f.write("File 1 content")
    with open(test_file2, "w") as f:
        f.write("File 2 content")

    # Test FolderMapping
    folder_mapping = FolderMapping()
    project_map = folder_mapping.scan_all(tmp_path)

    # Check if the mapping is correct
    if str(tmp_path) in project_map and str(subfolder) in project_map:
        print("test_folder_mapping: PASSED")
    else:
        print("test_folder_mapping: FAILED")
    assert str(tmp_path) in project_map
    assert str(subfolder) in project_map



# test_folder_mapping(tmp_path=Path("C:/Users/bless/Desktop/projects/sithaxa/sithaxa/tests/temp_test_dir"))

folder = FolderMapping()
folder_mapping = folder.scan_all(rootpath=Path("C:/Users/bless/Desktop/projects/sithaxa/sithaxa"))
print(folder_mapping)


# test_path = Path("C:/Users/bless/Desktop/projects/sithaxa/sithaxa/tests/")
# test_folder_contents(test_path)
# test_read_file(test_path)