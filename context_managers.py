with (
	open('file1') as f1,
	open('file2') as f2,
):
    print(f1.read())
    print(f2.read())

with open('file1') as f1, \
	open('file2') as f2:
    print(f1.read())
    print(f2.read())