# ------------------------------------------
# 👨‍💻 Parsa Heidari - تمرین کوچک‌ترین مضرب مشترک
# ------------------------------------------

import math

# تابع برای محاسبه LCM دو عدد
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# تابع برای محاسبه LCM چند عدد در لیست
def lcm_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# 🧪 تست برنامه
nums = [4, 6, 8]
print("لیست اعداد:", nums)
print("کوچک‌ترین مضرب مشترک (LCM):", lcm_list(nums))
