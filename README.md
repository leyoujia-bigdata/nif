# nif（nginx热部署）
## 描述  
该主要用于解决在使用nginx做分布式部署时，某一台服务器启动时，请求不通的情况；在项目启动的过程中，该项目可自动屏蔽对应的项目；  

## 运行环境说明
1. 系统：linux/windows
2. 语言：python2.7以上
3. 插件安装：pip或者pip3

## 配置说明
下载该项目后，更改config.ini的配置
```
  [WebServer]
  web-server-port = 8015
  web-server-ip = 0.0.0.0
  
  [Nginx]
  nginx-config-path = nginx.conf
  nginx-path = ./sbin/nginx
```

webServer 代表服务发布的配置  
1. port代表服务发布的端口
2. ip代表可访问的ip 0.0.0.0 表示都可以访问

nginx 代表nginx对应的地址

## 部署说明
linux下载命令：wget -c https://github.com/tandangfei/nif/archive/master.zip   
依赖的插件请查看requirements.txt  
```
pip安装命令：wget https://bootstrap.pypa.io/get-pip.py  
python get-pip.py  
```
linux安装关联的插件命令：pip freeze >requirements.txt  


## 使用说明
运行命令：python webServer.py  ||  nohup python webServer.py &  
运行后访问：http://{ip}:{port}/auto_nginx?type=1&ip=127.0.0.1&port=8080
1. type代表是屏蔽还是打开 1=屏蔽 2=打开
2. ip 代表要屏蔽/打开的ip
3. port 代表要屏蔽/打开的port

## 回滚说明
1. 在屏蔽或者打开时，如果启动nginx错误，会自动回滚并启动
2. 如果自动回滚错误，可以在ngixn服务器上面找到备份的nginx（格式：closeServer_nginx.conf20201116135306）配置文件，进行人工回滚
