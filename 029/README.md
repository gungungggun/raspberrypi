# Macとラズパイをシリアル接続
## ラズパイの設定
```
sudo raspi-config
```

で「Interfacing Options」>「Serial」でシリアル接続を有効にする。

## Macの準備
![USB－TTLシリアルコンソール](https://images-na.ssl-images-amazon.com/images/I/61paqf6ELFL._SL1024_.jpg)
[Raspberry Pi ラズベリーパイ用の USB－TTLシリアルコンソールのUSB変換COMケーブルモジュールのケーブル](https://www.amazon.co.jp/dp/B00K7YYFNM/)を用意する。
ドライバーが必要なので以下よりダウンロードする。  
[PL2303 Mac OS X Driver Download](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41) 

## 接続
| 色   | ピン               |
| :--- | :---               |
| 赤   | 接続しない         |
| 黒   | GND                |
| 白   | UARTO TX(8番ピン)  |
| 緑   | UARTO RX(10番ピン) |

Mac側のターミナルで
```
screen /dev/tty.usbserial 115200
```
