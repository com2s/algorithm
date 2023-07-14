# input.txt와 output.txt를 비교하여 파일이 일치하는지 확인합니다.

def compare_files(file1_path, file2_path, ignore_whitespace=False):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    if ignore_whitespace:
        # 공백과 줄바꿈을 제거한 내용으로 비교합니다.
        lines1 = [line.strip() for line in lines1 if line.strip()]
        lines2 = [line.strip() for line in lines2 if line.strip()]

    if lines1 == lines2:
        print("파일이 일치합니다.")
    else:
        print("파일이 일치하지 않습니다.")

        # 서로 다른 부분을 출력합니다.
        for line1, line2 in zip(lines1, lines2):
            if line1 != line2:
                print("첫 번째 파일:", line1)
                print("두 번째 파일:", line2)
                print()

        # 파일의 길이가 다른 경우, 나머지 부분도 출력합니다.
        if len(lines1) > len(lines2):
            for line in lines1[len(lines2):]:
                print("첫 번째 파일:", line)
        elif len(lines1) < len(lines2):
            for line in lines2[len(lines1):]:
                print("두 번째 파일:", line)

# 비교할 두 개의 파일 경로와 공백/줄바꿈 무시 옵션을 지정합니다.
file1_path = 'result.txt'
file2_path = 'output.txt'
ignore_whitespace = True

# 함수를 호출하여 파일을 비교합니다.
compare_files(file1_path, file2_path, ignore_whitespace
                                                        #=False
                                                         )