# All die Aufgaben sind auch hier in Miro zu finden: https://miro.com/app/board/uXjVHWe5lzc=/?share_link_id=15807961905
## Einsendeaufgabe OOD-E1: EVENT STORMING
 <img width="1370" height="909" alt="grafik" src="https://github.com/user-attachments/assets/165a68f7-78a6-44da-b301-8baac6b49a25" />

Hier wurden ein paar mehr Ereignisse hinzugefügt.

<img width="1870" height="869" alt="grafik" src="https://github.com/user-attachments/assets/d115e603-e10b-484a-b548-2edb37bc5e76" />
<img width="1891" height="964" alt="grafik" src="https://github.com/user-attachments/assets/b0e1a8a3-2c32-40d6-bf7c-ecf21458db10" />


 
 
## OOD-E2: CORE DOMAIN CHART
Hauptfunktion oder „Core“ dieser Anwendung ist die Such-Engine. Diese Funktion benötigt eine angepasste Annäherung an die Metrics und wird durch eine ständige Verbesserung ihres automatisierten Verhaltens zugespitzt. Man möchte vermeiden, dass die Engine sofort als Bot erkannt und somit der Zugang gesperrt wird. Während die letzten zwei Punkte als „supporting“ gekennzeichnet werden können, sind die nächsten „generic“: der Datenbank für die Speicherung von gemachten Suchen und Ergebnissen braucht keine speziellen Funktionen. Das Dashboard und die Bezahlungsmethode können sich an die Standards anlehnen. Die Persuasion-Gruppe mit Fördermittelerwerb und Marketing sind auch generic. 
<img width="1098" height="1057" alt="grafik" src="https://github.com/user-attachments/assets/6776434d-794c-478c-b772-8132a42345a4" />

 
## OOD-E3: DOMAIN MAPPINGS = BEZIEHUNGEN! 
Dieser Architektur liegt eine Schleife zugrunde, die sich nur in einer Richtung bewegt. Der kritische Knoten ist das Entropie-Engine. Diese erhält wichtige Konfigurationseinstellungen von der Non-deterministic-behavior-Gruppe sowie die Liste mit akzeptierten Suchbegriffen, aber die werden an den Kontext der Engine durch eine „Anticorruption Layer“ angepasst, damit die Funktionalität gewährleistet wird. Obwohl sie nicht der Anwendungskern ist, spielt DevSecOps eine zentrale Rolle, denn sie bestimmt Sicherheitsmaßnahmen für alle Komponenten, die sich als „conformist“ verhalten müssen oder, wie im Fall der Engine, als gleichberechtigte Zusammenarbeit. Diese Partnerschaft zielt darauf, eine angepasste Funktionalität aufrechtzuerhalten. Das ist auch der Fall bei der Beziehung zwischen der Datenbankbereitstellung und den Anforderungen der Metrics-Gruppe sowie bei dem Dashboard- und Marketing-Team. Eine wichtige Schnittstelle beschäftigt sich mit den möglichen Blockaden für automatisiertes Verhalten und fokussiert eher auf die Forschung und Entwicklung des algorithmischen Kerns der Anwendung. Der Gruppe mit den wenigsten Privilegien ist die GUI/Dashboard-Gruppe, die sich Daten visualisiert und Richtlinien von DevSecOps bekommt, so dass sie einen schmalen Spielraum als „conformist“ hat. 	
<img width="1514" height="1014" alt="grafik" src="https://github.com/user-attachments/assets/5688a978-37fc-4100-9a68-839377039864" />

## OOD-E4: Bounded Context Canvas
<img width="1069" height="595" alt="grafik" src="https://github.com/user-attachments/assets/15b9c2dd-d394-4c53-a197-31f8fb756b9b" />


 
