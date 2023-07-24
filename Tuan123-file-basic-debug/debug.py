# def calculate_division(a, b):
#     result = a / b
#     return result

# a = 10
# b = 0
# division_result = calculate_division(a, b)
# print("Kết quả chia:", division_result)

# #Nhấn tổ hợp phím Ctrl + Shift + D
# #Trong tab Debug, nhấp vào nút "Create a launch.json file" để tạo file cấu hình debug.
# #


def calculate_sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

# Dãy số cần tính tổng
numbers = [1, 2, 3, 4, 5]

# Bước debug
# 1. Đặt breakpoint tại dòng total_sum += number để kiểm tra giá trị của biến number và total_sum
# 2. Nhấn F5 hoặc Start Debugging để bắt đầu debug
# 3. Chương trình sẽ dừng lại tại điểm dừng và bạn có thể kiểm tra giá trị của biến number và total_sum trong tab "Variables"
# 4. Sử dụng các nút điều khiển debug để đi từng bước (Step Over, Step Into, Step Out) và theo dõi giá trị của biến trong quá trình thực thi
# 5. Khi kết thúc debug, kết quả tổng sẽ được hiển thị

sum_result = calculate_sum(numbers)
print("Tổng của dãy số:", sum_result)
#XIN CHÀO BẠN 