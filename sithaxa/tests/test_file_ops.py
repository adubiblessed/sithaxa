import os
from pathlib import Path
from sithaxa.utils.file_ops import FileOperations


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


# Fixed: Use Path objects instead of strings
test_path = Path("C:/Users/bless/Desktop/projects/sithaxa/sithaxa/tests/")
test_folder_contents(test_path)
# test_read_file(test_path)