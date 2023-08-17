# input() : 터미널에서, 문자열을 입력하는 형식
print("이메일을 입력해주세요")
email: input()
print(f"입력된 이메일은 : {email}")

print("hello python")
# ctrl + f5
a = 300
print(type(a))
b = 200
b = str(a)
print(b)
print(type(b))
result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)
# 코틀른 로그캣 출력
# Log.d("khs", "출력하기 ㅁ : ${a}")

print("출력형식 %d" % (a))
