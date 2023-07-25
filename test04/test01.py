# 从数据库中用download image

import pymysql
import os

# 建立与MySQL数据库的连接
connection = pymysql.connect(host='localhost', user='root', password='asdhjjlkfjlaksd23@#433$#%#&^!*)(#)(P*()$al', db='image_lib')

# 创建游标对象
cursor = connection.cursor()

# 查询图片数据
sql = "SELECT image_data FROM image WHERE id = %s"
image_id = 1  # 假设图片的ID为1
cursor.execute(sql, (image_id,))
result = cursor.fetchone()

if result:
    image_data = result[0]
    # 将图片数据保存为本地图片文件
    with open('image.jpg', 'wb') as file:
        file.write(image_data)

# 关闭连接
cursor.close()
connection.close()
