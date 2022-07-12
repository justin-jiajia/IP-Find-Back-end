# IP Find 后端

[![Python application test](https://github.com/justin-jiajia/IP-Find-Back-end/actions/workflows/python-app.yml/badge.svg)](https://github.com/justin-jiajia/IP-Find-Back-end/actions/workflows/python-app.yml) [![Build and push docker](https://github.com/justin-jiajia/IP-Find-Back-end/actions/workflows/docker.yml/badge.svg)](https://github.com/justin-jiajia/IP-Find-Back-end/actions/workflows/docker.yml)

IP Find是一个包括前、后端的项目，用油猴脚本实现获取页面所有IP归属地。（油猴脚本还没写<笑>）

# 使用方法

1.Pull 镜像
```shell
docker pull jiajia6666/ip-find-back-end
```

2.Run！！

```shell
docker run -d -p 5000:5000 jiajia6666/ip-find-back-end
```

现在它就在你的5000端口上运行了！是不是很简单呢？
