# -*- coding: utf-8 -*
# @Time    : 2023/2/9 15:24
# @Author  : liuy
# @File    : data_analysis.py
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)


def main():
    print("这是程序的入口")


"""
1.4 数据清洗
    1. 数据导入
    2. 查看缺失值
    3. 查看异常值
    4. 确定每一列的数据类型，特别是时间类数据类型
1.5 指标体系搭建
    1. 一级指标
        销售额
        销量
        毛利
    2. 
    
"""
# 1.4.1. 数据导入
RawData = pd.read_csv("static/data/superstore_dataset2011-2015.csv", encoding="ISO-8859-1")
# 1.4.2. 查看缺失值
# print(RawData.info())
# print(RawData.isnull().sum())

# 1.4.3. 查看异常值
# print(round(RawData.describe(), 2))

# 1.4.4. 确定每一列的数据类型，特别是时间类数据类型
RawData["Order Date"] = pd.to_datetime(RawData["Order Date"])
RawData["Ship Date"] = pd.to_datetime(RawData["Ship Date"])

# 1.5 指标体系搭建
"""
销售额（年，季度，月，周）
    如果要统计销售额应该对订单的时间列进行分组聚合
    在pandas中可以对时间数据进行很方便的处理，比如获取时间序列的年，月，日，和聚合为季度等
"""
RawData["Order_year"] = RawData["Order Date"].dt.year
RawData["Order_month"] = RawData["Order Date"].dt.month
RawData["Order_quarter"] = RawData["Order Date"].dt.to_period("Q")
# 按年统计出每年的销售额，销量，利润，发货成本
Order_year = round(RawData.groupby(by="Order_year").sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)

# 按季度统计每季度的销售额，销量，利润，发货成本
Order_quarter = round(RawData.groupby(by="Order_quarter").sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)

# 按月统计每季度的销售额，销量，利润，发货成本
Order_month = round(RawData.groupby(by=["Order_year", "Order_month"]).sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)

data = {}
print(Order_year)
data["Order_year"] = Order_year
data["Order_year_index"] = list(Order_year.index.values)
data["Order_year_sales_values"] = list(Order_year["Sales"])
data["Order_quarter"] = Order_quarter
data["Order_month"] = Order_month
print(data)
if __name__ == '__main__':
    print("程序结束！")
