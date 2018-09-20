# USBマイク

## 接続確認
```
lsusb
```

## オーディオモジュール優先順位確認
マイクを最優先にする必要があるので`cat /proc/asound/modules`を実行して優先順位を確認する。  
```
cat /proc/asound/modules
  0 snd_bcm2835
  1 snd_usb_audio
```
`snd_usb_audio`を優先にしないと行けないので、`/etc/modprobe.d/alsa-base.conf`を書き換える。  
このファイルがない場合は新規で作成する。  
ファイルの中身は以下
```
options snd slots=snd_usb_audiosnd_bcm2835
options snd_usb_audio index=0
options snd_bcm2835 index=1
```
これでもう一度`cat /proc/asound/modules`を実行して優先順位を確認すると
```
cat /proc/asound/modules
  0 snd_usb_audio
  1 snd_bcm2835
```
となっている。

## サウンドカードナンバーとデバイスナンバー
サウンドカードナンバーとデバイスナンバーは録音や再生をしたいときに必要。  
```
arecord -l
```
を実行すると以下のようなものが返ってくるので、ここの`card`と`device`の後の数値を確認。  
```
**** List of CAPTURE Hardware Devices ****
card 0: Device [USB PnP Audio Device] device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

## 録音
以下のコマンドを実行
```
arecord -D plughw:00 -r 16000 -f cd sample.wav
```

`-D`はデバイスを指定するオプション。0:0の場合、`~/.asoundrc`の設定ファイルにデフォルト設定していなければ、特に指定しなくても大丈夫。  
`-r`はサンプリングレート。  
`-f`はフォーマットを指定するオプションで`cd`の場合「16 ビット、リトルエンディアン、44100、ステレオ」となる。  
実行すると録音が開始され、「ctrl+c」で録音終了となる。  

## 再生
上記の例で録音すると`sample.wav`が出来上がる。  
再生はラズパイ上で行う場合、`aplay`コマンドを利用する。  
ラズパイ3にはイヤホンジャックとHDMI、2つで音声出力できるので再生時にどちらを使うか指定して上げる必要がある。  

```
aplay -l
```
を実行すると以下のように出力される。  
```
**** List of PLAYBACK Hardware Devices ****
card 1: ALSA [bcm2835 ALSA] device 0: bcm2835 ALSA [bcm2835 ALSA]
  Subdevices: 7/7
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
card 1: ALSA [bcm2835 ALSA] device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
イヤホンで確認したい場合、カードナンバーが1、デバイスナンバーは0となるので、  
```
aplay -Dhw:10 samplet.wav
```
録音した内容が聞き取れる。  
