def get_p(lists):
  result = []
  if len(lists) == 1:
    return [lists]
    
  for i in range(len(lists)):
    g = lists[i]
    n = lists[:i] + lists[i+1:]
     
    zip = get_p(n)

    for j in zip:
      result.append([lists[i]]+j)

  return result

def get_c(lists, r):
  if r == 0:
    return [[]]
  if len(lists) == 0:
    return []
  result = []
  for i in range(len(lists)):
    s = lists[i]
    n = lists[i+1:]

    cc = get_c(n, r-1)

    for j in cc:
      result.append([lists[s]]+j)

  return result