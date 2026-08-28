
import re
"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""

def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수
    회문 : 이효리 -> 이효리 / 앞뒤가 똑같은 문자열
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용
    # pass
    lower_s = s.lower()
    clean_s = lower_s.replace(" ", "")
    
    clean_s = re.sub(r'[^a-zA-Z가-힣0-9\s]', '', clean_s)
        
    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투 포인터 방식
    # pass
    
    # 8/28 문제풀이 point
    # 투 포인터 방식에서 끝을 어떻게 낼지가 어려움
    # 입력값 특수문자 제거 구글링
    
    
    # 인덱스 비교 
    result = 22
    start = 0
    end = len(clean_s) - 1

    while start < len(clean_s) and end > 0:
        # start 인덱스가 end 를 넘어가면 while 문 종료
        if start > end :
            break        
        
        # 첫글자 마지막 글자 다르면 return 
        if clean_s[start] != clean_s[end]:
            return False
        
        # 인덱스 증가
        start += 1
        end -= 1
        
    #  while 문 통과 시 회문
    return True

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


