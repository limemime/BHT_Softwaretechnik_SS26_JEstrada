# 11 Metrics

Für diese Aufgabe habe ich das Code von der Vibe Coding Aufgabe verdente. Diese Entropy-Engine, das willkürliche Suchen im Web macht, funktioniert:

<img width="1768" height="943" alt="grafik" src="https://github.com/user-attachments/assets/2098f2b8-7a8c-47a2-87a5-4352fbdb8c60" />

## Extensions

Zuerst habe ich die benötigte Extensions in Antigravity installiert:

<img width="1030" height="889" alt="grafik" src="https://github.com/user-attachments/assets/09fa3f63-3377-464d-b602-637a6eae0198" />

## Pylint

Pylint entdeckt ein Problem in code mit der Konventionen über "trailing whitespaces":

<img width="1504" height="961" alt="grafik" src="https://github.com/user-attachments/assets/fd9665cf-2e8f-4dcd-abe7-08c10102efbc" />


Wichtiger sind die Problemme mit den Imports (webdriver.Chrome) und auch das "Faule Format":

<img width="1375" height="718" alt="grafik" src="https://github.com/user-attachments/assets/b43792ec-8dff-4459-b36e-895e2c038340" />

Damit pylint ein Note gibt, muss man es in dem Terminal ausführen. Vorher muss man abe pylint in der .venv mit pip installieren und danach: 

<img width="1153" height="679" alt="grafik" src="https://github.com/user-attachments/assets/1a569743-301f-4611-ae30-a736b974c742" />


Die Note ist 1.83/10:

<img width="1072" height="352" alt="grafik" src="https://github.com/user-attachments/assets/97c784fb-9bfc-4d2e-9451-a62c495089ad" />

Die niedriege Note ist vielleicht nur die zahlreiche Trailing Whitespaces zu verdanken. 

## SonarQube 

In Engine hat SonarQube nur zwei Fehler gefunden: 

<img width="1375" height="733" alt="grafik" src="https://github.com/user-attachments/assets/8d707405-13b2-4994-b504-a975b7e81997" />

Aber für die Note mit SonarQueb muss man es mit node installieren:

<img width="768" height="172" alt="grafik" src="https://github.com/user-attachments/assets/38a16ba0-22d2-4b15-b270-e61e8d766287" />


Eine Konfigurationsdatei kreieren:
<img width="1096" height="568" alt="grafik" src="https://github.com/user-attachments/assets/b1cfe92d-626c-45c3-9c04-11a54d4b2279" />

Der erste Versuch hat gescheitert, weil ich der Server nicht angemacht habe:

<img width="1156" height="490" alt="grafik" src="https://github.com/user-attachments/assets/18326700-e859-4342-a753-f50469258346" />

Dafür bracht man Docker oder Docker Desktop.

docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest











