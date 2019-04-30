# ME_paltform 

=======

1、基于python3.6开发    
2、引入celery+rabbitmq,实现定时获取主机信息，并自动入库

![总体设计](https://github.com/jaminlu/ME_paltform/blob/master/%E4%BD%9C%E4%B8%9A%E7%AE%A1%E7%90%86%E5%B9%B3%E5%8F%B0%E8%AE%BE%E8%AE%A1.jpg)

ubuntu系统下需要相关mysqlclient的依赖包：
sudo apt-get install libmysqlclient-dev       
sudo apt install mysql-client-core-5.7
