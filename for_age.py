import time

my_list = [
    {"이름": "권기현", "나이": 32},
    {"이름": "홍서연", "나이": 20},
    {"이름": "박소진", "나이": 20},
    {"이름": "이미진", "나이": 19},
    {"이름": "이정현", "나이": 18},
    {"이름": "연제건", "나이": 17},
    {"이름": "강유지", "나이": 16},
    {"이름": "김태연", "나이": 15},
    {"이름": "김주영", "나이": 14},
]
# 해당 리스트를 for 문을 돌리면서 자신과 권기현을 제외한 모든 사람들의 나이를 +1 해주세요
for person in my_list:
    if person["이름"] == "권기현":
        # if person['이름']!='권기현':
        pass  # 또는 print('아무것도 안함')
    elif person["이름"] == "김주영":
        pass
    else:
        person["나이"] = person["나이"] + 1

print(my_list)
time.sleep(1)
