def scaleNum(inputNum, minimum, maximum, scale):
    difference = inputNum - minimum
    totalDiff = maximum - minimum
    return ((difference / totalDiff) * scale)
