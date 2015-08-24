#understanding decorators

import time

def timing_function(the_url):

    """
    Outputs the time a function takes
    to execute.
    """
    #print args
    def wrapper(some_func):

    	print some_func
    	def wrapped_f():

    		print "bro"
	    	#the_url = args[0]
	    	print "url: " + the_url
	    	#some_func = args[0]
	        t1 = time.time()
	        some_func()
	        t2 = time.time()
	        print "Time it took to run the function: " + str((t2-t1)) + "\n"
	        #return wrapped_f



	return wrapped_f
    return wrapper

@timing_function("bro.com/web")
def my_function():
    num_list = []
    for x in (range(0,1000)):
        num_list.append(x)
    print "\nSum of all the numbers: " +str((sum(num_list)))


print my_function()
