import os
import dbm
import pickle
import wc

fout = open('output.txt', 'w')
line1 = "This here's the wattle, \n"
fout.write(line1)
line2 = "the emblem of our land. \n"
fout.write(line2)

fout.close()
camels = 42
print('In %d years I have spotted %d %s' % (3, camels, 'camels'))

cwd = os.getcwd()
print(cwd)

print(os.path.isfile('output.txt'))
print(os.listdir(cwd))

list_of_files = []


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            list_of_files.append(name)
            # print(name)
        else:
            walk(path)
    return list_of_files


t = walk(cwd)

try:
    fin = open('bad_file')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong')

db = dbm.open('captions.db', 'c')

db['cleese.png'] = 'Photo of john Cleese.'

print(db['cleese.png'])

db['cleese.png'] = 'Photo of john Cleese doing a silly walk.'

print(db['cleese.png'])

for key in db:
    print(key, db[key])

db.close()


t = [1, 2, 3]
s = pickle.dumps(t)
t2 = pickle.loads(s)
print(t2)
print(t is t2)

cmd = 'dir'
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)


def open_zip(filename):
    cmd = 'gunzip -c ' + filename
    fp = os.popen(cmd)
    return fp


print(wc)
print(wc.linecount('output.txt'))
print(__name__)
print(wc.__name__)

s = '1 2\t 3\n 4'
print(s)
print(repr(s))

e = []
fin = open('output.txt')
for line in fin:
    words = line.strip()
    w = words.split()
    print(w)

