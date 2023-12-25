def get_clans():
    clans = []
    with open("clans.txt", "r") as f:
        for clan in f.read().split("\n"):
            if clan != "":
                clans.append(clan)
    return clans

def add_clan(clan):
    current_clans = get_clans()
    current_clans.append(clan)
    output = ""
    for i in range(len(current_clans)):
        output += current_clans[i]
        if i != len(current_clans)-1 and len(current_clans) != 0:
            output += "\n"
    with open("clans.txt", "w") as f:
        f.write(output)

def remove_clan(clan):
    current_clans = get_clans()
    with open("clans.txt", "w") as f:
        f.write('')
    for clan_curr in current_clans:
        if clan_curr != clan:
            add_clan(clan_curr)