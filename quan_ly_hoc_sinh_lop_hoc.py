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