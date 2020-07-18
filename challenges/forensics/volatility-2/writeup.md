# Writeup

Le 2è flag se trouve dans le clipboard, donc on utilise le module `clipboard` de volatility

```shell
$ volatility clipboard -f /path/to/volatile_mem.dmp

Volatility Foundation Volatility Framework 2.6.1
Session    WindowStation Format                 Handle Object     Data
---------- ------------- ------------------ ---------- ---------- --------------------------------------------------
		 0 WinSta0       CF_UNICODETEXT      0x96f00eb 0xe24ea678 SrayBRptOqTT3wOhR7tKDA9546ob5VIh+Hhn3GnO
[...]
```

`SrayBRptOqTT3wOhR7tKDA9546ob5VIh+Hhn3GnO`
