# Sowftware-Architektur

## ARC-E1: Finale Architektur

Damit man über die Architektur des Identity Entropy Engine (IEE) können wir zuerst einen Blick auf den Zustand- und Komponentendiagramm aus den früheren Aufgaben:

### Zustandsdiagramm
<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/228c7866d551e07dfaa256e25ce756928a1feb6d/05_UML/Zustandsdiagramm.png" />

### Komponentendiagramm

<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/fd355558ea78e59c9fd7d1369a4d185b5235c0da/05_UML/Komponentendiagramm.png" />

Wie im Zustandsdiagramm zu sehen ist, stellt eine Schleife die Hauptfunktionalität des Programms dar. Daher handelt es sich um eine Ereigniss basierte Architektur. Aber nach einen genauren Blick auf das Komponentendiagramm scheint die Artchitektur eher einen Hybrid zu sein. Die Kopplung mit der Datenbank und der Dashboard entsprechen eher eine N-Tier Architektur. Die unterschiedliche Elemente sind horizontal Angelegt.
