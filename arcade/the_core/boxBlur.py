def boxBlur(image):
    ans = []
    for i in range(len(image) - 2):
        temp = []
        for j in range(len(image[0]) - 2):
            cropped = [row[j:j+3] for row in image[i:i+3]]
            temp.append(sum(map(sum, cropped)) // 9)
        ans.append(temp)

    return ans
