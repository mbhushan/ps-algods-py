from Stack import Stack


def validateHTMLTags(htmlStr):
    stack = Stack()
    hsize = len(htmlStr)
    i = 0
    while i < hsize:
        tag = []
        openTag = True
        if htmlStr[i] == '<':
            tag.append('<')
            i += 1
            if htmlStr[i] == '/':
                openTag = False
                i += 1
            while (i < hsize) and htmlStr[i] == ' ':
                i += 1
            while (i < hsize) and (htmlStr[i].isalpha() or htmlStr[i].isdigit()):
                tag.append(htmlStr[i])
                i += 1
            while (i < hsize) and htmlStr[i] != '>':
                i += 1
            if (i >= hsize):
                return False
            tag.append(htmlStr[i])
            htmTag = ''.join(tag)
            # print ("tag: ", htmTag)
            if openTag:
                stack.push(htmTag)
            elif stack.is_empty():
                return False
            else:
                topTag = stack.pop()
                # print("popped: ", topTag)
                # print("htmTag: ", htmTag)
                if topTag != htmTag:
                    return False
        i += 1
    if not stack.is_empty():
        return False
    return True


def readinput():
    print ("Enter html string: ")
    htmlStr = input()
    return htmlStr


def main():
    html = readinput()
    isValid = validateHTMLTags(html)
    print("Input HTML String Valid? ", isValid)


if __name__ == '__main__':
    main()
