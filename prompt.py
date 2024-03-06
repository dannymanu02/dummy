def report_count(token):
    f = open("ada-lovelace.txt", "r")
    string = f.read().lower().split(" ")
    count = 0
    for i in string:
        if i == token:
            count += 1
    print(f"The term {token} shows up in the corpus {count} times.")

report_count("engine")