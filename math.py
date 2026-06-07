# 순열 코드
# def get_p(lists):
#     result = []
#     if len(lists) == 1:
#         return [lists]
#     else:
#         for i in range(len(lists)):
#             s = lists[i]
#             n = lists[:i] + lists[i+1:]

#             hap = get_p(n)

#             for j in hap:
#                 result.append([s]+j)
    
#     return result


# A문제 1번
# lists = list(map(str, input().split()))

# def get_ea(lists):
#     result1 = get_p(lists)
#     result2 = []
#     for rows in result1:
#         new_row = []

#         for words in rows:
#             if words =='ae':
#                 words = 'ea'
#                 new_row.append(words)
#             else:
#                 new_row.append(words)
#         result2.append(new_row)

#     return result1 + result2

# print(len(get_ea(lists)))

#A문제 2번
# def get_zamo(li1, li2):
#     result = []
#     o_p = get_p(li1)
#     t_p = get_p(li2)

#     for i in o_p:
#         for j in t_p:
#             result.append([i[0],j[0],i[1],j[1],i[2]])
#     return result

# consonants = ['b', 'c', 'd']
# vowels = ['a', 'e']

# print(len(get_zamo(consonants, vowels)))

# def get_c(lists, r):
#     result = []
#     if r == 1:
#         return [[i] for i in lists]
    
#     for i in range(len(lists)):
#         s = lists[i]

#         n = lists[i+1:]
#         hap = get_c(n, r-1)

#         for j in hap:
#             result.append([s]+j)
#     return result

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#B문제 1번
# def get_s(lists, r):
#     result1 = []
#     s = 7
#     lists.remove(7)
#     result2 = get_c(lists, r-1)
#     for i in result2:
#         result1.append([s]+i)

#     return result1

# print(len(get_s(cards, 3)))

#B문제 2번
# def get_hz(lists):
#     hol = [x for x in lists if x % 2 != 0]
#     zzak = [x for x in lists if x % 2 == 0]

#     hol_c = get_c(hol, 1)
#     zzak_c = get_c(zzak, 2)

#     result = []
#     for i in hol_c:
#         for j in zzak_c:
#             result.append(i+j)
#     return result

# print(len(get_hz(cards)))