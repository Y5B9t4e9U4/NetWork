import pandas as pd  # 导入工具模块
import numpy as np


data = pd.read_excel('D:\\\python\\NetWork\\resources\\工具人档案2.xlsx')  # 操作文件

data = data.replace({np.nan: None})


insert_statements = []

for index, row in data.iterrows():
    values = " ,".join(f"'{str(value)}'" if value is not None else 'NULL' for value in row)
    insert_statement = f"insert into 工具人信息数据库.工具人信息(id, 姓名, 身份证号, 民族, 户籍详细地址, 户籍所在地, 父亲身份证号, 母亲姓名, 母亲身份证号, 家长姓名, 家长电话, 学生电话) values({values})"
    insert_statements.append(insert_statement)


with open('a.sql', 'w', encoding='utf-8') as file:
    file.write('\n'.join(insert_statements))