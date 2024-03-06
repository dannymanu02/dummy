import lower_split

def report_count(token):
    f = open("corpus.txt", "r")
    string = f.read()
    string = lower_split.lower_split(string)
    count = 0
    for i in string:
        if i == token:
            count += 1
    print(f"The term {token} shows up in the corpus {count} times.")