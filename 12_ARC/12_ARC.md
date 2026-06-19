# Sowftware-Architektur

## ARC-E1: Finale Architektur

Damit man über die Architektur des Identity Entropy Engine (IEE) können wir zuerst einen Blick auf den Zustand- und Komponentendiagramm aus den früheren Aufgaben werfen:

### Zustandsdiagramm
<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/228c7866d551e07dfaa256e25ce756928a1feb6d/05_UML/Zustandsdiagramm.png" />

### Komponentendiagramm

<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/fd355558ea78e59c9fd7d1369a4d185b5235c0da/05_UML/Komponentendiagramm.png" />

Wie im Zustandsdiagramm zu sehen ist, stellt eine Schleife die Hauptfunktionalität des Programms dar. Daher handelt es sich um eine **ereignisbasierte Architektur**. Und nach einem genaueren Blick auf das Komponentendiagramm sieht man, wie die Funktionalitäten in interagierende Einheiten gruppiert sind. In diesem Projekt sind außerdem mehrere Design Patterns zu finden. Die Kopplung zwischen Engine, Datenbank und Dashboard entspricht einem N-Schichtenmodell. Die unterschiedlichen Elemente sind horizontal angelegt. Alle gehören zur Hauptebene, aber innerhalb jeder Komponente gibt es Klassen für die unterschiedlichen Funktionalitäten. Daher kann man auch sagen, dass es eine **sanfte Kopplung und gleichzeitig eine starke innere Kohäsion gibt. Diese sind kennzeichnende Prinzipien** im Projekt. Dies ist deutlich am Klassendiagramm zu erkennen:


<img width="758" height="671" alt="grafik" src="https://github.com/user-attachments/assets/cd35eba9-8d2b-4757-a731-55f1e541a886" />



Engine, Datenbank und Dashboard sind unabhängig voneinander. Daher lässt sich behaupten, dass aus dieser panoramischen Perspektive das Projekt ein **Model-View-Controller-Design** hat.  
Dieses Projekt wurde für die ESA Vibe Coding in zwei Versionen entwickelt und dabei verschieden **Frameworks** wurden benutzt. Eine Version wurde mit Gemini erstellt und greift auf die Standardpythonbibliothek und Flask zurück. Die andere Version benutzt Tkinter für die GUI, Selenium Webdriver für die Suche im Hintergrund und unittest und mutmut für die Tests.  
Mit den zwei letzten **Test-Frameworks** kann man die Qualität des Codes gewährleisten. Für die Metrics kann man sich immer auf pylint oder SonarQube stützen. Für dieses Projekt würde ich auf die lockere Kopplung achten. Diese Prinzip ist die Eckstein für die Interkation zwischen Komponenten. So ist grundsätzlich die Architektur von IEE:

<img width="988" height="351" alt="grafik" src="https://github.com/user-attachments/assets/ca73537a-4f18-4a8e-a63d-d3692221cd94" />

## ARC-E2: Architecture Communication Canvas

