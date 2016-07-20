use auto_operation;
create table if not exists t_service_distribution (
  id int(11) NOT NULL AUTO_INCREMENT,
  cluster_name varchar(20) NOT NULL,
  server_name varchar(20) NOT NULL,
  hostname  varchar(20) NOT NULL,
  server_id int(10),
  status int(2) DEFAULT '0',
  note varchar(50),
  server_function varchar(100),
  PRIMARY KEY (id),
  KEY cluster_name (cluster_name)
)ENGINE=INNODB  DEFAULT CHARSET=utf8;

create table if not exists t_host_info(
  cluster_name varchar(20) NOT NULL,
  hostname  varchar(20) NOT NULL,
  li_ip varchar(15),
  hi_ip varchar(15),
  lo_ip varchar(15),
  ho_ip varchar(15),
  note varchar(100)
)ENGINE=INNODB  DEFAULT CHARSET=utf8;
