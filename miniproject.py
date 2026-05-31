

# PHẦN I: KHỞI TẠO HỆ THỐNG


# Khởi tạo số lượng tồn kho ban đầu cho 3 mặt hàng
laptop_ton_kho = 0   
phone_ton_kho  = 0   
tablet_ton_kho = 0   

# Ngưỡng cảnh báo hàng thấp (Phần V yêu cầu < 10 thì cảnh báo)
NGUONG_CANH_BAO = 10



# PHẦN II: VÒNG LẶP MENU CHÍNH


print("=" * 50)
print("   CHÀO MỪNG ĐẾN HỆ THỐNG QUẢN LÝ KHO!")
print("=" * 50)

while True: 
    print("\n----- MENU CHÍNH -----")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    print("----------------------")

    lua_chon = input("Bạn chọn chức năng (1-5): ")

    # PHẦN II (tt): Điều hướng theo lựa chọn bằng if/elif/else

    #CHỨC NĂNG 1: XEM BÁO CÁO TỒN KHO
    if lua_chon == "1":

        print("\n===== BÁO CÁO TỒN KHO =====")

        # In số lượng tồn kho từng mặt hàng
        print(f"  Laptop      : {laptop_ton_kho} sản phẩm")
        print(f"  Điện thoại  : {phone_ton_kho} sản phẩm")
        print(f"  Máy tính bảng: {tablet_ton_kho} sản phẩm")

        # YÊU CẦU NÂNG CAO: Vẽ biểu đồ bằng dấu sao 
        print("\n----- BIỂU ĐỒ TỒN KHO -----")

        # Dùng vòng lặp for để in ra số dấu * bằng đúng số lượng tồn kho
        bieu_do_laptop = ""
        for i in range(laptop_ton_kho):
            bieu_do_laptop += "*"

        bieu_do_phone = ""
        for i in range(phone_ton_kho):
            bieu_do_phone += "*"

        bieu_do_tablet = ""
        for i in range(tablet_ton_kho):
            bieu_do_tablet += "*"

        # Nếu tồn kho = 0 thì in ra "(trống)" cho dễ đọc
        if bieu_do_laptop == "":
            bieu_do_laptop = "(trống)"
        if bieu_do_phone == "":
            bieu_do_phone = "(trống)"
        if bieu_do_tablet == "":
            bieu_do_tablet = "(trống)"

        print(f"  Laptop       ({laptop_ton_kho}): {bieu_do_laptop}")
        print(f"  Điện thoại   ({phone_ton_kho}): {bieu_do_phone}")
        print(f"  Máy tính bảng({tablet_ton_kho}): {bieu_do_tablet}")
        print("============================")


    #CHỨC NĂNG 2: NHẬP KHO 

        print("\n===== NHẬP KHO =====")
        print("Bạn muốn nhập hàng nào?")
        print("  1. Laptop")
        print("  2. Điện thoại")
        print("  3. Máy tính bảng")

        chon_hang = input("Chọn mặt hàng (1-3): ")

        # Kiểm tra người dùng có chọn đúng mặt hàng không
        if chon_hang == "1" or chon_hang == "2" or chon_hang == "3":

            # PHẦN IV: VÒNG LẶP KIỂM TRA SỐ LƯỢNG ÂM

            while True:
                so_luong_nhap = int(input("Nhập số lượng cần nhập kho: "))

                if so_luong_nhap < 0:
                    # Nếu nhập số âm thì cảnh báo và hỏi lại
                    print(" Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    # Số lượng hợp lệ (>= 0) thì thoát vòng lặp kiểm tra
                    break

            # Cộng dồn số lượng vào đúng mặt hàng được chọn
            if chon_hang == "1":
                laptop_ton_kho += so_luong_nhap   # += tức là laptop = laptop + so_luong_nhap
                print(f" Đã nhập {so_luong_nhap} Laptop. Tồn kho hiện tại: {laptop_ton_kho}")

            elif chon_hang == "2":
                phone_ton_kho += so_luong_nhap
                print(f" Đã nhập {so_luong_nhap} Điện thoại. Tồn kho hiện tại: {phone_ton_kho}")

            elif chon_hang == "3":
                tablet_ton_kho += so_luong_nhap
                print(f" Đã nhập {so_luong_nhap} Máy tính bảng. Tồn kho hiện tại: {tablet_ton_kho}")

        else:
            # Người dùng không nhập 1, 2, hoặc 3
            print(" Lựa chọn mặt hàng không hợp lệ!")


    #  CHỨC NĂNG 3: XUẤT KHO 
    elif lua_chon == "3":

        print("\n===== XUẤT KHO =====")
        print("Bạn muốn xuất hàng nào?")
        print("  1. Laptop")
        print("  2. Điện thoại")
        print("  3. Máy tính bảng")

        chon_hang = input("Chọn mặt hàng (1-3): ")

        if chon_hang == "1" or chon_hang == "2" or chon_hang == "3":

            # Vòng lặp kiểm tra số lượng âm (giống phần nhập kho)
            while True:
                so_luong_xuat = int(input("Nhập số lượng cần xuất kho: "))

                if so_luong_xuat < 0:
                    print(" Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    break  # Số lượng OK, thoát vòng lặp kiểm tra

            # Xuất kho từng mặt hàng, kèm kiểm tra đủ hàng không
            if chon_hang == "1":
                # So sánh: số lượng muốn xuất có lớn hơn tồn kho không?
                if so_luong_xuat > laptop_ton_kho:
                    print(f" Không đủ hàng! Laptop chỉ còn {laptop_ton_kho} sản phẩm.")
                else:
                    laptop_ton_kho -= so_luong_xuat   # -= tức là laptop = laptop - so_luong_xuat
                    print(f" Đã xuất {so_luong_xuat} Laptop. Tồn kho còn lại: {laptop_ton_kho}")

            elif chon_hang == "2":
                if so_luong_xuat > phone_ton_kho:
                    print(f" Không đủ hàng! Điện thoại chỉ còn {phone_ton_kho} sản phẩm.")
                else:
                    phone_ton_kho -= so_luong_xuat
                    print(f" Đã xuất {so_luong_xuat} Điện thoại. Tồn kho còn lại: {phone_ton_kho}")

            elif chon_hang == "3":
                if so_luong_xuat > tablet_ton_kho:
                    print(f" Không đủ hàng! Máy tính bảng chỉ còn {tablet_ton_kho} sản phẩm.")
                else:
                    tablet_ton_kho -= so_luong_xuat
                    print(f" Đã xuất {so_luong_xuat} Máy tính bảng. Tồn kho còn lại: {tablet_ton_kho}")

        else:
            print(" Lựa chọn mặt hàng không hợp lệ!")


    #  CHỨC NĂNG 4: CẢNH BÁO TỒN KHO THẤP 
    elif lua_chon == "4":

        print("\n===== CẢNH BÁO TỒN KHO THẤP =====")

        co_canh_bao = False  # Biến cờ để biết có mặt hàng nào cảnh báo không

        if laptop_ton_kho < NGUONG_CANH_BAO:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop_ton_kho} sản phẩm)")
            co_canh_bao = True

        if phone_ton_kho < NGUONG_CANH_BAO:
            print(f"[CẢNH BÁO] Mặt hàng Điện thoại sắp hết (Chỉ còn {phone_ton_kho} sản phẩm)")
            co_canh_bao = True

        if tablet_ton_kho < NGUONG_CANH_BAO:
            print(f"[CẢNH BÁO] Mặt hàng Máy tính bảng sắp hết (Chỉ còn {tablet_ton_kho} sản phẩm)")
            co_canh_bao = True

        # Nếu không có mặt hàng nào thấp thì thông báo tốt
        if co_canh_bao == False:
            print(" Tất cả mặt hàng đều đủ hàng. Không có cảnh báo nào!")

        print("===================================")


    #  CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH 
    elif lua_chon == "5":
        print("\nCảm ơn đã sử dụng hệ thống. Tạm biệt! 👋")
        break  # Thoát khỏi vòng lặp while True -> kết thúc chương trình


    # TRƯỜNG HỢP NHẬP SAI (không phải 1-5) 
    else:
        # Người dùng nhập bừa số 6, 7, chữ cái,... thì báo lỗi
        print(" Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 5.")

print("Chương trình đã đóng.")

