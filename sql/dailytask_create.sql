CREATE TABLE `daily_task` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '任务id',
  `uid` varchar(20) NOT NULL DEFAULT '' COMMENT '用户uid',
  `content` varchar(255) NOT NULL DEFAULT '0.00' COMMENT '内容',
  `summary` varchar(255) NOT NULL DEFAULT '' COMMENT '总结',
  `state` int(11) NOT NULL DEFAULT '0' COMMENT '进度',
  `create_time` datetime NOT NULL DEFAULT '' COMMENT '最近更新时间',
  `aim` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '关联周目标',
  `task_time` DATETIME NOT NULL DEFAULT '' COMMENT '任务时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='日常任务表'