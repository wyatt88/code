-- --------------------------------------------------------
-- 主机:                           192.168.1.106
-- 服务器版本:                        5.1.44 - Source distribution
-- 服务器操作系统:                      apple-darwin8.11.1
-- HeidiSQL 版本:                  8.2.0.4675
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 studentprice 的数据库结构
DROP DATABASE IF EXISTS `studentprice`;
CREATE DATABASE IF NOT EXISTS `studentprice` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `studentprice`;


-- 导出  表 studentprice.student 结构
DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `sid` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '序号',
  `phone` varchar(11) NOT NULL DEFAULT '' COMMENT '手机号',
  `password` varchar(30) NOT NULL DEFAULT '' COMMENT '密码',
  `sname` varchar(15) DEFAULT '' COMMENT '姓名',
  `school` varchar(15) DEFAULT '' COMMENT '学校',
  `grade` int(2) DEFAULT NULL COMMENT '年级（0-大一；1-大二）',
  `regtime` datetime NOT NULL COMMENT '注册时间',
  `image` varchar(100) DEFAULT NULL COMMENT '照片目录',
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  studentprice.student 的数据：~0 rows (大约)
DELETE FROM `student`;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
