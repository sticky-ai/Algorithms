def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if i == j[:len(i)]:
                return False
    return True
