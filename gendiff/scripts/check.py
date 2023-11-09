from gendiff import generate_diff


diff = generate_diff('/home/alaev/python-project-50/gendiff/file1.json',
                     '/home/alaev/python-project-50/gendiff/file2.json')
print(diff)