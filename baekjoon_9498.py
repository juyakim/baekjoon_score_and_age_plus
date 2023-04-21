# 백준 9498번 문제: 시험성적

# 초반에 적어 틀린 답(이정도의 복잡도는 필요없는 문제인듯)
score = int(input("점수를 입력하세요 :"))  # 정수를 input 받기
# 시험 점수를 입력받아 90 ~ 100점은 A,
if score >= 90 and score <= 100:
    result = "A"  # 점수 A result에 저장
# 80 ~ 89점은 B,
elif score >= 80 and score <= 89:
    result = "B"  # 점수 B result에 저장
# 70 ~ 79점은 C,
elif score >= 70 and score <= 79:
    result = "C"  # 점수 C result에 저장
# 60 ~ 69점은 D,
elif score >= 60 and score <= 69:
    result = "D"  # 점수 D result에 저장
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
else:
    result = "F"  # 점수 F result에 저장

# 성적출력
print("해당학생의 성적은{}점 입니다".format(result))  # format 함수를 사용하여 {}안에 결과할당

# format() 매소드를 사용해서 인수로 {} 개수 만큼 문자열이나, 숫자를 추가 해주면
# 해당 값이 차례대로 문자열에 들어간다.


########옳은답(매우간단)

score = int(input())  # int함수 사용- 정수로 변환하여 input 받아 변수에 선언
# 시험 점수를 입력받아 90 ~ 100점은 A,
if score >= 90:
    print("A")  # 점수 A 출력
# 80 ~ 89점은 B,
elif score >= 80:
    print("B")  # 점수 B 출력
# 70 ~ 79점은 C,
elif score >= 70:
    print("C")  # 점수 C 출력
# 60 ~ 69점은 D,
elif score >= 60:
    print("D")  # 점수 D 출력
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
else:
    print("F")  # 점수 F 출력
