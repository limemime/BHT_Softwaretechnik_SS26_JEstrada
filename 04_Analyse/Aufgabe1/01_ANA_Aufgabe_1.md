**04 ESA-Analyse**

**Aufgabe 1)** 

 # 1.	Ist-Analyse

  ##  1.1.	Geschäftsidee
Hauptidee dieses Projekts ist, ein Programm zu entwickeln, das das Recht auf eine private, digitale Identität gewährleistet, indem das Profiling durch Beobachtung des Webs mit Suchmaschinen erschwert wird. Dies kann gelingen durch die Obfuscation digitaler Persona, d. h. durch ein automatisiertes Poisoning der von einem Anwender verursachten Daten.

  ##  1.2.	Unternehmensziele
Dieses Projekt stellt ein erster Schritt für die Gründung einer Einrichtung sein, die Tools für Datenschutz entwickelt und forscht. Da es sowohl öffentliche als private Interesse an das Thema gibt, sollte sich diese Einrichtung zum einen als ein privates Unternehmen entwickeln. Zum anderen könnte die öffentliche Unterstützung auch helfen, diese Einrichtung zu gründen.  

## 1.3.	Ressourcenplanung
Da es sich um eine kleine App und einen Prototyp handelt, gibt es zurzeit keine Kosten. Es handelt sich um eine Selbstentwicklung, die nur Zeit in Anspruch nimmt, weswegen ein Budget noch nicht erstellt wurde. Trotzdem kann man Finanzierung als Seed Capital durch Akzelerator- oder Inkubator-Programme erwerben. In Betracht kommen Horizon-Programme der EU und der European Investment Fund. Da der Staat keinen aktiven Schutz der digitalen Rechte ihrer BürgerInnen anbietet, gibt es eine Marktnische zu erobern und gleichzeitig ein öffentliches Interesse, die auch zu politischer und finanzieller Unterstützung führen kann.   

   ## 1.4.	Stakeholders
Geschäftsführer: Soll öffentliche und private Finanzierung erwerben und sich in einer Marktnische positionieren.  
Endkunden: Menschen mit dem Wunsch, sich aktiv vor dem digitalen Meinungsengineering zu schützen.  
Hauptentwickler: Soll die technischen Anforderungen des Projekts beherrschen, ein dazu passendes Entwicklungsteam bilden und ein machbares Design entwerfen.  
Projektleiter: Hilft dabei, das Projekt zu organisieren, dokumentieren, Meilensteine und Fristen zu setzen. Er übernimmt die Aufgabe, eine reibungslose Kommunikation zwischen Entwicklerteam und Geschäftsführer sicherzustellen.  
Staatliche Interessen: Da man sich mit einem strittigen Thema beschäftigt, ist zu erwarten, dass politische Akteure sich an diesem Projekt direkt oder indirekt beteiligen.  
Dieser Zwischenraum zwischen öffentlichen und privaten Interessen kann zu Problemen zwischen Stakeholdern führen.

   ## 1.5.	Marktanalyse
Der Markt bietet zurzeit passiven Schutz vor der Verfolgung im Internet. Es gibt Browsererweiterungen gegen Tracking-Cookies, gegen Fingerprinting, gegen Werbung. Nichtdestotrotz fehlt es an aktiven Maßnahmen. Daher wäre es einfach, dieses Produkt im Markt zu positionieren.

#  2.	Soll-Konzept
##    2.1.	Technischer Prototyp
Der Prototyp sollte randomisierte Suche von Vorschlägen aus Wörterbuch in randomisiertem Rhythmus ausführen. Diese Hauptfunktion wird von einer „Entropie Engine“ durchgeführt. Weitere Kernfunktionen sind eine Implementierung von Selenium oder Playwright, damit die Engine im Hintergrund läuft, und man sollte auswählen können, wie oft die Suchen durchgeführt werden.

  ##  2.2.	GUI-Prototyp
Die GUI sollte ein Dashboard für die Bedienung und ggf. Metriken von den durchgeführten Suchen haben. Man sollte auch mit einem Knopf das Tempo der Suchen anpassen können. 

## 2.3.	Dokumentierung
Das Projekt wird in einer README.md erklärt. Jeder Schritt in der Implementation wird in dieser Datei dokumentiert und erklärt. Da es sich um eine modularisierte Entwicklung handelt, werden die Fortschritte in einer Art Gantt-Chart verfolgt und aktualisiert.

  ##  2.4.	Konzept der Qualitätssicherung und Sicherheit
Die Qualität wird durch die Setzung von Meilensteinen sowie Code-Reviews gewährleistet. Für die Sicherheit gibt es wesentliche Voraussetzungen. Die Engine sollte nicht für DDoS-Angriffe instrumentalisiert werden oder übernommen werden.

   ## 2.5.	Legal Implikationen
Diese Anwendung kann gegen den Fair-Use-Klausel der Suchmaschinen stoßen. Deswegen sollte man untersuchen, in welchem Maß diese Entropie Engine benutzt werden darf. Dürfen die Unternehmen Crawler im Web benutzen, aber man darf nicht ähnliche automatisierte Verfahren benutzen?

 ##   2.6.	Glossar
Entropie Engine: Die Kernfunktion dieser Anwendung. Sie sucht nach beliebigen Themen  
Rhythmus: Automatisierung ist nicht gleich deterministisches Verhalten.
