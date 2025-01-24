# გამოიკვლიეთ მასივში მაქსიმუმის მოძებნის ამოცანა 5 ელემენტის შემთხვევაში (ვარიანტისთვის [4]3გვ:21ეგვ): დაწერეთ
# ფსევდოკოდი, ბლოკ-სქემა, ანალიზი.

# ამოცანის ამოხსნა შეგვიძლია რამდენიმე გზით. ერთ-ერთი გზა არის შემდეგი:
def max5_0(a, b, c, d, e):
    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return a
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
        else:
            if c > d:
                if c > e:
                    return c
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
    else:
        if b > c:
            if b > d:
                if b > e:
                    return b
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
        else:
            if c > d:
                if c > e:
                    return c
                else:
                    return e
            else:
                if d > e:
                    return d
                else:
                    return e
                
#check
print(max5_0(1, 2, 3, 4, 5)) # 5
print(max5_0(54, 12, 23, 35, 19)) # 54
print(max5_0(110, 267, 134, 423, 594)) # 594

#მეორე გზა არის შემდეგი:
def max5_1(a, b, c, d, e):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    if d > largest:
        largest = d
    if e > largest:
        largest = e
    return largest

#check
print(max5_1(1, 2, 3, 4, 5)) # 5
print(max5_1(54, 12, 23, 35, 19)) # 54
print(max5_1(110, 267, 134, 423, 594)) # 594