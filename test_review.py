def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]  # 인덱스로 접근하는 비효율적 코드
    return total

def unsafe_eval(code_str):
    # 보안상 위험한 eval 함수 예시
    return eval(code_str)

def simple_greeting(name):
    print("Hello, " + name + "!")  # 문자열 연결법 개선 가능

# TODO: 함수 주석 보강 필요