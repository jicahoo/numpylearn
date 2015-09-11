import numpy
import operator
import types
import pprint

#Size of things from numpy
seq=0

seq+=1
print "\n%s. Total number:" % (seq)
print "The total number of things from numpy is %s module." % len(dir(numpy))

#Get stats info of attrs of numpy 
stats_of_type = {}
for item in dir(numpy):
    #print type(eval('numpy.%s' % item))
    attr_of_numpy = eval('numpy.%s' % item)
    attr_type = type(attr_of_numpy)
    if str(attr_type) in stats_of_type:
        stats_of_type[str(attr_type)] +=1
    else:
        stats_of_type[str(attr_type)] = 1

seq += 1
print "\n%s. Stats of numpy:" % (seq)
pprint.pprint(sorted( stats_of_type.items(), key = operator.itemgetter(1), reverse = True))
