import sys

def permute(ip, op):

	# base case
	if len(ip) == 0:
		print(op, end="\n")
		return

	# pick lower and uppercase
	ch = ip[0].lower()
	ch2 = ip[0].upper()
	ip = ip[1:]
	permute(ip, op+ch)
	permute(ip, op+ch2)

# driver code


def main():
	try:
		ip = str(sys.argv[1])
		#ip = "senseiesnes@proton.me"
		permute(ip, "")
	except IndexError:
		print("You did not specify an email")
		print("Try to: python3 permute.py mail@example.com")
		sys.exit(1)



main()

