import pandas as pd
import datetime
import pandas_datareader.data as web
import statsmodels.tsa.stattools as ts

#从yahoo 拿amzn的数据
amzn = web.DataReader('AMZN','yahoo',datetime.datetime(2000,1,1), datetime.datetime(2015,1,1))
print (ts.adfuller(amzn['Adj Close']))
# (0.35739536543512335, 0.97982983072590579, 25, 3748,
# {'1%': -3.4320959403174709,
# '5%': -2.862311460117259,
# '10%': -2.5671806588757691},
# 19372.03872132457)
# 这里看5% 比上面的0.3573953654351233大，说明是不能拒绝的

# print(amzn.head(20))





