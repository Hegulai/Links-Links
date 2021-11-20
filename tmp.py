

def main():
    with open("data/holiday_season_activity.csv", "r") as fin:
        lines = fin.readlines()
    with open("data/holiday_season_activity2.csv", "w") as fout:
        for l in lines:
            fout.write(f"Postcode{l}")
    return

def main2():
    with open("christmas_activity.csv", "r") as fin:
        lines = fin.readlines()
    with open("christmas_activity2.csv", "w") as fout:
        for l in lines:
            spl = l.split(",")
            n = spl[1][1:-2]
            fout.write(f"Postcode{spl[0]},{n}\n")
    return

if __name__=="__main__":
    main2()