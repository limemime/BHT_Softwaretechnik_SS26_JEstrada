# Buildmanagement mit ANT
## 1
Der erste Schritt ist ein Projekt zu erstellt und vergessen ein build.xml zu erstellen, daher kriege ich diese Fehlermeldung:
<img width="1346" height="295" alt="grafik" src="https://github.com/user-attachments/assets/f4ba28da-1ed8-4c26-afc0-0eb55ee8b5d3" />
## 2
Ant war nicht installiert:
<img width="1344" height="460" alt="grafik" src="https://github.com/user-attachments/assets/49f2d0a2-e704-4649-a9d9-95426a5bd7fd" />

<img width="1301" height="248" alt="grafik" src="https://github.com/user-attachments/assets/a477fced-86c4-4524-82d8-bd4f0400e6e0" />

## 3
Aber die Probleme bestehen, weil mir nicht klar war, dass die Targets im build.xml und nicht in Build Steps seins sollten:

<img width="1343" height="595" alt="grafik" src="https://github.com/user-attachments/assets/ba18b467-c90d-4e99-853f-d19f6d678955" />

## 4

Nach mehrere Problemen habe ich endlich Jenkins verstanden:

<img width="1364" height="548" alt="grafik" src="https://github.com/user-attachments/assets/7ffddf28-f3e3-4dc7-ad6b-98d57348bd5a" />

## 5

Hier habe ich herausgefunden, dass die Dependencies immer zuerst ausgeführt werden. Deshalb sieht man sie doppelt. I habe LEDAT und dann CLEAN in the Vuilding Steps hinzugefügt:

<img width="739" height="529" alt="grafik" src="https://github.com/user-attachments/assets/765c4920-d1f9-4ba9-aebd-8d1ad5f35bc5" />

## 6

Ich habe ein COMPILE und JAR implementiert, aber wenn ich ein JavaRUN ausführe, erhalte ich eine Fehlermeldung, weil ich die Datei schon kreiert habeb, deshalb brauche ich noch ein clean:
<img width="1302" height="421" alt="grafik" src="https://github.com/user-attachments/assets/b801e448-c2ba-401e-9a4b-319cee181cb4" />


<img width="1108" height="660" alt="grafik" src="https://github.com/user-attachments/assets/27b64c58-3103-4718-b111-55a06f21f749" />

## 7

Noch ein Problem, weil die Pfad zu .class fehlt:

<img width="931" height="162" alt="grafik" src="https://github.com/user-attachments/assets/68793d64-462e-4881-acf8-2243d6437e53" />

## 8

Nach ein paar Probleme mit der Pfaden hat das Java programm funktioniert. Die Entsprechende Datei sind im Unterordner.
Hier füge ich nur ein paar Screenshot hinzu.

<img width="1276" height="625" alt="grafik" src="https://github.com/user-attachments/assets/8b5f4b9a-66d0-45dd-8f88-74bfe4078833" />

<img width="1174" height="771" alt="grafik" src="https://github.com/user-attachments/assets/9c817e4a-03c3-404d-b1ae-f3041f830477" />

## 9

Java docs:

<img width="1327" height="640" alt="grafik" src="https://github.com/user-attachments/assets/49f3c074-2f41-4015-86e6-ebd097b6b112" />














