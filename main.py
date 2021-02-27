''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
from myMath import myStatistics

data=[]

for  i in range(1,6):
    data.append(float(input('請輸入5個數以計算平均數，第'+str(i)+'個：')))
  
print(myStatistics.myMean(data))
