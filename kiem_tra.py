ct_quan_ly_doi_bong =[]
while True:
    print("MENU")
    print("1.xem danh sach cau thu ")
    print("2.nhap thong tin cau thu tu ban phim")
    print("3.tinh cot thuong cho cac cau thu")
    print("4.tim kiem va xoa cau thu co cung ma cau thu nhap tu ban phim")
    print("5.tim kiem va chinh sua thong tin cau thu co cung ma cau thu nhap tu ban phim")
    print("6.xem danh sach cau thu sap xep theo so huy chuong tu nho den lon")
    print("7.thoat chuong trinh")
    lua_chon = input("nhap lua chon ma ban muon su dung vao day:")
    if lua_chon.isdigit() == False:
        raise ValueError("loi nhap vao! yeu cau nhap vao so tu nhien")
    else:
        lua_chon = int(lua_chon)
        if lua_chon == 1:
            print("xem danh sach cau thu")
            print("ma_cau_thu","\t","ten_cau_thu", "\t", "tuoi", "\t", "vi_tri", "\t", "so_huy_chuong", "\t", "thuong", "\t")
            for ct in ct_quan_ly_doi_bong:
                print(ct["ma_cau_thu"],"\t",ct["ten_cau_thu"], "\t", ct["tuoi"], "\t", ct["vi_tri"], "\t", ct["so_huy_chuong"], "\t", ct["thuong"], "\t")
        elif lua_chon == 2:
            print("nhap thong tin cac cau thu tu ban phim")
            while True:
                cau_thu ={"ma_cau_thu":"",
                          "ten_cau_thu":"",
                          "tuoi":"",
                          "vi_tri":"",
                          "so_huy_chuong":"",
                          "thuong":"",
                          }
                cau_thu['ma_cau_thu'] = input("Nhap ma cau thu: ")
                cau_thu['ten_cau_thu'] = input("Nhap ten cau thu: ")
                cau_thu['tuoi'] = int(input("Nhap tuoi: "))
                cau_thu['vi_tri'] = input("Nhap vi tri")
                cau_thu['so_huy_chuong'] = int(input("Nhap so huy chuong"))
                cau_thu['thuong'] = float(input("Nhap so thuong "))
                
                
                