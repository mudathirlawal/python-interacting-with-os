
#!usr/bin/env python3

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = [] 

for i, filename in enumerate(filenames):
  if filename.endswith('hpp'):  
    n = len(filename) - 2
    newfilenames.append(filename[:n])
    print('{}, {}, {}'.format(i, n, filename))
  else:
    newfilenames.append(filename)
    print('{}, {}, {}'.format(i, '-', filename))

print('{} {}'.format('\n', filenames))    
print('{} {}'.format('\n', newfilenames))  