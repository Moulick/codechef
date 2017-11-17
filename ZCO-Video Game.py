def toString(a):
    b = a[:] # copy list (like slice() in JavaScript) — "buffer"
    for i in range(len(a)): # iterate
        b[i] = str(b[i]) # convert each to string
    return ' '.join(b) # return all string

w, h = map(int, input().split())
boxes = [int(x) for x in input().split()]
moves = [int(x) for x in input().split()]
c_pos = 0
has_box = False
# 1 : Move left
# 2 : Move right
# 3 : Pick up box
# 4 : Drop box
# 0 : Quit

for x in moves:

    if x == 0:
        break
    elif x == 1 and c_pos >0:
        c_pos -= 1
    elif x == 2 and c_pos<w:
        c_pos +=1
    elif x == 3 and has_box == False and boxes[c_pos] >0:
        boxes[c_pos] -= 1
        has_box = True
    elif x==4 and has_box == True and boxes[c_pos] < h:
        boxes[c_pos] += 1
        has_box = False

str1 = toString(boxes)
print(str1)