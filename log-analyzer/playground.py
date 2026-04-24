with open("log.txt") as file:
    for line in file:
        print("RAW:", line)
        print("STRIPPED:", line.strip())