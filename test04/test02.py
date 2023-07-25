# 狼子野心，雄行天下
# 为了未来，更好的生活
# 我就不信，我学不会python
# study：2023/7/25 18:24

# 导入所用模块
import pymysql

# 建立于数据库连接
concurrent = pymysql.connect(host='localhost', user='root', password='asdhjjlkfjlaksd23@#433$#%#&^!*)(#)(P*()$al', db='image_lib')

# 建立游标，这个游标是什么，他是一个很重要的东西
# 他为我吧sql语句上传到数据库里面执行
curses = concurrent.cursor()

# 把图片读取到内存中
with open('../resources/无标题.jpg', 'rb') as file:
    image_data = file.read()

sql = 'insert into image(image_data) values(%s)'
curses.execute(sql, (image_data,))

curses.close()
concurrent.commit()
