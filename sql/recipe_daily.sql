CREATE TABLE `week_aim` (
  `id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '序号',
  `state` int(8) unsigned NOT NULL DEFAULT '0' COMMENT '进度',
  `aim` VARCHAR(50000) DEFAULT '' COMMENT '目标',
  `create_time` TIMESTAMP NOT NULL COMMENT '创建时间',
  `uid` INT(11) UNSIGNED NOT NULL COMMENT '用户uid',
  `summary` VARCHAR(255) DEFAULT '' COMMENT '总结',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='周目标表'