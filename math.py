# def get_p(lists):
#   result = []
#   if len(lists) == 1:
#     return [lists]
    
#   for i in range(len(lists)):
#     g = lists[i]
#     n = lists[:i] + lists[i+1:]
     
#     zip = get_p(n)

#     for j in zip:
#       result.append([lists[i]]+j)

#   return result

# def get_c(lists, r):
#   if r == 0:
#     return [[]]
#   if len(lists) == 0:
#     return []
#   result = []
#   for i in range(len(lists)):
#     s = lists[i]
#     n = lists[i+1:]

#     cc = get_c(n, r-1)

#     for j in cc:
#       result.append([s]+j)

#   return result

## A번 1번
# def get_p(lists):
#     result = []
#     if len(lists) == 1:
#         return [lists]

#     for i in range(len(lists)):
#         n = lists[:i] + lists[i+1:]

#         zip = get_p(n)

#         for j in zip:
#             result.append([lists[i]] + j)

#     return result


# perms = get_p("a b c d e".split())

# count = 0

# for p in perms:
#     a = p.index('a')
#     e = p.index('e')

#     if abs(a - e) == 1:
#         count += 1

# print("경우의 수:", count)

## 2번
# perms = get_p("a b c d e".split())

# count = 0
# vowel = ['a', 'e']

# for p in perms:
#     if (p[0] not in vowel and
#         p[1] in vowel and
#         p[2] not in vowel and
#         p[3] in vowel and
#         p[4] not in vowel):
#         count += 1

# print("경우의 수:", count)

##B번 1번
# def get_c(lists, r):
#   result = []
#   if r == 0:
#     return [[]]
#   if len(lists) == 0:
#     return []
#   for i in range(len(lists)):
#     s = lists[i]
#     n = lists[i+1:]

#     cc = get_c(n, r-1)

#     for j in cc:
#       result.append([s]+j)

#   return result

# cards = [1,2,3,4,5,6,7,8,9]

# combs = get_c(cards, 3)

# count = 0

# for c in combs:
#     if 7 in c:
#         count += 1

# print(count)

##B번 2번
# def get_c(lists, r):
#   result = []
#   if r == 0:
#     return [[]]
#   if len(lists) == 0:
#     return []
#   for i in range(len(lists)):
#     s = lists[i]
#     n = lists[i+1:]

#     cc = get_c(n, r-1)

#     for j in cc:
#       result.append([s]+j)

#   return result

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# combs = get_c(cards, 3)

# count = 0

# for c in combs:
#   even = 0
#   odd = 0

#   for num in c:
#     if num % 2 == 0:
#       even += 1
#     else :
#       odd += 1
#   if even == 2 and odd == 1:
#     count += 1

# print(count)