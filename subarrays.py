def sub(array):
  arrSize = len(array)
  
  for startPoint in range(arrSize):
    for lenSubArray in range(startPoint, arrSize + 1):
      result = []
      for j in range(startPoint, lenSubArray):
        result.append(array[j])
      print(result)
    
sub([1, 2, 3])