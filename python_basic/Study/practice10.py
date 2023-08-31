# 10-1) 예외처리
'''
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번재 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번재 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))  # 깜빡
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러 : 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
    print("알 수 없는 에러가 발생하였습니다.")
'''



# 10-2) 에러 발생시키기
'''
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번재 숫자를 입력하세요 : "))
    num2= int(input("두 번재 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError  # 의도적으로 ValueError 를 발생시킴

    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''

''''''
# 10-3) 사용자 정의 예외처리

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번재 숫자를 입력하세요 : "))
    num2= int(input("두 번재 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {}, {}".format(num1, num2))
        # 의도적으로 에러를 발생시킴

    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
except Exception as err:
    print(err)
# 10-4) finally : 에러 유무와 상관없이 무조건 출력
finally:
    print("계산기를 이용해 주셔서감사합니다")