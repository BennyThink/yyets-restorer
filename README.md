# yyets-restorer
用来解密人人影视客户端下载的视频的工具



## 人人影视客户端直链接下载 ##
```
GET http://www.zmzfile.com/file/search?keyword=%E9%80%83%E9%81%BF%E5%8F%AF%E8%80%BB
```
keyword=为要搜索的关键词，可以为url编码。

返回：

```
[
    {
        "file_name": "逃避可耻却有用.NIGERUHA.HAJIDAGA.YAKUNITATSU.Ep01.Chi_Jap.HDTVrip.1280X720-ZhuixinFanV2.mp4",
        "file_size": 733967923,
        "fileid": "fa1a42ee8066da0aa2b66ca470814489160ad214",
        "url": "https://www.zmzfile.com:9043/rt/route?fileid=fa1a42ee8066da0aa2b66ca470814489160ad214"
    },
    {
        "file_name": "逃避可耻却有用.NIGERUHA.HAJIDAGA.YAKUNITATSU.Ep02.Chi_Jap.HDTVrip.1280X720-ZhuixinFan.mp4",
        "file_size": 629086728,
        "fileid": "d21a081cc6a32daa85310ca6aad81e378f0b736e",
        "url": "https://www.zmzfile.com:9043/rt/route?fileid=d21a081cc6a32daa85310ca6aad81e378f0b736e"
   },
   以下省略………………
]
```
对URL继续进行get，经过几轮重定向之后，即可得到真正的下载地址（根据你的IP重定向到不同的服务器）。
然后可以使用curl url -C - -Lv -o xxx.mp4下载。

## 加密原理 ##
原理由[JasonKhew96](https://github.com/BennyThink/ExpressBot/issues/3)提供，在此非常感谢他的工作！

简单复述下就是使用md5(file_id+'zm'+file_id)作为key，以aes-128-ecb每4096个字节加密前16个字节。

## 使用方法 ##
需要Python（2、3均可），先安装cryptography
```bash
pip install cryptography
```
然后运行如下命令：
```bash
python restore.py sample.mp4 fb755fd1b51c769bfed987e2a8c8b03ee7a8e7cc
```
或者直接使用release下的二进制文件
```cmd
restore.exe sample.mp4 fb755fd1b51c769bfed987e2a8c8b03ee7a8e7cc
```

## 另请参见 ##
* [人人影视客户端](http://app.zimuzu.tv/)
* [关于被加密的视频文件](https://github.com/BennyThink/ExpressBot/issues/3)
* [ExpressBot](https://github.com/BennyThink/ExpressBot)

## License ##
Apache License 2.0