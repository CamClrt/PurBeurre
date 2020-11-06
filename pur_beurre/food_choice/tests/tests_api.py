"""This module test the google the OpenFoodFacts API class."""

from unittest.mock import patch
from django.test import TestCase
from food_choice.api import API
import requests


categories_res = {
    "tags": [
        {"name": "Aliments et boissons à base de végétaux"},
        {"name": "Aliments d'origine végétale"},
        {"name": "Snacks"},
        {"name": "Snacks sucrés"},
        {"name": "Boissons"},
        {"name": "Viandes"},
        {"name": "Produits laitiers"},
        {"name": "Plats préparés"},
        {"name": "Aliments à base de fruits et de légumes"},
        {"name": "Céréales et pommes de terre"},
        {"name": "Produits fermentés"},
        {"name": "Produits laitiers fermentés"},
        {"name": "Produits à tartiner"},
        {"name": "Biscuits et gâteaux"},
        {"name": "Charcuteries"},
    ],
    "count": 15,
}


class CategoryMockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return categories_res

    parameters = {
        "address": "fake-address",
        "key": "fake-key",
    }

    headers = {
        "date": "06/11/2020",
        "user-agent": '"FoodChoice/fake_version',
    }


class Test__categories(TestCase):

    """GIVEN a mocke version of requests.get() WHEN the HTTP response
    is set to successful THEN check the HTTP response."""

    @patch("requests.get", return_value=CategoryMockResponse())
    def test__categories(self, mocked):
        api = API()
        api.categories
        result = api.selected_categories
        expected_result = [
            "Aliments et boissons à base de végétaux",
            "Aliments d'origine végétale",
            "Snacks",
            "Snacks sucrés",
            "Boissons",
        ]
        self.assertEqual(result, expected_result)


products_res = {
    "products": [
        {
            "product_name_fr": "Farine complète de Petit Épeautre",
            "nutrition_grades_tags": ["a"],
            "url": "https://fr.openfoodfacts.org/produit/3273120020969/farine-complete-de-petit-epeautre-celnat",
            "nutriments": {
                "fat_100g": 3.7,
                "carbohydrates_100g": 58.4,
                "fiber_100g": 10.1,
                "saturated-fat_100g": 0.7,
                "proteins_100g": 11.9,
                "sugars_100g": 1.8,
                "energy_100g": 1402,
                "salt_100g": 0.01,
            },
            "image_url": "https://static.openfoodfacts.org/images/products/327/312/002/0969/front_fr.51.400.jpg",
            "code": "3273120020969",
        }
    ]
}


class ProductMockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return products_res

    parameters = {
        "address": "fake-address",
        "key": "fake-key",
    }

    headers = {
        "date": "06/11/2020",
        "user-agent": '"FoodChoice/fake_version',
    }


class Test_products(TestCase):
    """GIVEN a mocke version of requests.get() WHEN the HTTP response
    is set to successful THEN check the HTTP response."""

    @patch("requests.get", return_value=ProductMockResponse())
    def test_products(self, mocked):
        api = API()
        api.selected_categories = [
            "Aliments et boissons à base de végétaux",
            "Aliments d'origine végétale",
            "Snacks",
            "Snacks sucrés",
            "Boissons",
        ]
        expected_result = [
            products_res.get("products")[0],  # request & cat n°1
            products_res.get("products")[0],  # request & cat n°2
            products_res.get("products")[0],  # request & cat n°3
            products_res.get("products")[0],  # request & cat n°4
            products_res.get("products")[0],  # request & cat n°5
        ]
        result = api.products
        self.assertEqual(result, expected_result)