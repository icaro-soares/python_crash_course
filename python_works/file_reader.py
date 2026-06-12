from pathlib import Path


path = Path('text_files/file_reader.py')
content = path.read_text()
print(content)
