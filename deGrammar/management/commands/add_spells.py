from django.core.management.base import BaseCommand
from deGrammar.models import Spell


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        data_arr = [

                {"word": "Молоко", "variants": ["Die Milch", "Das Milko", "Der Milk"]},
                {"word": "Вода", "variants": ["Das Wasser", "Die Wassa", "Der Wode"]},
                {"word": "Ліжко", "variants": ["Das Bett", "Die Bette", "Der Bedd"]},
                {"word": "Дерево", "variants": ["Der Baum", "Das Baam", "Die Boem"]},
                {"word": "Година", "variants": ["Die Stunde", "Das Stund", "Der Stunden"]},
                {"word": "Яблуко", "variants": ["Der Apfel", "Das Apfle", "Die Apple"]},
                {"word": "Спідниця", "variants": ["Der Rock", "Die Spidnitz", "Das Spind"]},
                {"word": "Чашка", "variants": ["Die Tasse", "Der Tasche", "Das Tass"]},
                {"word": "Вечір", "variants": ["Der Abend", "Das Eben", "Die Eve"]},
                {"word": "Колір", "variants": ["Die Farbe", "Das Farben", "Der Kolore"]},
                {"word": "Квітка", "variants": ["Die Blume", "Das Blumen", "Der Blom"]},
                {"word": "Вікно", "variants": ["Das Fenster", "Die Fenst", "Der Fentzer"]},
                {"word": "Місяць", "variants": ["Der Mond", "Das Monde", "Die Moon"]},
                {"word": "Сміх", "variants": ["Das Lachen", "Die Lachin", "Der Laugh"]},
                {"word": "Шлях", "variants": ["Der Weg", "Die Wegen", "Das Wagh"]},
                {"word": "Вечеря", "variants": ["Das Abendessen", "Der Dinner", "Die Abendmahlzeit"]},
                {"word": "Рука", "variants": ["Die Hand", "Der Hant", "Das Hande"]},
                {"word": "Хліб", "variants": ["Das Brot", "Der Brod", "Die Brote"]},
                {"word": "Кава", "variants": ["Der Kaffee", "Die Caffa", "Das Kaffe"]},
                {"word": "Дорога", "variants": ["Der Weg", "Die Wega", "Das Woge"]},
                {"word": "Волосся", "variants": ["Die Haare", "Das Hare", "Der Haar"]},
                {"word": "Сніг", "variants": ["Der Schnee", "Das Snei", "Die Sneg"]},
                {"word": "Робота", "variants": ["Die Arbeit", "Der Arbeite", "Das Arbeiten"]},
                {"word": "Відпочинок", "variants": ["Die Erholung", "Der Relax", "Das Ruhe"]},
                {"word": "Літо", "variants": ["Der Sommer", "Das Sommer", "Die Sumer"]},
                {"word": "Окно", "variants": ["Das Fenster", "Die Fentzer", "Der Fenst"]},
                {"word": "Мама", "variants": ["Die Mutter", "Der Mama", "Das Mum"]},
                {"word": "Тато", "variants": ["Der Vater", "Die Tata", "Das Dad"]},
                {"word": "Школа", "variants": ["Die Schule", "Der School", "Das Schulen"]},
                {"word": "Країна", "variants": ["Das Land", "Die Landa", "Der Londe"]},
                {"word": "Мова", "variants": ["Die Sprache", "Das Sprach", "Der Spreech"]},
                {"word": "Острів", "variants": ["Die Insel", "Der Insel", "Das Eiland"]},
                {"word": "Коло", "variants": ["Der Kreis", "Das Circle", "Die Rund"]},
                {"word": "Ніч", "variants": ["Die Nacht", "Der Nocht", "Das Nichte"]},
                {"word": "Птах", "variants": ["Der Vogel", "Das Vogle", "Die Fowl"]},
                {"word": "Вечірка", "variants": ["Die Party", "Das Feest", "Der Abendfest"]},
                {"word": "Лікарня", "variants": ["Das Krankenhaus", "Die Krankenhaus", "Der Heil"]},
                {"word": "Друзі", "variants": ["Die Freunde", "Der Frienden", "Das Freund"]}
            ]

        for data in data_arr:
            new_instance = Spell(
                word=data,
                level="A1"
            )
            new_instance.save()

        print(len(data_arr))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))
