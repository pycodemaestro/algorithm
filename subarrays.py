def sub(array):
  arrSize = len(array)
  
  for startPoint in range(arrSize):
    for lenSubArray in range(startPoint, arrSize + 1):
      result = []
      for j in range(startPoint, lenSubArray):
        result.append(array[j])
      if result :
        print(result)
  print([])  
  
if __name__ == '__main__' :    
  sub([1, 2, 3])