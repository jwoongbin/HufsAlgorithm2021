def solution(N, stages):
    answer = []
    result = []
    for i in range(1, N+1):
        players = 0
        challenger = 0
        for stage in stages:
            if stage >= i: # 해당 스테이지에 도달
                players += 1
            if stage == i: # 해당 스테이지에 머물고 있음(아직 클리어하지 못함)
                challenger += 1
        if players == 0:
            fail_rate = 0
        else:
            fail_rate = float(challenger / players)
        result.append([fail_rate,i])

    result.sort(key = lambda x: (-x[0]))
    for results in result:
        answer.append(results[1])
    print(answer)
    return answer

solution(5,[2,1,2,6,2,4,3,3])
