# portScanner v1
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

- Sys
- Socket
- PyFiglet
