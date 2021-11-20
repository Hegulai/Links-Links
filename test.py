from dataclasses import dataclass
from datetime import date, datetime
from itertools import groupby
from operator import attrgetter
from typing import DefaultDict
from collections import defaultdict

@dataclass
class flow:
    dat: datetime
    postinro: str
    kotipostinro: str
    lkm: int


def read_flow(path):
    flows = []
    with open(path, "r") as fin:
        lines = fin.readlines()
    for l in lines:
        spl = l.split(";")
        spldat = spl[0].split(".")
        if len(spldat) < 3: continue
        flows.append(flow(
            dat = datetime(day=int(spldat[0]), month=int(spldat[1]), year=int(spldat[2])),
            postinro = spl[1],
            kotipostinro = spl[2],
            lkm = int(spl[3])
        ))
    return flows

def total_movement_by_day(flows):
    groups = defaultdict(lambda: [])
    for grp, data in groupby(sorted(flows, key=attrgetter("dat")), key=attrgetter("dat")):
        for element in data:
            groups[element.dat].append(element)
    
    total_movements = defaultdict(lambda: [])
    for key in groups:
        s = 0
        for el in groups[key]:
            s += el.lkm
        total_movements[el.dat].append(s)

    with open("tulokset_paivittain.csv", "w") as fout:
        for key in total_movements:
            fout.write(f"{key}: {total_movements[key][0]}\n")
    return

def total_movement_by_postal_code(flows):
    movements = defaultdict(lambda: 0)
    for i in flows:
        movements[(i.kotipostinro, i.postinro)] += i.lkm
    with open("tulokset_postinumeroittain.csv", "w") as fout:
        for key in movements:
            fout.write(f"{key[0]}->{key[1]}:\t{movements[key]}\n")
    return
    
def total_movement_by_target_postal_code(flows):
    movements = defaultdict(lambda: 0)
    for i in flows:
        movements[i.postinro] += i.lkm
    with open("tulokset_kohde_postinumeroittain.csv", "w") as fout:
        for key in movements:
            fout.write(f"{key};{movements[key]}\n")
    return


def main():
    path = "liikkuvuus.txt"
    flows = read_flow(path)
    #total_movement_by_day(flows)
    #total_movement_by_postal_code(flows)
    total_movement_by_target_postal_code(flows)
    return

            
if __name__=="__main__":
    main()

