django simpleui demo.
---

simpleui demo,默认使用sqlite数据库。
启动步骤请查看下面的内容，如果你没有接触过django 或者 django admin，请先自己去django的官方查看相关文档学习。

simpleui 是一个django admin的ui框架，与代码无关。

# 步骤
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
