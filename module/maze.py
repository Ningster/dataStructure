matrix = [
    ["*","*","*","e","*"],
    ["*"," ","*"," ","*"],
    ["s"," ","*"," ","*"],
    ["*"," "," "," ","*"],
    ["*","*","*","*","*"]
]

def printMaze(m):
    result = ''
    for i in matrix:
        for j in i:
            result = result + str(j)+' '
        print result
        result = ''

def escape(m, start, row, column):
    result = False
    step = 0
    if m[row][column]=='*':
        result= False
    elif m[row][column]=='e':
        result= True
        step = 1
    else:
        if start == 'left':
            if escape(m,'down',row-1,column) or  escape(m,'left',row,column+1) or  escape(m,'up',row+1,column) :
                result = True
                m[row][column]='0'
                #step = 1+escape(m,'down',row-1,column).step + escape(m,'left',row,column+1).step + escape(m,'up',row+1,column).step
            #check up, right, down
        elif start == 'up':
            if escape(m,'left',row,column+1) or  escape(m,'up',row+1,column) or  escape(m,'right',row,column-1) :
                result = True
                m[row][column]='0'
                #step = 1+escape(m,'left',row,column+1).step + escape(m,'up',row+1,column).step + escape(m,'right',row,column-1).step
            #check right, down, left
        elif start == 'right':
            if escape(m,'up',row+1,column) or  escape(m,'right',row,column-1) or  escape(m,'down',row-1,column) :
                result = True
                m[row][column]='0'
                #step = 1+escape(m,'up',row+1,column).step + escape(m,'right',row,column-1).step + escape(m,'down',row-1,column).step
            #check  down, left, up
        else:
            if escape(m,'right',row,column-1) or  escape(m,'down',row-1,column) or  escape(m,'left',row,column+1) :
                result = True
                m[row][column]='0'
                #step = 1+escape(m,'right',row,column-1).step + escape(m,'down',row-1,column).step + escape(m,'left',row,column+1).step
            #check left, up, right
    return result


print escape(matrix,'left',2,0)
printMaze(matrix)
