CREATE TABLE 图片 (
  id INT AUTO_INCREMENT PRIMARY KEY,
  文件名 VARCHAR(255),
  文件类型 VARCHAR(50),
  文件数据 LONGBLOB,
  创建时间 TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM `图片`



----------------------------------------------------

SELECT acc,`password`,`describe` 
FROM account_library.`account` 
WHERE `describe` LIKE '%github%'