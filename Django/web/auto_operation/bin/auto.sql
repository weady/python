use auto_operation;
create table if not exists t_service_distribution (
  f_id int(11) NOT NULL AUTO_INCREMENT,
  f_clustername varchar(20) NOT NULL,
  f_servername varchar(20) NOT NULL,
  f_hostname  varchar(20) NOT NULL,
  f_serverid int(10),
  f_status varchar(10),
  f_description varchar(50),
  f_function varchar(100),
  PRIMARY KEY (f_id),
  KEY cluster_name (f_clustername)
)ENGINE=INNODB  DEFAULT CHARSET=utf8;

create table if not exists t_host_info(
  f_clustername varchar(20) NOT NULL,
  f_hostname  varchar(20) NOT NULL,
  f_liip varchar(15),
  f_hiip varchar(15),
  f_loip varchar(15),
  f_hoip varchar(15),
  f_description varchar(100)
)ENGINE=INNODB  DEFAULT CHARSET=utf8;
