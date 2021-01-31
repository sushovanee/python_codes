def choc_dist(num, new_choc):
	bool_list = []
	for entry in num:
		bool_list.append(entry+new_choc >= max(num))
	return bool_list
	
if __name__ == '__main__':
    candies = [4,2,1,1,2]
    extraCandies = 1
    req_list = choc_dist(candies, extraCandies)
    print(req_list)