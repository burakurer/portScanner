# portScanner v1.1
Python ile yazılmış port tarama programı

## Tarama seçenekleri

- Tekli port tara
- Çoklu port tara
- En çok kullanılan portları tara

`Tekli port tara` seçeneğinde girilen tek portu tarar.

`Çoklu port tara` seçeneğinde girilen başlangıç portundan, bitiş portuna kadar olan tüm portları tarar.

`En çok kullanılan portları tara` seçeneğinde **21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 2082, 2083, 2086, 2087, 3306, 3389, 8443, 8447, 8880** portlarını tarar.

## Program ayarları
`config.timeout` zaman aşımı ayarı (varsayılan 0.9)

## Gerekli kütüphaneler

- PyFiglet (`pip3 install pyfiglet`)

<hr>

#### English
Port scanning program written in Python

## Scan options

- Scan single port
- Scan multiple ports
- Scan for most used ports

Scans for a single port entered in the `Scan for single port` option.

Scans the ports from the start port to the end port entered in the `Scan for multiple ports` option.

`Scan for most used ports` **21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 2082, 2083, 2086, 2087, 3306, 3389, 8443, 8447, 8880**.

## Program settings
`config.timeout` timeout setting (default 0.9)

## Required libraries

- PyFiglet (`pip3 install pyfiglet`)
