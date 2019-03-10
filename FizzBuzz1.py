number = int(input("数字を入れてね: "))

if number % 15 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("number")

# 最初が適用されるので15を3の前に持っていった
# 3が最初だと15の時にFizzが発動してまうので15を最初に持っていった
