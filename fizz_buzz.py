def fizz_buzz(num):
	if num%15 == 0:
		return 'fizz_buzz'
	elif num%5 == 0:
		return 'fizz'
	elif num%3 == 0:
		return 'buzz'
	else:
		return num
		
if __name__ == '__main__':
    in_list = [3,2,4,5,15,9,45]
    print(in_list)
    print(list(map(fizz_buzz, in_list)))
	# for entry in map(fizz_buzz, in_list):
		# print(entry)