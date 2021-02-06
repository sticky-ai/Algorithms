def meetingRoom(s):
	s.sort(lambda x: (x[1], x[0]))

	start, cnt = 0, 0
	for meet in s:
		if meet[0] >= start:
			start = meet[1]
			cnt += 1
	return cnt
