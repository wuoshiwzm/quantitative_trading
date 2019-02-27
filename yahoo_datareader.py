import pandas as pd
import datetime
import pandas_datareader.data as web
import statsmodels.tsa.stattools as ts

#从yahoo 拿amzn的数据
# amzn = web.DataReader('AMZN','yahoo',datetime.datetime(2000,1,1), datetime.datetime(2015,1,1))
# print (ts.adfuller(amzn['Adj Close']))
# (0.35739536543512335, 0.97982983072590579, 25, 3748,
# {'1%': -3.4320959403174709,
# '5%': -2.862311460117259,
# '10%': -2.5671806588757691},
# 19372.03872132457)
# 这里看5% 比上面的0.3573953654351233大，说明是不能拒绝的

# print(amzn.head(20))

# 获取数据
start = datetime.datetime(2016,1,1)
end = datetime.date.today()
prices = web.DataReader('AAPL','yahoo',start,end)  #AAPL:苹果 yahoo:数据源
# print(prices.head())


# 获取股利数据 actions表示证券所进行的操作， value表示操作值
actions = web.DataReader('AAPL','yahoo-actions',start,end)
print(actions.head(100))

#合并股利和股价数据
# prices['action'] = actions.action
# prices['action_value'] = actions.value
# print(prices.head())

# 用pandas merge
prices = pd.merge(prices,actions,how='outer',left_index=True,right_index=True)
# print(prices.head())

# 输出为CSV文件
prices.to_csv('.\\out\\AAPL.csv')
print('exported!')




