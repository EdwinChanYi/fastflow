CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `uid` int(11) unsigned NOT NULL COMMENT 'uid,业务使用此id',
  `code` varchar(20) NOT NULL DEFAULT '' COMMENT '商店代码',
  `password` varchar(255) NOT NULL DEFAULT '' COMMENT '密码',
  `nickname` varchar(50) NOT NULL DEFAULT '' COMMENT '昵称',
  `age` int(1) NOT NULL DEFAULT '0' COMMENT '年龄',
  `sex` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1:男,2:女',
  `register_time` int(11) NOT NULL DEFAULT '0' COMMENT '注册时间',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '邮箱',
  `phone` varchar(20) NOT NULL DEFAULT '' COMMENT '手机号',
  `open_id` varchar(255) NOT NULL DEFAULT '' COMMENT '微信open_id',
  `union_id` varchar(255) NOT NULL DEFAULT '' COMMENT '微信union_id',
  `province` varchar(10) NOT NULL DEFAULT '' COMMENT '省份',
  `city` varchar(10) NOT NULL DEFAULT '' COMMENT '城市',
  `status` tinyint(1) DEFAULT NULL COMMENT '-1:禁用,1-正常',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) DEFAULT NULL COMMENT '最近更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表'