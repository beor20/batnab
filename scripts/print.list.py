import time 
# this script demonstrates looping through a list

def print_list() :
	for i in range(0, len(colors)):
		print colors[i]
		time.sleep(1)

if __name__== '__main__':
	try:
		print_list()
	except KeyboardInterrupt:
		print 'Good bye'
