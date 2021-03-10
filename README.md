django simpleui demo.
---

<center>
<a href="https://github.com/newpanjing/simpleui">Simple UI源码</a> |
<a href="https://simpleui.88cto.com">Simple社区</a> 
</center>

simpleui demo,默认使用sqlite数据库。
启动步骤请查看下面的内容，如果你没有接触过django 或者 django admin，请先自己去django的官方查看相关文档学习。

simpleui 是一个django admin的ui框架，与代码无关。

# Docker

demo制作了官方的镜像，可以直接拉取使用

```shell
docker pull newpanjing/simpleui_demo

docker run -p 8080:8080 newpanjing/simpleui_demo
```

启动成功后访问：http://127.0.0.1:8080



# 自动安装
Linux或者macOS可以直接运行`bootstrap.sh`脚本，自动配置虚拟环境、安装依赖包、启动运行
```shell
sh ./bootstrap.sh
```

# 手动步骤

## 第一步
下载源码到本地
```shell
git clone https://github.com/newpanjing/simpleui_demo
```

## 第二步
安装依赖包

```shell
pip install -r requirements.txt
```

## 第三步
```shell
python manage.py runserver 8000 
```

## 第四步
打开浏览器，在地址栏输入以下网址
> http://localhost:8000/admin

## 第五步
在用户名和密码的框框输入
+ 用户名：simpleui
+ 密码：demo123456


## PS
+ 有任何疑问请加入QQ群：786576510
+ 或者前往社区提问搜索答案：[Simple社区](https://simpleui.88cto.com)