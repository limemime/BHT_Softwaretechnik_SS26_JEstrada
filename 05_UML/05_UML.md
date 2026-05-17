
# TEIL A  

## Anwendungsfalldiagramm
<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/user-attachments/assets/67afe027-dc35-4a57-98e8-86025c18810c" />

## Paketdiagramm
<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/1590f891c54f77961ba17e9a6e4a9bf346040167/05_UML/Packetdiagramm.png" />

## Zustandsdiagramm
<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/228c7866d551e07dfaa256e25ce756928a1feb6d/05_UML/Zustandsdiagramm.png" />

## Komponentendiagramm

<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/fd355558ea78e59c9fd7d1369a4d185b5235c0da/05_UML/Komponentendiagramm.png" />

## Klassendiagramm

<img width="425" height="441" alt="Use_Case_Diagramm_IEE" src="https://github.com/limemime/BHT_Softwaretechnik_SS26_JEstrada/blob/c4839b8da612c3f97ba3db25fb1731e5bbcea173/05_UML/Klassendiagramm.png" />

# TEIL B



Ich habe zwei Diagramme mit KI generiert. Zuert habe ich Lumo nach eine Paketdiagrammestruktur meiner Projekt gefragt. Der Kontext stammt aus den vorherigen ESAs. Danach habe ich die Ergebnisse i eraser.io eingegeben

## Erstes Beispiel
: Make A package diagramm with this: packageDiagram
    package "EntropySearchEngine" {
        package "Core" {
            package "DictionaryManager" {
                class "WordListLoader"
                class "TermSelector"
                class "ContextGenerator"
            }
            package "EntropyEngine" {
                class "RandomizationStrategy"
                class "RhythmController"
                class "SearchScheduler"
                interface "ISearchExecutor"
            }
        }

        package "Automation" {
            package "BrowserAdapter" {
                class "SeleniumWrapper"
                class "PlaywrightWrapper"
                class "HeadlessManager"
            }
            package "AntiDetection" {
                class "FingerprintSpoofing"
                class "BehavioralMimicry"
                class "IPRotationHandler"
            }
        }

        package "Presentation" {
            package "Dashboard" {
                class "MetricsView"
                class "ControlPanel"
                class "LogViewer"
            }
            package "Settings" {
                class "RhythmConfig"
                class "FrequencySlider"
                class "ProfileManager"
            }
        }

        package "Infrastructure" {
            package "Security" {
                class "DDoSProtection"
                class "RateLimiter"
                class "SafeGuard"
            }
            package "Persistence" {
                class "LocalConfigStore"
                class "SearchHistoryLog"
            }
        }
    } 


<img width="1899" height="2181" alt="diagram-export-17 5 2026-22_16_44" src="https://github.com/user-attachments/assets/43f4076c-0d66-4ae6-b63a-c88170606738" />

## Zweites Beispile
Hier habe ich auch Proton benutzt. EIn Beispiel von klassen Diagramme erstellen lassen und danach, habe ich die Text in mermaid eingegeben und auch nach Kardinalitäten und Aggregationen bzw. Kompositionen gefragt. Hier ist der link https://mermaid.ai/d/c4ab199f-e184-4af8-ab5a-df7d6d62e438


<img width="958" height="871" alt="grafik" src="https://github.com/user-attachments/assets/cd35eba9-8d2b-4757-a731-55f1e541a886" />


Mermaid hat diese Code erstellt 

classDiagram
    %%{init: {"layout":"elk"}}%%

    class User {
        +String userId
        +UserProfile preferences
        +startSession()
        +stopSession()
        +configureRhythm(minInterval:int, maxInterval:int)
    }

    class Dashboard {
        +Boolean isActive
        +Integer totalSearches
        +String currentStatus
        +List~SearchLog~ logEntries
        +updateMetrics()
        +displayAlert(message:String)
        +renderGraph(data:List~Integer~)
    }

    class EntropyEngine {
        +SearchScheduler scheduler
        +DictionaryManager dictionary
        +BrowserWrapper browser
        +SafetyGuard safetyGuard
        +Boolean isRunning
        +executeCycle()
        +generateNextSearchQuery()
        +triggerSearch(query:String)
        +pause(duration:int)
        +terminate()
    }

    class RhythmGenerator {
        +Integer minDelayMs
        +Integer maxDelayMs
        +Double jitterFactor
        +DateTime lastExecutionTime
        +calculateNextDelay()
        +isHumanLikePattern()
        +reset()
    }

    class DictionaryManager {
        +List~String~ wordList
        +String categoryFilter
        +Integer currentIndex
        +loadFromFile(path:String)
        +getRandomTerm()
        +combineTerms(count:int)
        +validateTerm(term:String)
    }

    class BrowserWrapper {
        +WebDriver driver
        +String userAgent
        +Point viewportSize
        +Boolean isHeadless
        +initialize()
        +navigateTo(url:String)
        +performSearch(query:String)
        +simulateHumanMovement()
        +close()
    }

    class SafetyGuard {
        +Integer maxRequestsPerMinute
        +Integer currentRequestCount
        +DateTime windowStartTime
        +List~String~ blocklist
        +checkLimit()
        +recordRequest()
        +detectAnomaly(errorCode:String)
        +emergencyStop()
    }

    class SearchLog {
        +DateTime timestamp
        +String query
        +Integer durationMs
        +String status
        +Integer rhythmDelay
        +toString()
        +toJSON()
        +isSuccessful()
    }

    %% Relationships (composition and aggregation with cardinality)
    User "1" --> "1" Dashboard : monitors >
    User "1" o-- "1" EntropyEngine : controls >

    EntropyEngine "1" *-- "1" RhythmGenerator : uses >
    EntropyEngine "1" *-- "1" DictionaryManager : uses >
    EntropyEngine "1" *-- "1" BrowserWrapper : controls >
    EntropyEngine "1" *-- "1" SafetyGuard : guards >

    Dashboard "1" *-- "0..*" SearchLog : records >

    DictionaryManager "1" --> "1..*" SearchLog : contributes terms to >




