from django.core.management.base import BaseCommand
from food_choice.models import Category, Product
from food_choice.api import API
from progress.bar import Bar


class Command(BaseCommand):
    help = "From OpenFoodFacts API upload product informations in database"

    def handle(self, *args, **kwargs):
        api = API()
        api.categories
        imported_products = api.products

        # A SUPPRIMER ENSUITE
        categories = api.selected_categories
        for category in categories:
            print(category)
        # A SUPPRIMER ENSUITE

        if imported_products is not None:
            self.stdout.write(self.style.SUCCESS("API import: success"))
        else:
            self.stdout.write(self.style.ERROR("API import: error"))

        # insert data in DB
        print("\n----> Insertion des données en base <----\n")

        with Bar("Progression", max=len(imported_products)) as bar:
            for imported_product in imported_products:

                imported_categories = []
                # filter & insert categories
                tmp_categories = imported_product.get("categories", "").split(",")
                for tmp_category in tmp_categories:
                    tmp_category = tmp_category[:50]
                    if tmp_category is not None:
                        imported_categories.append(category)

                # filter & insert products
                name = imported_product.get("product_name_fr", "")[:150]
                brand = imported_product.get("brands", "")[:100]
                url = imported_product.get("url", "")
                image_url = imported_product.get("image_url", "")
                code = imported_product.get("code", (13 * "0"))
                nutrition_grade = imported_product.get("nutrition_grades", "z")[:1]
                energy_100g = imported_product.get("nutriments", "").get(
                    "energy_100g", "999999"
                )
                # get nutriments details
                fat = imported_product.get("nutriments", "").get("fat_100g", "999999")

                saturates = imported_product.get("nutriments", "").get(
                    "saturated-fat_100g", "999999"
                )

                carbohydrate = imported_product.get("nutriments", "").get(
                    "carbohydrates_100g", "999999"
                )

                sugars = imported_product.get("nutriments", "").get(
                    "sugars_100g", "999999"
                )

                protein = imported_product.get("nutriments", "").get(
                    "proteins_100g", "999999"
                )

                salt = imported_product.get("nutriments", "").get("salt_100g", "999999")

                fiber = imported_product.get("nutriments", "").get(
                    "fiber_100g", "999999"
                )

                bar.next()

        # A REVOIR
        if imported_products is not None:
            self.stdout.write(self.style.SUCCESS("DB import: success"))
        else:
            self.stdout.write(self.style.ERROR("DB import: error"))
