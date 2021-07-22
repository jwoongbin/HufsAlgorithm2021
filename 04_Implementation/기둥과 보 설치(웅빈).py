def check(answer):
    for x, y, item in answer:
        if item == 0:  # 구조물이 기둥일 경우
            # 해당 좌표가 바닥이거나, 기둥 위거나 보 위면 설치 가능
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:  # 허공이면 불가능
                return False

        else:  # 구조물이 '보'일 경우
            # 오른쪽 혹은 왼쪽이 기둥인 경우, 양 옆이 '보'인 경우 설치 가능
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x + 1, y, 1] in answer and [x - 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, item, command in build_frame:
        # 명령이 설치일 경우
        if command == 1:
            answer.append([x, y, item])
            if not check(answer):
                answer.remove([x, y, item])


        # 명령이 삭제일 경우
        else:  # command == 0:
            if [x, y, item] in answer:
                answer.remove([x, y, item])
                if not check(answer):
                    answer.append([x, y, item])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
