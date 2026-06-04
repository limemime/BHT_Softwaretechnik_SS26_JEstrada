# Buildmanagement mit ANT

## 1 Der erste Schritt ist ein Projekt zu erstellt, aber ich habe vergessen, ein build.xml zu erstellen.

Daher kriege ich diese Fehlermeldung:

<img width="1346" height="295" alt="grafik" src="https://github.com/user-attachments/assets/f4ba28da-1ed8-4c26-afc0-0eb55ee8b5d3" />

## 2 Ant war nicht für eine automatische Installation konfiguriert:

<img width="1344" height="460" alt="grafik" src="https://github.com/user-attachments/assets/49f2d0a2-e704-4649-a9d9-95426a5bd7fd" />

<img width="684" height="607" alt="grafik" src="https://github.com/user-attachments/assets/3b038229-d094-46e0-ae4e-c1fc1afafc59" />

## 3 Aber die Probleme bestehen, weil mir nicht klar war, dass die Targets im build.xml und nicht in Build Steps seins sollten:

<img width="1343" height="595" alt="grafik" src="https://github.com/user-attachments/assets/ba18b467-c90d-4e99-853f-d19f6d678955" />

## 4 Nach mehreren Problemen habe ich endlich Jenkins verstanden:

<img width="1364" height="548" alt="grafik" src="https://github.com/user-attachments/assets/7ffddf28-f3e3-4dc7-ad6b-98d57348bd5a" />

## 5 Ich habe LEDAT (leere Datei) und dann CLEAN hinzugefügt:

<img width="739" height="529" alt="grafik" src="https://github.com/user-attachments/assets/765c4920-d1f9-4ba9-aebd-8d1ad5f35bc5" />

## 6 LEDAT wurde zwei Mal ausgeführt, weil es eine Dependency von Clean war.

<img width="1467" height="483" alt="grafik" src="https://github.com/user-attachments/assets/b72f6e2c-ac72-4d26-95ff-4926822d6418" />

## 7 COMPILE und JAR sind implementiert, aber es gibt ein Fehlermeldung mit JavaRUN: Es fehlt noch ein CLEAN

<img width="1302" height="421" alt="grafik" src="https://github.com/user-attachments/assets/b801e448-c2ba-401e-9a4b-319cee181cb4" />

## 8 Noch ein Problem: die Pfad von .class fehlte und Classname war nkcht richtig.

<img width="931" height="162" alt="grafik" src="https://github.com/user-attachments/assets/68793d64-462e-4881-acf8-2243d6437e53" />

## 9 Endlich funktioniert das Java-Programm. Die Entsprechende Datei sind im Unterordner.

Hier füge ich nur ein paar Screenshot hinzu.

<img width="1276" height="625" alt="grafik" src="https://github.com/user-attachments/assets/8b5f4b9a-66d0-45dd-8f88-74bfe4078833" />

<img width="1174" height="771" alt="grafik" src="https://github.com/user-attachments/assets/9c817e4a-03c3-404d-b1ae-f3041f830477" />

## 9 Java docs:

<img width="1327" height="640" alt="grafik" src="https://github.com/user-attachments/assets/49f3c074-2f41-4015-86e6-ebd097b6b112" />

# Buildmanagement mit GRADLE

Kurzeres Beispiel

## 1 Hello World hat funktioniert:

<img width="939" height="217" alt="grafik" src="https://github.com/user-attachments/assets/bc9384a0-3a55-4335-a282-c22cb5c32b2c" />

<img width="1423" height="655" alt="grafik" src="https://github.com/user-attachments/assets/192a2985-8b3d-444d-a217-dc028fe5baf1" />

## 2 Mit der Plugins kann man die task asuführen, ohne entsprechendes Code im build.gradle zu schreiben:

<img width="549" height="346" alt="grafik" src="https://github.com/user-attachments/assets/97ef965c-2481-4e80-8d4d-69a60d5604e4" />

<img width="1330" height="541" alt="grafik" src="https://github.com/user-attachments/assets/34bb97d8-2ba7-4cc1-92a7-bfc980db616c" />

## 3 Pkugins verain fachen das ganze Prozesss:

<img width="412" height="442" alt="grafik" src="https://github.com/user-attachments/assets/e1c9127c-4aeb-4b54-b599-b1e4ff99876c" />

<img width="454" height="414" alt="grafik" src="https://github.com/user-attachments/assets/1edf7d21-99d4-4a7c-9388-cb393f436117" />

## 4 Eine kleine Dependency

<img width="489" height="226" alt="grafik" src="https://github.com/user-attachments/assets/9b6942fc-86e4-422d-9cfd-4d56c9e57f52" />

<img width="487" height="487" alt="grafik" src="https://github.com/user-attachments/assets/a71dd608-3b43-4266-919f-0f1ea928b537" />

## 5 Am ende ein kleiner Versuch mit groovy

<img width="1306" height="303" alt="grafik" src="https://github.com/user-attachments/assets/65062972-e217-4a1a-8bf1-92abb4f1ad7d" />

## 6 Insgesamt machen die Plugins die Arbeit mit gradle sehr einfach. 



















