from gendiff import generate_diff


diff = generate_diff('/home/alaev/python-project-50/tests/fixtures/file1.json',
                     '/home/alaev/python-project-50/tests/fixtures/file2.json')
print(diff)
