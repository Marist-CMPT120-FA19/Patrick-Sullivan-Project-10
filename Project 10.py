import string
def censor():
    fname = input("Enter filename: ")
    file = open("cen.txt", 'r').readlines()
    val = open("answer.txt", 'w')
    i = 'and'
    for i in file:
        words = i.split( )
        for word in words:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 3:
                if "." in word:
                    word = "***."
                elif "," in word:
                    word = "***,"
                elif "?" in word:
                    word = "***?"
                elif "!" in word:
                    word = "***!"
                else:
                    word = "***"
            print(word + " ", file = val, end = "")
    val.close()
censor()
