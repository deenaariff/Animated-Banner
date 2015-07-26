from sys import stdout
import time

message = raw_input("Enter the message you want in the banner: ")
display = []
gutter = len(message)*3 
iteration = 0
i = 0

while(iteration < 20):
	display = []
	for j in range(len(message) + gutter):
		display.append(" ") 			
	for j in range(len(message)):
		if (i+j) <= (len(display) - 1):	
			display[i+j]=message[j]
		else:
			display[i+j-len(display)]=message[j] 
	i += 1
	if i == (len(message) + gutter):
		i = 0
		iteration += 1;	
	output = ''.join(display)
	stdout.write("\r" + output)
	stdout.flush()	
	time.sleep(0.10)

