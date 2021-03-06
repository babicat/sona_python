import re   #특수문자 제거
import collections #리스트 내 아이템 카운트 및 정렬


def read_file(url) :
    # 파일 불러오기
    f = open(url, 'rt', encoding='UTF8')
    # 불러온 파일을 라인별로 split 해서 리스트로 저장
    line_data = f.read().splitlines()
    f.close()
    # 첫번째 값 삭제
    # del(line_data[0])

    return line_data



def create_list(read_data) :
    new_data = []

    #주석 및 필요없는 줄 제거
    for n in range(len(read_data)) :
        if read_data[n].startswith('--') == True :
            pass
        
        elif read_data[n].startswith('INSERT') == True :
            pass
        
        #문제있는 부분-----------------------------------------------
        elif read_data[n] == None:
            pass

        else :
            # 특수문자 및 공백 제거
            read_data[n] = re.sub("[';() ]", "", read_data[n])
            # , 기준으로 split
            read_data[n] = read_data[n].split(",")
            # 필요한 값만 빼서 새 리스트에 넣기
            new_data.append([read_data[n][1], read_data[n][3]])

    return new_data



def create_dict(create_list) :
    # 로그 value와 매칭 시킬 키 값 리스트 생성
    key = ['sno', 'typelog']
    create_dict = []

    # key와 value를 매칭시키고 dict형으로 변환
    for n in range(len(create_list)) : 
        create_dict.append(dict(zip(key, create_list[n])))
    
    return create_dict



def top_typelog(userlogs, rank) :
    value_list = []

    # value만 value_list 리스트에 append
    for i in range(len(userlogs)) :
        value_list.append(userlogs[i]['typelog'])

    # Counter 함수로 데이터 개수를 count
    value_list = collections.Counter(value_list)
    # count가 높은 순으로 내림차순 정렬
    top_typelog = value_list.most_common(rank)

    print("[Top ", rank, " typelog]\n")

    for i in range (0, rank) :
        print("┌No.",i+1," : ", top_typelog[i][0], "\n└count : ", top_typelog[i][1] )




def total_log(userlogs) :
    print("\nTotal userlogs : ", len(userlogs))



def sno_count(userlogs, typelog) :
    count_user = []

    for n in range(len(userlogs)) : 
        if typelog in (userlogs[n].values()) :
            count_user.append(userlogs[n]['sno'])

    if not count_user :
        print(typelog, "is not exist.")
    else :
        print("\n", typelog, "in", len(set(count_user)), "SNO(s).\n")




def typelog_count(userlogs, sno) :
    count_typelog = []

    for n in range(len(userlogs)) : 
        if sno in (userlogs[n].values()) :
            count_typelog.append(userlogs[n]['typelog'])

    if not count_typelog :
        print(sno, "is not exist.")
    else :
        count_typelog = collections.Counter(count_typelog)
        # count가 높은 순으로 내림차순 정렬
        count_typelog = count_typelog.most_common()
        print("\n[", sno, "'s typelog]\n")
        for i in range (0, len(count_typelog)) :
           print("┌Typelog : ", count_typelog[i][0], "\n└count : ", count_typelog[i][1] )
