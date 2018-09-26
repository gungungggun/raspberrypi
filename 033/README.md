# USB扇風機のON/OFF

`hub-ctrl`を使う。  
[hun-ctrlのリポジトリ](https://github.com/codazoda/hub-ctrl.c)からソースをクローン
```
gcc -o hub-ctrl hub-ctrl.c -lusb
```
でコンパイルすれば`hub-ctrl`が使える。
```
hub-ctrl -v
```
で情報が表示されればOK。  

2番ポートにUSB扇風機を繋いで、
```
sudo hub-ctrl -h 0 -P 2 -p 0
```
を実行すると扇風機が止まる。
```
sudo hub-ctrl -h 0 -P 2 -p 1
```
で再度動く
