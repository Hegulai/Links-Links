def main():
    with open("tulokset_kohde_postinumeroittain.csv", "r") as fin:
        lines = fin.readlines()
    activities = []
    for i in lines:
        spl = i.split(",")
        try:
            activities.append(int(spl[1]))
        except:
            continue
    biggest = max(activities)
    changed = []
    for i in lines:
        spl = i.split(",")
        try:
            changed.append(f"{spl[0]},{int(spl[1])/biggest}")
        except:
            changed.append(i)
    with open("normalisoitu.csv", "w") as fout:
        for i in changed:
            fout.write(f"{i}\n")
    return

if __name__=="__main__":
    main()