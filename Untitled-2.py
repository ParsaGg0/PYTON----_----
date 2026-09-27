# ------------------------------------------
# 👨‍💻 Parsa Heidari - Maximum Quadratic Function
# موضوع: پیدا کردن بیشینه تابع برای مقادیر مختلف k
# ------------------------------------------


def maximum_point(k):
    x_max = k / 2
    y_max = -(x_max**2) + k * x_max + 10

    return x_max, y_max


best_k = None
best_x = None
best_y = None

for k in range(2, 9):
    x_max, y_max = maximum_point(k)

    print(f"k = {k} | x_max = {x_max} | y_max = {y_max}")

    if best_y is None or y_max > best_y:
        best_k = k
        best_x = x_max
        best_y = y_max


print("\n--- نتیجه نهایی ---")
print("بهترین مقدار k:", best_k)
print("مقدار x در نقطه بیشینه:", best_x)
print("بیشترین مقدار y:", best_y)
