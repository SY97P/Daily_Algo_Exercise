def convert_time(time):
    time_info = list(map(int, time.split(':')))
    return 3600*time_info[0] + 60*time_info[1] + time_info[2]

def revert_time(time):
    h = str(time // 3600).zfill(2)
    m = str((time % 3600) // 60).zfill(2)
    s = str(time % 60).zfill(2)
    return "{h}:{m}:{s}".format(h=h, m=m, s=s)


def solution(play_time, adv_time, logs):
    time_bound = convert_time("100:00:00")

    play_time = convert_time(play_time)
    adv_time = convert_time(adv_time)

    time_table = [0]*time_bound

    for log in logs:
        log = log.split('-')
        s, e = convert_time(log[0]), convert_time(log[1])
        time_table[s] += 1
        time_table[e] -= 1

    for i in range(time_bound-1):
        time_table[i+1] += time_table[i]
    for i in range(time_bound-1):
        time_table[i+1] += time_table[i]

    max_cnt = time_table[adv_time]
    answer = 0
    for s in range(time_bound-1):
        e = s + adv_time if s + adv_time < time_bound else time_bound-1
        if time_table[e] - time_table[s] > max_cnt:
            max_cnt = time_table[e] - time_table[s]
            answer = s+1

    return revert_time(answer)


def main():
    answer = solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])
    answer = solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
    answer = solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
    print(answer)


if __name__ == '__main__':
    main()