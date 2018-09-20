# Macシリアル接続できなくなった場合

## SIP
```
/dev/tty.usbserial
```
があるか確認。  
ないと接続できない。  

SIPが悪さをするらしいので、リカバリーモードでSIPをdisableにする。  
その後通常起動して
```
csrutil status
```
で
```
System Integrity Protection status: disabled.
```
をすれば多分接続できる。

## ドライバーの再インストール
```
sudo rm -rf /Library/Extensions/ProlificUsbSerial.kext
sudo rm -rf /var/db/receipts/*PL2303*.*
sudo rm -rf /var/db/receipts/*ProlificUSbSerial*.*
```
