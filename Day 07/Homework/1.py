converter = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, 
    "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, 
    "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, 
    "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
}
def hw1(num,x):
    if "." in str(num):
        num = str(num)
        listn = num.split(".")
        sum = 0
        a = listn[0]
        b = listn[1]
        y = 0
        for i in range(len(a)-1,-1,-1):
            sum += int(a[i]) * (x**y)
            y += 1
        z= -1
        for i in range(len(b)):
            sum += int(b[i]) * (x**z)
            z -= 1
        return sum
    else:
        num = str(num)
        sum = 0
        y = 0
        for i in range(len(num)-1,-1,-1):
            sum += converter[num[i]] * (x**y)
            y += 1
        return sum