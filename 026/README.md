# chromiun導入

## インストール
```
sudo apt install chromium-browser
```

## 起動
```
DISPLAY=:0 chromium-browser
```

```
DISPLAY=:0 chromium-browser --kiosk
```

## マウスカーソル非表示
```
sudo apt install unclutter
```

`/etc/xdg/lxsession/LXDE/autostart`に
```
@unclutter -idle 0.1 -root
```
