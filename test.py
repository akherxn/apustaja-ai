import codecs, time, os


n = codecs.open('test.txt', 'r+', 'utf-8')
read_lines = n.readlines()
g = 'bbb'
line_index = read_lines.index(g)
index_string = str(line_index)
print("index: " + index_string)
del read_lines[:line_index+1]
print("deleted")
nn = codecs.open('test1.txt', 'w', 'utf-8')
nn.writelines(read_lines)
os.remove('test.txt')
os.rename('test1.txt', 'test.txt')
time.sleep(5)