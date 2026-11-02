
def kiem_tra_trung_lich(lich_hoc):
    for i in range(len(lich_hoc)):
        for j in range(i + 1, len(lich_hoc)):
            lich_1 = lich_hoc[i]
            lich_2 = lich_hoc[j]

            if lich_1["ngay"] == lich_2["ngay"]:
                if (lich_1["bat_dau"] < lich_2["ket_thuc"]
                    and lich_2["bat_dau"] < lich_1["ket_thuc"]):
                    print("Lich hoc bi trung:")
                    print(lich_1["mon"], "va", lich_2["mon"])
                    return True

    print("Khong co lich hoc bi trung")
    return False


lich_hoc = [
    {"mon": "Co so du lieu", "ngay": "Thu 2",
     "bat_dau": 7, "ket_thuc": 9},

    {"mon": "Lap trinh Python", "ngay": "Thu 2",
     "bat_dau": 8, "ket_thuc": 10},

    {"mon": "Mang may tinh", "ngay": "Thu 3",
     "bat_dau": 7, "ket_thuc": 9}
]

kiem_tra_trung_lich(lich_hoc)
