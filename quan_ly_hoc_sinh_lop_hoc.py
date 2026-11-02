danh_sach_lop = []
danh_sach_hoc_sinh = []

def them_lop():
    ma_lop = input("Nhập mã lớp: ")
    ten_lop = input("Nhập tên lớp: ")
    lop = {
        "ma_lop": ma_lop,
        "ten_lop": ten_lop
    }
    danh_sach_lop.append(lop)
    print("Thêm lớp thành công!")

def hien_thi_lop():
    for lop in danh_sach_lop:
        print(lop)
def them_hoc_sinh():
    ma_hs = input("Nhập mã học sinh: ")
    ten_hs = input("Nhập tên học sinh: ")
    ma_lop = input("Nhập mã lớp: ")
    hoc_sinh = {
        "ma_hs": ma_hs,
        "ten_hs": ten_hs,
        "ma_lop": ma_lop
    }
    danh_sach_hoc_sinh.append(hoc_sinh)
    print("Thêm học sinh thành công!")

def hien_thi_hoc_sinh():
    for hs in danh_sach_hoc_sinh:
        print(hs)

def tim_hoc_sinh():
    ma = input("Nhập mã học sinh cần tìm: ")

    for hs in danh_sach_hoc_sinh:
        if hs["ma_hs"] == ma:
            print(hs)
            return

    print("Không tìm thấy học sinh!")

while True:
    print("\n1. Thêm lớp")
    print("2. Hiển thị lớp")
    print("3. Thêm học sinh")
    print("4. Hiển thị học sinh")
    print("5. Tìm học sinh")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        them_lop()
    elif chon == "2":
        hien_thi_lop()
    elif chon == "3":
        them_hoc_sinh()
    elif chon == "4":
        hien_thi_hoc_sinh()
    elif chon == "5":
        tim_hoc_sinh()
    elif chon == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")