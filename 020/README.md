## インストール
```
sudo apt-get install motion
```

## 設定ファイル
`/etc/motion/motion.conf`

```
webcontrol_localhost on
```
↓
```
webcontrol_localhost off
```

```
stream_localhost on
```
↓
```
stream_localhost off
```

## 起動
```
sudo motion -n
```

## 停止
```
sudo service motion stop
```
