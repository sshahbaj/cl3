import  xml.etree.ElementTree as ET           # to take .xml file as input and to ise xml.tree we made an object named as "ET"
from threading import Thread
import threading
import time
#import thread

def qsort(sets,left,right):

    print("thead {0} is sorting {1}".format(threading.current_thread(), sets[left:right]))

    i = left
    j = right
    pivot = sets[(left + right)//2]
    temp = 0
    while(i <= j):
         while(pivot > sets[i]):
             i = i+1
         while(pivot < sets[j]):
             j = j-1
         if(i <= j):
             temp = sets[i]     
             sets[i] = sets[j]
             sets[j] = temp
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    if (left < j):
        lthread = Thread(target = lambda: qsort(sets,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(sets,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return sets


'''testing below'''
ls = [int(num.find('value').text) for num in ET.parse('A2_demo.xml').getroot().findall('number')]
res = qsort(ls, 0, len(ls) - 1)
print(res)
