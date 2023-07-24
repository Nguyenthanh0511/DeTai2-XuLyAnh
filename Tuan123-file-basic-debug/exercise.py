import time
# hàm tính tổng 
def calculate_sum(n):
    total_sum=sum(range(1,n+1))
    return total_sum
#Tổng sự kiện
def calculate_even_sum(n):
    #sử dụng generator comprehension  để optimal 
    # x is iterator (đếm )
    even_sum = sum(x for x in range(n,n+1) if x%2==0) # tổng x lặp từ x đến n tiếp +1 , nếu chẵn thì
    return even_sum

#hàm chính 
def main():
    n = int(input("Nhập một số n: "))
    # Tính tổng các số từ 1 đến n
    sum_result = calculate_sum(n)
    print("Tổng các số từ 1 đến n5: ", sum_result)

    # Tính tổng các số chẵn trong khoảng 1 đến n
    even_sum_result = calculate_even_sum(n)
    print("Tổng các số chẵn trong khoảng 1 đến n: ", even_sum_result)

if __name__ == "__main__":
    # Bắt đầu đếm thời gian
    start_time = time.time()
    # Gọi hàm chính
    main()
    # Kết thúc đếm thời gian và tính thời gian chạy
    end_time = time.time()
    run_time = end_time - start_time
    print("Thời gian chạy của chương trình: ", run_time, " giây")

