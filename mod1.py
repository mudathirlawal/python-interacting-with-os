
#!usr/bin/env python

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  ordered_list2 = [ (list2[(len(list2)- 1)- i]) for i, student in enumerate(list2) ]
  for stud in ordered_list2:
    list1.append(stud ) 
  return list1

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))

# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# newfilenames = [] 

# for i, filename in enumerate(filenames):
#   if filename.endswith('hpp'):  
#     n = len(filename) - 2
#     newfilenames.append(filename[:n])
#     print('{}, {}, {}'.format(i, n, filename))
    
# print('{} {}'.format('\n', newfilenames)) 

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  # ordered_list1 = [ (list1[(len(list1)- 1)- i]) for i, student in enumerate(list1) ]
  list1.reverse()
  for stud in list1:
    list2.append( stud ) 
  return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))


class Repository:
     def __init__(self):
         self.packages = {}
     def add_package(self, package):
          self.packages[package.name] = package
     def total_size(self):
         result = 0
         for package in self.packages.values():
             result += package.size
         return result
         