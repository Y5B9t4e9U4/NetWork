# 狼子野心，雄行天下
# 为了未来，更好的生活
# 我就不信，我学不会python
# study：2023/7/18 17:20
import pymysql

# 建立与MySQL数据库的连接
connection = pymysql.connect(host='localhost', user='root', password='asdhjjlkfjlaksd23@#433$#%#&^!*)(#)(P*()$al', db='工具人信息数据库')

# 创建游标对象
cursor = connection.cursor()

# 读取图片文件
with open('D:\\python\\NetWork\\resources\\aaa.jpg', 'rb') as file:
    image_data = file.read()

# 执行INSERT语句
sql = "INSERT INTO 图片 (文件数据) VALUES (%s)"
cursor.execute(sql, (image_data,))

# 提交事务
connection.commit()

# 关闭连接
cursor.close()
connection.close()



