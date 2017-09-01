# seProgram

## 網路情境program

攻擊端:A 
<br>
受害者端:B

### A 端開啟防火牆的 port 40000

#### 暫時性設定
$sudo firewall-cmd --add-port=40000/tcp

#### 永久性設定
$sudo firewall-cmd --add-port=40000/tcp -permanent

#### 顯示目前的設定
$sudo firewall-cmd --list-all

[上述指令參考於此 ](http://blog.xuite.net/tolarku/blog/363801991)

### 使用方法
B端先執行server, A再端執行client。B端將顯示 I get server message. A端將顯示 I get client message. 接著自動結束連線。
