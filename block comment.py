from collections import deque

def chunkSplit(l, n):
    def chunker():
        for i in range(0, len(l), n):  
            yield l[i:i + n]
    return [' '.join(chunk) for chunk in chunker()]


def blockComment(code,comment,justification = None, clinesize = 5):
    justificationtoggle = 1
    if justification == None:
        commentdividend = 1
        justificationtoggle = 0
    elif justification == 'center':
        commentdividend = 2
    elif justification == 'right':
        commentdividend = 1
    
    output = []
    lines = code.split('\n')
    longestlen = max([len(line) if '\t' not in line else len(line)+4*line.count('\t') for line in lines])+20
    
    codecenter = int(len(lines)/2)
    words = comment.split(' ')
    
    commentlines = chunkSplit(words, clinesize)
    longestcommentline = max([len(line) for line in commentlines])
    #commentlines = [line.ljust(longestcommentline-len(line),' ') for line in commentlines]
    commentcenter = int(len(chunkSplit(words, 5))/2)

    queue = deque(commentlines)
    
    for index, line in enumerate(lines):
        if index >= codecenter-commentcenter:
            try:
                comment_append = queue.popleft()
            except:
                comment_append = ''
        else:
            comment_append = ''
        #print(longestcommentline-len(comment_append))
        if index == 0 or index == len(lines)-1:
            output.append(line+' # <---+    '.rjust(longestlen-len(line)+1,' ')+' '*(int((longestcommentline-len(comment_append))/commentdividend)*justificationtoggle)+comment_append)
        elif index == codecenter:
            output.append(line+' #     +--> '.rjust(longestlen-len(line)+1,' ')+' '*(int((longestcommentline-len(comment_append))/commentdividend)*justificationtoggle)+comment_append)
        else:
            output.append(line+' #     |    '.rjust(longestlen-len(line)+1,' ')+' '*(int((longestcommentline-len(comment_append))/commentdividend)*justificationtoggle)+comment_append)
    return '\n'.join(output)

def main():
    global blockComment


if __name__ == '__main__':
    main()
