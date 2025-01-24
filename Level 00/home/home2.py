
converter = {"0": 0, "1": 1, "2": 2,
"3": 3, "4": 4, "5": 5, "9": 9, "A": 10, "B": 11,
"6": 6, "7": 7, "8": 8, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "0": 24, "p": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
}

def hw2_try1(num, b):
    num = str(num)
    nums1 = []
    nums2 = []
    if "." in num:
        num = num.split(".")
        part1 = num[0][::-1]
        part2 = num[1]
        for i in range(len(part1)):
            nums1.append(int(converter [part1[i]]) * (b ** i))
        for x in range(len(part2)):
            nums2.append(int(converter [part2 [x]]) * (1 / b ** (x+1)))
        return sum(nums1 + nums2)
    else:
        num = num[::-1]
    for i in range(len(num)):
        nums1.append(int(converter [num[i]]) * (b ** i))
    return sum(nums1)
# test:
print (hw2_try1(1001, 2))
print(hw2_try1(1001, 4))
print(hw2_try1(520.3, 10))
print(hw2_try1(1001, 16))
print(hw2_try1 (1011, 16))
print(hw2_try1("1FFF", 16))
print(hw2_try1("FFF", 16))
print(hw2_try1(520.3, 6))