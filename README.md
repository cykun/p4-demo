# p4-demo
## 环境
p4c

bmv2

p4runtime

## 项目文件
```
\include         p4 子模块
  checksum.p4    数据包头校验
  define         数据字段定义
  headers.p4     数据包头定义
  parser.p4      数据报头解析
\util            p4 与 mininet 结合脚本
main.p4          p4 主函数
s1-runtime.json  s1 配置文件
s1-runtime.json  s2 配置文件
s3-runtime.json  s3 配置文件
topology.json    拓扑文件
```
## Topo

                     c1
               /     |     \
             /       |       \
    h1 ---- s1 ----- s2 ----- s3 ----- h2
## 运行
```
git clone https://github.com/cykun/p4-demo
cd p4-demo
make run
```