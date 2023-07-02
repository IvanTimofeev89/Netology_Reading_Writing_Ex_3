with open("1.txt", encoding="UTF-8") as f:
    data_1 = dict.fromkeys(["1.txt"],[])
    for row in f:
        data_1["1.txt"].append(row.strip())

with open("2.txt", encoding="UTF-8") as f:
    data_2 = dict.fromkeys(["2.txt"],[])
    for row in f:
        data_2["2.txt"].append(row.strip())

with open("3.txt", encoding="UTF-8") as f:
    data_3 = dict.fromkeys(["3.txt"],[])
    for row in f:
        data_3["3.txt"].append(row.strip())

def all_data_sorted(data1, data2, data3):
    temp_dict = data1 | data2 | data3
    return dict(sorted(temp_dict.items(), key=lambda item: len(item[1])))

with open("4.txt", "w", encoding="UTF-8") as f:
    for key, value in all_data_sorted(data_1, data_2, data_3).items():
        f.write(f"{key}\n")
        f.write(f"{len(value)}\n")
        for row in value:
            f.write(f"{row}\n")

