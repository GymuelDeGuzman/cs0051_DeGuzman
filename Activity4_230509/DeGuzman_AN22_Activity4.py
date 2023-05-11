# De Guzman, Gymuel D. - Parallel Computing

# import libraries and dependencies
import random
from threading import Thread
from time import sleep


# prints the load sending confirmation
def sendLoad(amount, num, transNum):

	# waits a random time (between 1 to 5 sec) to simulatte delay and inconsistencies
	sleepTime = random.randint(1, 5)
	sleep(sleepTime)

	# prints confirmation message with transaction number, amount, and wait time
	print("  [tn#" + str(transNum) + "]  " + "An amount of " + str(amount) + " PHP was sent to " + num + "!  " + "[" + str(sleepTime) + "s]")


# prints the load sending confirmation
def inputLoad(num, transNum):
	amountLoad = int(input("Input load amount: "))
	print("  >>>>>>  Sending", amountLoad, "PHP to", num, "...\n")

	# initialize threads and increment transaction number counter
	transNum+=1
	send = Thread(target = sendLoad, args = (amountLoad, num, transNum,))
	menu = Thread(target = inputLoad, args = (num, transNum,))

	# starts the threads
	menu.start()
	send.start()

	# synchronizes threads
	menu.join()
	send.join()


# main program that calls the function for loading thread
def main():
	print("\n  --- PASALOAD APP ---\n")
	numAccount = input("Enter load recipient: ")
	inputLoad(numAccount, 0)

# main call
main()
