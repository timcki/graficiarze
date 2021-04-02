import random

def main():
	tries = 200
	su = 0
	for i in range(tries):
		el = [random.randint(0, 6) for x in range(10)]
		su += int(check_seq(el))
	print(su/tries)


def check_seq(seq):
	if sum(seq) % 2:
		return False
	return True






if __name__ == '__main__':
	main()