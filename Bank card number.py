#Credit from CS50'Pset1 but in Py not in C
#Determine the type of bank card by its number
#
print ("        Determine the type of bank card by its number.\n")
print (" Give the bank card number (without any spaces or other characters.): ")
inp = raw_input(" ")
print ""

# is input an integer?
try:
   n = int(inp)# Global card number variable is converted to integer
   #print("input is integer")
   isInteger = True
except(TypeError, ValueError):
   print ("\n Entered data has wrong format.\n")
   isInteger = False

# Luhn's algorithm function definition is here
def LuhnsAlgorithm(s):
	ns = str(n) # convert bank card number to string for confort loop FOR
	i = 0 # variable for convenience of sorting each digit of the number by the parity criterion
	b = 0 # ancillary variable
	c = 0 # ancillary variable
	d = 0 # ancillary variable
	e = 0 # ancillary variable
	for m in reversed(ns):
        # we need to start our counting from right to left
        # if we will counting from left to right, our function will wright count Luhn's sum only for
        # such bank cards, the number of digits in the numbers of which is odd (15 for example)
		i = i+1
		if (i%2 == 0):
                #if the digit is even
			b = int(m)*2 # convert to int and multiply by 2
			if (b > 9):
				b = b-9 # exceptions for two-digit numbers
			c = b + c	
		else:
                #if the digit is odd
			d = int(m)# convert to int
			e = e + d
	#print "i= ", i, ""
	#print "c = ", c, ""
	#print "e = ", e, ""
	s = c + e # sum of digits -- Luhn's number
	#print "s = ", s, " "
	s = s%10 # exact Luhn's number
	#print "s%10 = ", s, "\n"
 
	return s

if (isInteger):
        # Check for number of digits
        if (n <= 4000000000000 or (n > 4999999999999 and n < 340000000000000) or n >= 5599999999999999):
                print (" Check your bank card number. Entered number is INVALID.\n")
        else:
                # call for Luhn's algorithm function
                if (LuhnsAlgorithm(n) == 0):
                # the last digit in Luhn's number is 0, so card is legit!
                        #print (" Luhn say: VALID NUMBER.\n")
                        if ((n>=340000000000000 and n <=349999999999999) or (n>=370000000000000 and n<=379999999999999)):
                                print (" This bank card is AMEX.\n")
                        elif (n>=5100000000000000 and n <=5599999999999999):
                                print (" This bank card is MASTERCARD.\n")
                        elif ((n>=4000000000000 and n <=4999999999999) or (n>=4000000000000000 and n<=4999999999999999)):
                                print (" This bank card is VISA.\n")
                        else:
                                print (" Error. Unknown bank card type.\n")
                else:
                # the last digit in Luhn's number is NOT 0, so card is not legit!
                        #print (" Luhn says: INVALID NUMBER.\n")
                        print (" This bank card number is INVALID.\n")

#####
# The End
#####
print "\n Press Enter to exit."
raw_input()
exit(0)

