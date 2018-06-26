import unittest


def merge_ranges(meetings):
    # Merge meeting ranges
    meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
    print("sorted one : ",meetings)
    meetings1 = [meetings[0]]

    for i in range(len(meetings)):
        tupl1 = meetings1[-1]
        print("tup1 :",tupl1)
        tupl2 = meetings[i]
        tupl3=()
        print("tup2 :",tupl2)
        if tupl2[0] <= tupl1[1]:
            print("tup2[0],tup1[1] :",tupl2[0],tupl1[1])
            temp=tupl1[0]
            if tupl1[1]<tupl2[1]:
                temp2=tupl2[1]
            else:
                temp2=tupl1[1]
            #meetings1[-1] = (tupl1[0], max(tupl1[1], tupl2[1]))
            meetings1[-1]=(temp,temp2)
            print("meetings 1 :",meetings1[-1])
        else:
            meetings1.append(tupl2)
        print("end for :",meetings1)
    return meetings1


# Tests

meetings=[(1,2),(3,4),(1,7)]
print(merge_ranges(meetings))