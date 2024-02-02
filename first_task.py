
start = [2024, 6, 12, 14, 15, 16]
end = [2024, 6, 12, 14, 20, 16]

def get_days_and_seconds(start:list, end:list):
    days_in_mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    start_days = (start[0]*365)+(sum(days_in_mounth[:start[1]-1]))+start[2]
    end_days = (end[0]*365)+(sum(days_in_mounth[:end[1]-1]))+end[2]
    days_result= end_days - start_days

    assert end_days>=start_days , 'Так не получится'

    start_seconds = (start[3]*60*60)+(start[4]*60)+(start[5])
    end_seconds = (end[3] * 60 * 60) + (end[4] * 60) + (end[5])
    second_result = end_seconds - start_seconds


    if end_seconds < start_seconds:
        days_result -= 1
        second_result = (24 * 60 * 60+end_seconds)-start_seconds


    return days_result,second_result

if __name__ == '__main__':
    assert get_days_and_seconds([980, 2, 12, 10, 30, 1],[ 980, 3, 1,10, 31, 37]) == (17,96)
    assert get_days_and_seconds([2024, 6, 12, 14, 20, 16], [2024, 6, 12, 14, 20, 16]) == (0, 0)
    assert get_days_and_seconds([1001, 5, 20, 14, 15, 16], [9009, 9, 11, 12, 21, 11]) == (2923033, 79555)
