from pathlib import Path


path = Path('C:/Users/Ícaro/Downloads/Ícaro/python_crash_course/python_works/text_files/pi_digits.py')
content = path.read_text()
print(content)
