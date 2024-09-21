import streamlit as st

st.set_page_config(
    page_title="Green Rider",
    page_icon="💚",
)

# Session management
def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
def load_value(key):
    st.session_state["_"+key] = st.session_state[key]

# Add a logo to the sidebar
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.success("Ich bin ein Success panel.")

# Checkbox group in the sidebar for enabling/disabling sections
st.sidebar.header("Enable/Disable Sections")
is_allgemein = st.sidebar.checkbox("Allgemein", value=True)
is_mobilitaet = st.sidebar.checkbox("Mobilität", value=True)
is_energieeffizienz = st.sidebar.checkbox("Energieeffizienz", value=True)
is_abfall = st.sidebar.checkbox("Abfall", value=True)
is_catering = st.sidebar.checkbox("Catering / Verpflegung", value=True)
is_unterkunft = st.sidebar.checkbox("Lokale Unterkünfte und Hotels", value=True)
is_produktion = st.sidebar.checkbox("Produktion", value=True)
is_kommunikation = st.sidebar.checkbox("Kommunikation & Team", value=True)
is_kompensation = st.sidebar.checkbox("CO2-Emissionsmessungen und Kompensation", value=True)
is_barrierefreiheit = st.sidebar.checkbox("Barrierefreiheit, soziale Gerechtigkeit, Inklusion", value=True)
is_awareness = st.sidebar.checkbox("Awareness", value=True)

# Title for the main view
st.title("Green Rider")
st.subheader("# Generator 👋")

# Conditionally display sections based on checkbox state
if is_allgemein:
    st.markdown(
        """
        ## Allgemein  
        Wir stehen alle in der Verantwortung, unseren Teil zum Klimaschutz beizutragen, auch auf Tour oder unterwegs im Festivalsommer. Um unsere Konzerte nachhaltiger zu gestalten, ist es wichtig, dass gewisse Vorsätze eingehalten und beachtet werden. Uns ist natürlich bewusst, dass nicht immer alle Punkte umgesetzt werden können – wir würden uns aber freuen, wenn wir in Kooperation mit euch so viele Punkte wie möglich umsetzen können. Da ihr vor Ort alles im Blick habt und einen Großteil der Ressourcen für die Produktion bezieht, brauchen wir dafür eure Unterstützung! Falls ihr dazu Fragen haben solltet, meldet euch sehr gerne bei *Kontaktperson*.

        Generell wollen wir uns folgende Fragen in genau dieser Priorität in allen Bereichen stellen:  
        1. Wo können wir verzichten?  
        2. Wo können wir einsparen?  
        3. Wo müssen wir kompensieren?
        """
    )

if is_mobilitaet:
    st.markdown(
        """
        ## Mobilität  
        Die Anreise der Besucher\*innen hat erfahrungsgemäß den größten Impact bei einer Veranstaltung. Um eine umweltfreundliche Anreise des Publikums zu ermöglichen, hilft es, wenn…

        - die Tickets die kostenlose Nutzung öffentlicher Verkehrsmittel enthalten  
        - Veranstaltungszeiten (Beginn/Ende) so gelegt werden, dass den Besuchenden eine problemlose An- und Abreise mit dem öffentlichen Verkehr (Bahn, ÖPNV) ermöglicht werden kann  
        - Besuchende über umweltschonende Anreisemöglichkeiten sensibilisiert werden – via Rad, Bus oder Zug oder im Fall des Autos mit einer Vollbelegung, z.B. durch Fahrgemeinschaften (via Website, Facebook-Veranstaltung, etc.)  
        - Besuchende ihre Fahrräder sicher abstellen können  
        - es explizite Hinweise dazu auf den Tickets gibt: Anreise und Wegbeschreibungen, Hinweise auf Fahrplanauskünfte der Bahn und des ÖPNV, Verweis auf den „UmweltMobilCheck“ der Deutschen Bahn ([UmweltMobilCheck](https://www.bahn.de/umweltmobilcheck)).

        Außerdem erreichen wir umweltfreundlichere Mobilität, indem folgende Punkte beachtet werden:
        - „kurze Wege“, z.B. beim Catering, Künstler\*innen etc.  
        - Effizienz und Auslastung sowie nachhaltige Transportoptionen wie z.B. umweltfreundliche Taxidienste, andernfalls kraftstoffsparende und/oder Hybridfahrzeuge.
        """
    )

if is_energieeffizienz:
    st.markdown(
    """
    ## Energieeffizienz  
    Falls ihr schon regenerativen Strom bezieht, super gut! Falls ihr dies noch nicht tut, Ökostrom ist eine einfache und sehr effiziente Möglichkeit, um die Veranstaltung klimafreundlicher zu gestalten. In vielen Fällen kann beim Anbieterwechsel sogar noch Geld gespart werden ([changeyourstrom.net](https://changeyourstrom.net), [Grüner Strom Label](https://www.gruenerstromlabel.de); Übersicht von Ökostrom anbietenden Unternehmen in Deutschland).

    - Im besten Fall wird nur regenerativer Strom ("Ökostrom") bezogen, um die Nutzung fossiler Energieressourcen nicht zu fördern.  
    - Das Licht in den Umkleideräumen und die Klimaanlage/Heizung sollten erst kurz vor der Ankunft der Band/Künstler\*innen eingeschaltet werden.  
    - Alle Kühlschränke, Wasserkocher, Toaster, Lampen usw. in den Umkleidekabinen sollten möglichst energieeffizient sein (kauft aber bitte nichts Neues nur für einen Anlass – denkt einfach an den nächsten Ersatz).  
    - Wird für eine effizientere Energienutzung auf LED-Beleuchtung geachtet?    
    """
    )

if is_abfall:
    st.markdown(
    """
    ## Abfall  
    Viele Einweg-Kunststoffe verschmutzen unsere Ozeane. Ihre Produktion verschlingt beträchtliche Mengen an Öl und Wasser und verursacht Konflikte, Ressourcenverknappung und Treibhausgase. Lasst uns den Einmalverbrauch von Plastik stoppen.

    - Sowohl Backstage als auch am FOH: Bitte stellt ausreichend und eindeutig farblich gekennzeichnete Behälter für eine einfache Mülltrennung, auch für Lebensmittelabfälle, zur Verfügung.  
    - Bitte minimiert Verpackungsabfälle und überflüssige Einweg-Werbegeschenke von Sponsoren, Flyering o.ä.  
    - Verwendet Pfandsysteme für das Publikum.  
    - Bitte vermeidet unnötige Drucke und verwendet zertifiziertes, ethisch einwandfreies oder recyceltes Papier, dies gilt auch für Toilettenpapiere, Servietten, Tickets oder Zugangsausweise.  
    - Bitte stellt in allen Raucherbereichen Mülleimer und/oder Aschenbecher auf.  
    - An der Abendkasse könnt ihr Stempel (biologisch abbaubare Farben) statt Plastikbänder/Karten nutzen.
    """
    )

if is_catering:
    st.markdown(
    """
    ## Catering / Verpflegung  
    Fleisch- und Milchproduktion tragen elementar zu globalen CO2-Emissionen bei. Nach wie vor basieren sie oft auf unmenschlichen Praktiken. Eine vegane oder vegetarische Ernährung verbraucht viel weniger Wasser, Land und Öl und produziert weniger Treibhausgase.

    - Lebensmittel und Getränke sind bestenfalls vegan, biologisch, saisonal, lokal und frei von Palmöl.  
    - Bitte achtet auf fair gehandelte Produkte (auch bei Tee, Kaffee, Zucker oder Schokolade) und das entsprechende Siegel.  
    - Bitte verwendet keine Produkte von ethisch bedenklichen Firmen (Nestlé, Danone, Mars, Coca Cola etc.) und greift dafür auf faire Firmen mit Zertifikaten wie [UTZ Certified](https://utz.org), [Rainforest Alliance Certified](https://www.rainforest-alliance.org), [Euroblatt](https://de.wikipedia.org/wiki/Euro-Blatt), [Fairtrade](https://www.fairtrade-deutschland.de/was-ist-fairtrade/siegel). Umwelt- und Biosiegel, sowie Saisonkalender können zur Referenz genutzt werden.  
    - Bitte stellt nur Lebensmittel und verderbliche Getränke in der gewünschten Menge bereit und trefft Vorkehrungen, um überschüssige Lebensmittel zu sammeln, umzuverteilen oder zu spenden.  
    - Lebensmittel sollten zudem möglichst wenig Einwegverpackungen enthalten.  
    - Achtet bitte auf umweltfreundliche Produkte und gebt diesen den Vorzug.  
    - Bitte stellt uns wiederverwendbares/abwaschbares Geschirr zur Verfügung.  
    - Bitte sorgt dafür, dass allen jederzeit trinkbares Leitungswasser (oder Zapfstellen bzw. Wasserspender) zum Nachfüllen zur Verfügung steht. Wir bringen unsere eigenen wiederbefüllbaren Wasserflaschen mit.
    """
    )

if is_unterkunft:
    st.markdown(
    """
    ## Lokale Unterkünfte und Hotels  
    - Bitte achtet auf kurze Wege zwischen Veranstaltungsort und Unterbringung.  
    - Bitte favorisiert Unterkünfte mit einer geringen Umweltbelastung oder Umweltzertifikat (z.B. dem [Green-Key-Umweltzeichen](https://www.greenkey.global/) oder dem [EU-Umweltzeichen für touristische Unterkünfte](https://ec.europa.eu/environment/ecolabel/)) wenn möglich.  
    - Hier findet ihr ökologische(re) Unterkünfte.
    """
    )

if is_produktion:
    st.markdown(
    """
    ## Produktion  
    - Gibt es eine detaillierte Liste vorhandener Backline/Geräte/Instrumente und verfügbarem In-House-Equipment, damit nichts transportiert wird, was nicht unbedingt notwendig ist oder sogar via Zug angereist werden kann?  
    - Gibt es Green-Ticketing-Partner\*innen zur Kompensation der Anreise?  
    - Besteht die Möglichkeit, ein "grünes Ticket" einzuführen? Die zusätzlichen Kosten gehen zugunsten einer vom Artist gewählten Umweltinitiative.  
    - Berücksichtigt ihr bei allen Kaufentscheidungen die ethischen und ökologischen Folgen, kontrolliert ihr die ethischen Quellen neuer Materialien oder wird gebraucht erworben, recycled oder ausgeliehen?  
    - Wird auf die Qualität und Lebensdauer von Produkten geachtet, um Mehrfachkäufe zu vermeiden?  
    - Wird auf einen umweltfreundlichen Druck für unvermeidliche Flyer, Poster, Werbung geachtet? Bitte verwendet z.B. ausschließlich zertifiziertes, ethisch einwandfreies oder recyceltes Papier und biobasierte Tinte.
    """
    )


if is_kommunikation:
    st.markdown(
    """
    ## Kommunikation & Team  
    Wir haben als Musikbranche eine enorm große Reichweite – damit steigt unsere Verantwortung in der Kommunikation.

    - Wird regelmäßig über die Verantwortung der eigenen Reichweite reflektiert?  
    - Wird die Reichweite genutzt, um auf Klimagerechtigkeit aufmerksam zu machen?  
    - Stimmen die vermittelten Werte der eingeladenen Musiker\*innen und der Songtexte mit einer sozialen und nachhaltigen Gesellschaft überein?  
    - Wird für eine transparente, nachhaltige Kommunikation und Informationsstrategie gegenüber allen Gewerken sowie dem Publikum gesorgt? Z.B. über die Nachhaltigkeitsmaßnahmen (z.B. Abfalltrennprozesse bei Veranstaltungen), um die Effektivität zu maximieren und zu motivieren, sich für die Thematik ebenfalls zu engagieren.  
    - Nachhaltiges Arbeiten: Existiert eine tragende Leitidee/Vision im Team? Oft scheitern Prozesse oder Projekte aufgrund fehlender Klarheit.  
    - Wird bei digitaler Kommunikation auf nachhaltige Anbieter\*innen von Server-, Cloud-Diensten, Mobilfunk, Suchmaschinen etc. geachtet?  
    - Wird auf Geldtransfer über ethische Banken geachtet, die nicht in fossile Brennstoffe investieren ([Fair Finance Guide](https://www.fairfinanceguide.de/))?  
    - Geht in den Austausch: Sind eure Dienstleister\*innen (Presswerke o.ä.) nachweislich auf Nachhaltigkeit ausgerichtet?  
    - Werden lokale Umwelt-NGOs und andere Gruppen gefördert und unterstützt?
    """
    )

if is_kompensation:
    st.markdown(
    """
    ## CO2-Emissionsmessungen und Kompensation  
    - Messt ihr eure CO2-Emissionen?  
    - Leitet ihr aus den Messergebnissen wichtige Maßnahmen und Verbesserungspotenziale ab?  
    - Habt ihr ein Nachhaltigkeitsmanagement im Team?  
    - Arbeitet ihr für eine erfolgreiche Nachhaltigkeitsstrategie mit professionellen Offset-Unternehmen und Lieferanten zusammen?
    """
    )

if is_barrierefreiheit:
    st.markdown(
    """
    ## Barrierefreiheit, soziale Gerechtigkeit, Inklusion  
    Als Teil einer vielfältigen Gesellschaft sind wir alle aufgerufen, Strukturen zu schaffen, die es jedem Menschen ermöglichen, an Veranstaltungen teilzunehmen und sich bei diesen sicher und wohl zu fühlen. Wir möchten, dass alle Besucher\*innen an unseren Konzerten teilhaben können, deshalb wäre es uns wichtig, wenn ihr bei der Veranstaltung auf Barrierefreiheit, Gleichberechtigung und Inklusion achtet (z.B. durch Dolmetscher\*in für Gehörlose, Soli-Tickets, barrierearme Geländegestaltung etc.). Bitte kontaktiert uns, sollte die Location nicht barrierefrei sein.
    """
    )

if is_awareness:
    st.markdown(
    """
    ## Awareness  
    Uns liegt es am Herzen, dass die Locations, bei denen wir spielen, ein Safer Space für alle Beteiligten sind. Ein achtsamer und respektvoller Umgang ist uns wichtig, damit sich alle beim Konzert sicher und wohlfühlen können – dafür sind wir gemeinsam verantwortlich! Wir akzeptieren keinerlei Formen von Diskriminierung. Wir sprechen uns klar gegen Sexismus, Rassismus, Antisemitismus, Ableismus, Body Shaming, Queer- und Transfeindlichkeit, sowie jegliche weitere Formen von psychischer und physischer Gewalt aus.

    - Wird auf Fairness, auch in der Bezahlung, geachtet?  
    - Ist das Team möglichst divers und paritätisch besetzt?  
    - Wenn es euch möglich ist, würden wir uns freuen, wenn ihr uns dabei unterstützt. Im besten Fall habt ihr bereits ein Awareness-Konzept und ein Awareness-Team vor Ort als Anlaufstelle, das sich dem annehmen kann, dementsprechend gekennzeichnet ist und ggf. Rückzugsorte ermöglichen kann. Das würden wir uns wünschen.

    Hier findet ihr weiterführende Informationen und Angebote im Bereich Awareness: [Awareness Akademie](https://www.awareness-akademie.de/), [Safe the Dance](https://www.safethedance.de/), [SONAR Berlin](https://sonar.berlin/), [Act Aware e.V.](https://www.act-aware.de/), [Initiative barrierefrei feiern](https://www.barrierefrei-feiern.de/).
    """
    )

st.markdown(
    """
    ## Vielen Dank für Eure Mithilfe, Zeit, Mühe und die Zusammenarbeit!  
    Gemeinsam können wir die Musikbranche nachhaltiger und achtsamer gestalten. Nicht nur auf der ökologischen Ebene, sondern auch auf der sozialen. Wir bitten euch, diese Punkte zu beachten und sie in die Planung einzubeziehen. Bei Fragen oder Unklarheiten könnt ihr euch gern jederzeit an uns wenden.

    Diese Checkliste wurde zusammengestellt von Music Declares Emergency Germany und ist inspiriert von:
    - Julie's Bicycle Green Rider  
    - Green Rider der Soundsgood Music Agency  
    - GRÜNE MUSIKPRODUKTION bei [listentojules](https://www.listentojules.com/)  
    - Richtlinien Nachhaltigkeit und Awareness von Provinz  
    - Sustainability Checklist von [Sustainable Event Solutions](https://sustainableeventsolutions.com/)

    Weitere Informationen und Hilfestellungen, wie die Musikbranche umweltfreundlicher und nachhaltiger gestaltet werden kann, findet ihr zum Beispiel unter [www.musicdeclares.net/de](https://www.musicdeclares.net/de) oder [www.juliesbicycle.com](https://www.juliesbicycle.com).
    """
)

# Columns example
left_column, right_column = st.columns(2)

# Add a button in the left column and trigger balloons if it's clicked
if left_column.button('Ballons!'):
    st.balloons()  # This will trigger the balloons animation when the button is clicked


# Adressat