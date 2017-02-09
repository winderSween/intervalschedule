# Tyler Moore
# 09/22/2016
# HW3 Q1 Starter Code
# Implementation of interval partitioning algorithm
import datetime
from heapq import heappush , heappop

def scheduleRooms(rooms,cls):
    """
    Input: rooms - list of available rooms
           cls   - dictionary mapping class names to pair of (start,end) times
    Output: Return a dictionary mapping the room name to a list of
    non-conflicting scheduled classes.
    If there are not enough rooms to hold the classes, return 'Not enough rooms'.
    """
    rmassign = {}
    orderedcls = sorted([(value[1], value[0], key) for (key, value) in cls.items()])

    # 2. arrange class to classroom one by one
    for r in rooms:
        queue=[]
        for value in orderedcls:
            heappush(value(0,rm1))


    #     if len(orderedcls) == 0:
    #         break
    #     # select the first class for room r
    #     first = orderedcls[0]
    #     clsbak = orderedcls[1:]
    #     rmassign[r] = [first[2]]
    #     endtime = first[0]
    #
    #     for x in orderedcls[1:]:
    #         if x[1] >= endtime:  # add class for room r, greedy select
    #             rmassign[r].append(x[2])
    #             endtime = x[0]  # update endtime
    #             clsbak.remove(x)
    #
    #     orderedcls = clsbak[:]
    #
    # if len(orderedcls) > 0:
    #     return 'Not enough rooms'

    return rmassign

if __name__=="__main__":
    cl1 = {"a": (datetime.time(9),datetime.time(10,30)),
           "b": (datetime.time(9),datetime.time(12,30)),
           "c": (datetime.time(9),datetime.time(10,30)),
           "d": (datetime.time(11),datetime.time(12,30)),
           "e": (datetime.time(11),datetime.time(14)),
           "f": (datetime.time(13),datetime.time(14,30)),
           "g": (datetime.time(13),datetime.time(14,30)),
           "h": (datetime.time(14),datetime.time(16,30)),
           "i": (datetime.time(15),datetime.time(16,30)),
           "j": (datetime.time(15),datetime.time(16,30))}
    rm1 = [1,2,3]
    print cl1
    print scheduleRooms(rm1,cl1)
    print scheduleRooms([1,2],cl1)
    ensrooms = ['KEH U1','KEH M1','KEH M2','KEH M3','KEH U2','KEH U3','KEH U4','KEH M4','KEH U8','KEH U9']
    csclasses = {'CS 1043': (datetime.time(9,30),datetime.time(11)),
              'CS 2003': (datetime.time(10,30),datetime.time(12)),
              'CS 2123': (datetime.time(11,15),datetime.time(12,45)),
              'CS 3003': (datetime.time(8,15),datetime.time(11,30)),
              'CS 3353': (datetime.time(11),datetime.time(12)),
              'CS 4013': (datetime.time(13),datetime.time(14,45)),
              'CS 4063': (datetime.time(12,30),datetime.time(14,30)),
              'CS 4123': (datetime.time(14),datetime.time(15)),
              'CS 4163': (datetime.time(14),datetime.time(16,30)),
              'CS 4253': (datetime.time(12),datetime.time(16)),
    }
    print csclasses
    print scheduleRooms(ensrooms,csclasses)
    print scheduleRooms(ensrooms[:4],csclasses)