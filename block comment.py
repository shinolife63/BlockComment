from collections import deque

def chunkSplit(l, n):
    def chunker():
        for i in range(0, len(l), n):  
            yield l[i:i + n]
    return [' '.join(chunk) for chunk in chunker()]

def deblockComment(code):
    lines = code.split('\n')
    output = []
    for line in lines:
        output.append('#'.join(line.split('#')[:-1]).rstrip())
    return '\n'.join(output)

def blockComment(code,comment,justification = None, clinesize = 7):
    
    justificationtoggle = 1                  # <---+    
    if justification == None:                #     |    justificationtoggle being zero will cause no extra
        commentdividend = 1                  #     |    spaces to be appended to comment_append, commentdividend
        justificationtoggle = 0              #     |    determines the kind applied if justification is
    elif justification == 'center':          #     +--> infact desired, will default to left. 
        commentdividend = 2                  #     |    All this is doing is setting up
    elif justification == 'right':           #     |    for the comment appending stage.
        commentdividend = 1                  # <---+    
    
    
    lines = code.split('\n')
    longestlen = max([len(line) if '\t' not in line else len(line)+4*line.count('\t') for line in lines])+20
    codecenter = int(len(lines)/2)

    if '\n' not in comment:                                  # <---+    Checks if the comment already has linebreaks,
        words = comment.split(' ')                           #     |    if not it breaks the comment into
        commentlines = chunkSplit(words, clinesize)          #     +--> lines composed of clinesize'd words, and if
    else:                                                    #     |    it does, simply uses the existing line breaks.
        commentlines = comment.split('\n')                   # <---+    

        
    longestcommentline = max([len(line) for line in commentlines])
    commentcenter = int(len(commentlines)/2)

    queue = deque(commentlines)
    output = []
    
    for index, line in enumerate(lines):                                                                                                 # <---+    
        if (index >= codecenter-commentcenter) and queue:                                                                                #     |    
            comment_append = queue.popleft()                                                                                             #     |    codecenter-commentcenter is the point where the comment should begin in order to align with the codeblock's center
        else:                                                                                                                            #     +--> if index(the line currently being worked on) had reached that point, and the queue is not empty, comment_append is set to the next value from the queue
            comment_append = ''                                                                                                          #     |    justificationtoggle being zero will cause no extra spaces to be appended to comment_append, commentdividend determines the kind applied if justification is infact desired, will default to left
        comment_append = ' '*(int((longestcommentline-len(comment_append))/commentdividend)*justificationtoggle)+comment_append          # <---+    


        if index == 0 or index == len(lines)-1:                                                          # <---+    
            output.append(line+' # <---+    '.rjust(longestlen-len(line)+1,' ')+comment_append)          #     |    Because this operates on the codeblock line
        elif index == codecenter:                                                                        #     |    by line, the output is an array
            output.append(line+' #     +--> '.rjust(longestlen-len(line)+1,' ')+comment_append)          #     +--> we append the modified lines to, and
        else:                                                                                            #     |    then convert back to a multiline string
            output.append(line+' #     |    '.rjust(longestlen-len(line)+1,' ')+comment_append)          # <---+    right before returning.

    
    return '\n'.join(output)

def main():
    global blockComment


if __name__ == '__main__':
    main()
