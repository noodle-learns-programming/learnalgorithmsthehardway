total   = 0

def count_rectange_with_size(size):
    result = 0
    for y in range(0, 8):
        if y + size > 8:
            break
        for x in range (0, 8):
            if x + size > 8:
                break
            result += 1

    return result


for size in range(1, 9):
    print 'With size %s is %s: ', (size, count_rectange_with_size(size))
    total += count_rectange_with_size(size)

print 'Number of rectangle in a square 8x8 are: ', total