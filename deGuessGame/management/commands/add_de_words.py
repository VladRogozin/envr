from django.core.management.base import BaseCommand
from deGuessGame.models import DeWord  # Замените 'myapp' на имя вашего приложения


class Command(BaseCommand):
    help = 'Add words to the Word model'

    def handle(self, *args, **options):
        words_array = [
            {
                "original_word": "der Mensch",
                "translated_word": "людина",
                "auxiliary_words": {
                    "Menschheit": "людство",
                    "Person": "особа",
                    "Individuum": "індивід"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Mann",
                "translated_word": "чоловік; чоловік",
                "auxiliary_words": {
                    "Kerl": "хлопець",
                    "Herr": "господар",
                    "Ehemann": "чоловік (у шлюбі)"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Frau",
                "translated_word": "жінка; дружина",
                "auxiliary_words": {
                    "Dame": "дама",
                    "Ehefrau": "дружина",
                    "Weib": "жінка (старомодно)"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Kind",
                "translated_word": "дитина",
                "auxiliary_words": {
                    "Junge": "хлопчик",
                    "Mädel": "дівчинка",
                    "Nachwuchs": "нащадок"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Junge",
                "translated_word": "хлопчик",
                "auxiliary_words": {
                    "Kerl": "хлопець",
                    "Bube": "пацан"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Mädchen",
                "translated_word": "дівчинка",
                "auxiliary_words": {
                    "Fräulein": "дівчина (шлюбного віку)",
                    "Kleines Mädchen": "маленька дівчинка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Freund",
                "translated_word": "друг",
                "auxiliary_words": {
                    "Kumpel": "компаньйон",
                    "Kollege": "колега"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Gast",
                "translated_word": "гість",
                "auxiliary_words": {
                    "Besucher": "відвідувач",
                    "Herr": "господар"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Eltern",
                "translated_word": "батьки",
                "auxiliary_words": {
                    "Vater und Mutter": "батько і мати",
                    "Familie": "сім'я"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Vater",
                "translated_word": "батько",
                "auxiliary_words": {
                    "Papa": "тато",
                    "Herr im Haus": "господар у будинку"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Mutter",
                "translated_word": "мати",
                "auxiliary_words": {
                    "Mama": "мама",
                    "Frau des Hauses": "господиня у будинку"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Sohn",
                "translated_word": "син",
                "auxiliary_words": {
                    "Junge": "хлопчик",
                    "Nachkomme": "нащадок"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Tochter",
                "translated_word": "дочка",
                "auxiliary_words": {
                    "Mädel": "дівчинка",
                    "Kind": "дитина"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Großvater",
                "translated_word": "дід...",
                "auxiliary_words": {
                    "Opa": "дідусь",
                    "Altvater": "старий батько"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Schwiegervater",
                "translated_word": "тесть/свекор....",
                "auxiliary_words": {
                    "Vater des Ehepartners": "батько партнера з подружжя",
                    "Familienvater": "батько родини"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Onkel",
                "translated_word": "дядько",
                "auxiliary_words": {
                    "Bruder des Vaters": "брат батька",
                    "Verwandter": "родич"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Tante",
                "translated_word": "тітка",
                "auxiliary_words": {
                    "Schwester des Vaters": "сестра батька",
                    "Verwandte": "родичка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Bruder",
                "translated_word": "брат",
                "auxiliary_words": {
                    "Geschwister": "рідні брати",
                    "Blutsbruder": "кровний брат"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Schwester",
                "translated_word": "сестра",
                "auxiliary_words": {
                    "Geschwister": "рідні сестри",
                    "Blutschwester": "кровна сестра"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Cousin",
                "translated_word": "двоюрідний брат",
                "auxiliary_words": {
                    "Sohn des Onkels oder der Tante": "син дядька чи тітки",
                    "Verwandter": "родич"
                },
                "word_level": "A1"
            },
            {
                "original_word": "die Kusine",
                "translated_word": "двоюрідна сестра",
                "auxiliary_words": {
                    "Tochter des Onkels oder der Tante": "дочка дядька чи тітки",
                    "Verwandte": "родичка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Geschäftsmann",
                "translated_word": "бізнесмен",
                "auxiliary_words": {
                    "Unternehmer": "підприємець",
                    "Manager": "менеджер",
                    "Unternehmensführer": "керівник компанії"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Lehrer",
                "translated_word": "учитель",
                "auxiliary_words": {
                    "Pädagoge": "педагог",
                    "Unterrichtender": "викладач"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Fahrer",
                "translated_word": "водій",
                "auxiliary_words": {
                    "Autofahrer": "водій автомобіля",
                    "Chauffeur": "шофер"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Arbeiter",
                "translated_word": "робітник",
                "auxiliary_words": {
                    "Werktätiger": "працівник",
                    "Handwerker": "ремісник"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Ingenieur",
                "translated_word": "інженер",
                "auxiliary_words": {
                    "Techniker": "технік",
                    "Konstrukteur": "конструктор"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Arzt",
                "translated_word": "лікар",
                "auxiliary_words": {
                    "Mediziner": "медик",
                    "Doktor": "доктор"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Krankenschwester",
                "translated_word": "медсестра",
                "auxiliary_words": {
                    "Pflegerin": "сестра по догляду",
                    "Gesundheitspflegerin": "медсестра"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Verkäufer",
                "translated_word": "продавець",
                "auxiliary_words": {
                    "Einzelhändler": "роздрібний продавець",
                    "Handelsvertreter": "торговий представник"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Buchhalter",
                "translated_word": "бухгалтер",
                "auxiliary_words": {
                    "Finanzbuchhalter": "фінансовий бухгалтер",
                    "Rechnungsprüfer": "ревізор"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Maler",
                "translated_word": "художник",
                "auxiliary_words": {
                    "Künstler": "митець",
                    "Bildermacher": "творець картин"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Journalist",
                "translated_word": "журналіст",
                "auxiliary_words": {
                    "Reporter": "репортер",
                    "Pressevertreter": "представник преси"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Kellner",
                "translated_word": "офіціант",
                "auxiliary_words": {
                    "Servicekraft": "обслуговуючий персонал",
                    "Gastgeber": "господар ресторану"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Musiker",
                "translated_word": "музикант",
                "auxiliary_words": {
                    "Instrumentalist": "інструменталіст",
                    "Künstler der Töne": "митець звуків"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Schauspieler",
                "translated_word": "актор",
                "auxiliary_words": {
                    "Künstler der Bühne": "митець сцени",
                    "Darsteller": "виконавець ролі"
                },
                "word_level": "A2"
            },

            {
                "original_word": "der Schüler",
                "translated_word": "школяр, учень",
                "auxiliary_words": {
                    "Jugendlicher": "підліток",
                    "Bildungssuchender": "освітянин"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Student",
                "translated_word": "студент",
                "auxiliary_words": {
                    "Hochschulstudent": "вищий навчальний заклад",
                    "Studierender": "студент"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Katze",
                "translated_word": "кішка",
                "auxiliary_words": {
                    "Samtpfote": "шерстяна лапа",
                    "Stubentiger": "домашня кішка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Hund",
                "translated_word": "собака",
                "auxiliary_words": {
                    "Wauwau": "гав-гав",
                    "Fellnase": "шерстяний нос"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Vogel",
                "translated_word": "птах",
                "auxiliary_words": {
                    "Flattermann": "летюча тварина",
                    "Gefiederter Freund": "пернатий друг"
                },
                "word_level": "A1"
            },
            {
                "original_word": "die Kuh",
                "translated_word": "корова",
                "auxiliary_words": {
                    "Milchproduzent": "виробник молока",
                    "Wiederkäuer": "жуйний"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Pferd",
                "translated_word": "кінь",
                "auxiliary_words": {
                    "Ross": "кінь (старомодно)",
                    "Reittier": "верхова тварина"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Bär",
                "translated_word": "ведмідь",
                "auxiliary_words": {
                    "Großbär": "великий ведмідь",
                    "Pelzträger": "тварина з хутром"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Maus",
                "translated_word": "миша",
                "auxiliary_words": {
                    "Nager": "гризун",
                    "Kleinsäuger": "малий ссавець"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Schwein",
                "translated_word": "свиня",
                "auxiliary_words": {
                    "Stallgenosse": "товариш по хліву",
                    "Rüsseltier": "тварина з хоботом"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Schule",
                "translated_word": "школа",
                "auxiliary_words": {
                    "Bildungseinrichtung": "навчальний заклад",
                    "Lernstätte": "місце навчання"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Theater",
                "translated_word": "театр",
                "auxiliary_words": {
                    "Bühnenhaus": "будинок для вистав",
                    "Schauspielhaus": "драматичний театр"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Straße",
                "translated_word": "вулиця; дорога",
                "auxiliary_words": {
                    "Fahrbahn": "дорожній полотно",
                    "Verkehrsstraße": "транспортна дорога"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Platz",
                "translated_word": "площа; місце",
                "auxiliary_words": {
                    "Stadtplatz": "міська площа",
                    "Ort": "місце"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Haus",
                "translated_word": "будинок",
                "auxiliary_words": {
                    "Wohnstätte": "місце проживання",
                    "Heim": "дім"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Kirche",
                "translated_word": "церква",
                "auxiliary_words": {
                    "Gotteshaus": "святиня",
                    "Kirchengebäude": "будівля церкви"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Fluss",
                "translated_word": "річка",
                "auxiliary_words": {
                    "Wasserlauf": "водний потік",
                    "Strom": "ріка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Cafe",
                "translated_word": "кафе",
                "auxiliary_words": {
                    "Kaffeehaus": "кав'ярня",
                    "Gastronomiebetrieb": "гастрономічний заклад"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Hotel",
                "translated_word": "готель",
                "auxiliary_words": {
                    "Herberge": "гостинний дім",
                    "Übernachtungsstätte": "місце для ночівлі"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Garten",
                "translated_word": "сад",
                "auxiliary_words": {
                    "Pflanzstätte": "місце посадки",
                    "Grünanlage": "зелений майданчик"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Park",
                "translated_word": "парк",
                "auxiliary_words": {
                    "Landschaftsgarten": "ландшафтний сад",
                    "Erholungsgebiet": "місце відпочинку"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Bank",
                "translated_word": "банк",
                "auxiliary_words": {
                    "Geldinstitut": "грошовий інститут",
                    "Finanzunternehmen": "фінансова компанія"
                },
                "word_level": "A1"
            },
            {
                "original_word": "die Haltestelle",
                "translated_word": "остановка",
                "auxiliary_words": {
                    "Bushaltestelle": "автобусна зупинка",
                    "Bahnhaltestelle": "зупинка поїздів"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Kino",
                "translated_word": "кінотеатр",
                "auxiliary_words": {
                    "Filmpalast": "кінопалац",
                    "Filmtheater": "кінотеатр"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Brücke",
                "translated_word": "міст",
                "auxiliary_words": {
                    "Überführung": "переход",
                    "Steg": "містець"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Kreuzung",
                "translated_word": "перекрёсток",
                "auxiliary_words": {
                    "Verkehrsknotenpunkt": "вузол доріг",
                    "Wegkreuzung": "розігнута дорога"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Wald",
                "translated_word": "ліс",
                "auxiliary_words": {
                    "Forst": "лісництво",
                    "Baumgruppe": "група дерев"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Krankenhaus",
                "translated_word": "больница",
                "auxiliary_words": {
                    "Klinik": "клініка",
                    "Heilanstalt": "лікувальний заклад"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Markt",
                "translated_word": "рынок",
                "auxiliary_words": {
                    "Handelsplatz": "торговий майданчик",
                    "Wochenmarkt": "тижневий ринок"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Polizei",
                "translated_word": "полиция",
                "auxiliary_words": {
                    "Polizeidienststelle": "поліцейський відділ",
                    "Ordnungshüter": "страж порядку"
                },
                "word_level": "A1"
            },

            {
                "original_word": "die Post",
                "translated_word": "почта",
                "auxiliary_words": {
                    "Postamt": "поштове відділення",
                    "Briefstelle": "місце прийому листів"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Bahnhof",
                "translated_word": "станция, вокзал",
                "auxiliary_words": {
                    "Eisenbahnstation": "залізнична станція",
                    "Zughalt": "місце зупинки потяга"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Zentrum",
                "translated_word": "центр",
                "auxiliary_words": {
                    "Innenstadt": "центр міста",
                    "Mittelpunkt": "центральна точка"
                },
                "word_level": "A1"
            },

            {
                "original_word": "das Geschäft",
                "translated_word": "магазин",
                "auxiliary_words": {
                    "Laden": "магазин",
                    "Kaufhaus": "торговий дім"
                },
                "word_level": "A1"
            },

            {
                "original_word": "der Berg",
                "translated_word": "гора",
                "auxiliary_words": {
                    "Berggipfel": "вершина гори",
                    "Gebirge": "гірський хребет"
                },
                "word_level": "A1"
            },
]






        for word_data in words_array:
            word_instance = DeWord(
                original_word=word_data["original_word"],
                translated_word=word_data["translated_word"],
                auxiliary_words=word_data["auxiliary_words"],
                word_level=word_data["word_level"],
            )
            word_instance.save()
        print(len(words_array))
        self.stdout.write(self.style.SUCCESS('Words added successfully!'))










