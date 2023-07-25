# 狼子野心，雄行天下
# 为了未来，更好的生活
# 我就不信，我学不会python
# study：2023/7/18 17:20
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='asdhjjlkfjlaksd23@#433$#%#&^!*)(#)(P*()$al', db='image_lib')
# 建立与MySQL数据库的连接

# 创建游标对象
cursor = connection.cursor()

# 读取图片文件
with open('D:\\python\\NetWork\\resources\\杨玉环.jpg', 'rb') as file:
    image_data = file.read()

# 执行INSERT语句
sql = "INSERT INTO image(image_data2)  VALUES (%s)"
cursor.execute(sql, (image_data,))

# 提交事务
connection.commit()

# 关闭连接
cursor.close()
connection.close()



