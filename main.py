
def read_line(n, file):
    try:
        if type(n) != int:
            return "invalid input detected"
        f = open(file, 'r')
        count = 1
        for line in f:
            if count==n:
                return line
            else:
                count = count+1
        return "line "+str(n)+"  doesn't exist"
    except:
        return "file not found"


def  longest_words(file):
    try:
        list = ["a", "a", "a", "a", "a"]
        file = open(file, 'r')
        for line in file:
            line = line.replace('.', ' ')
            line = line.replace('-', '')
            line = line.replace(',', '')
            line = line.split()
            for word in line:
                if len(word) > len(list[4]):
                    list[4] = word
                    list.sort(key=len, reverse= True)
        return list
    except:
        return "file not found"


