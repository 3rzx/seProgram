# seProgram

## attack_client attack_server

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

### 執行說明
A 端先執行 attack_server, server 便會開始聽取來自網路的連線，確認是否有人要連接，接著 B 端執行 attack_client，與 A 端建立連線。A 端會送出 `I get server message.` B 端接收到後會顯示出來並向 A 端傳送 `I get client message.` A 端接收到後一樣會顯示在畫面上，接著便結束兩者的連線。

## ransomware
由 ransomware.c 編譯而成

**執行後**
- 將名為 file 的檔案壓縮成 zip 檔
- 並設定壓縮密碼，密碼可在原始碼中查看
- 最後刪除原檔 file
