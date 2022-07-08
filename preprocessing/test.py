import codecs, time
'''
dd = codecs.open('longtext.txt', 'r', 'utf-8')
read = dd.readlines()
for line in read:
    print("kkkkkk")
    print(line)
    time.sleep(2)

''' 
import itertools
with codecs.open('longtext.txt', 'r', 'utf-8') as f:
    for line1,line2 in itertools.zip_longest(*[f]*2):
        print("kkkkkk")
        print(line1,line2)
        time.sleep(5)
