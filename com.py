import gzip
content = "Lots of content here "*100
with gzip.open('file.txt.gz', 'w+') as f:
	for i in range(5000):
		f.writelines(content)
f.close()
