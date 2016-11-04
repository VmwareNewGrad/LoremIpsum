import sys

def readFile(data):
    with open(data, 'r') as file_data:
        lines = file_data.read().split('.')
    return lines

def get_sentences(data, num=1):
    sentences = readFile(data)
    ret = '.'.join(sentences[:num])
    return ret

def get_paragraphs(data, num=1):
    lines_per_para = 10

    fileread = readFile(data)
    if num*lines_per_para > len(fileread):
        lines_per_para = len(fileread) // num

    para = []
    for i in xrange(0, num):
        para.append('. '.join(fileread[i*lines_per_para:(i+1)*lines_per_para]))

    return "\n\n".join(para)

def get_words(data, num=1):
    words = []
    fileread = readFile(data)
    for line in fileread:
        words += line.split()
    return ' '.join(words[:num])

def get_letters(data, num=1):
    fileread = readFile(data)

    letters = []
    for line in fileread:
        for word in line.split('.'):
            letters += list(word)
            if len(letters) > num:
                break
    return ''.join(letters[:num])
        
def main(argv):
    data = argv[0]
    print "2 Sentences:"
    print get_sentences(data, 2)
    print "-------------------------------"
    print "2 Paragraphs:"
    print get_paragraphs(data, 2)
    print "-------------------------------"
    print "50 Words:"  
    print get_words(data, 50)
    print "-------------------------------"
    print "500 Letters:"  
    print get_letters(data, 500)
    print "-------------------------------"

if __name__ == "__main__":
    main(sys.argv[1:])
