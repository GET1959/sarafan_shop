Это проект интернет-магазина.

Для запуска надо заполлнить файл .env по образцу .env.sample.
Данные можно загрузить из фикстуры.

Пустым POST запросом http://localhost:8000/shop/basket/ создается пустая корзина,
Потом POST запросом  на http://localhost:8000/shop/basket-items/ в формате

[{
    "basket": 4,
    "product": 5,
    "quantity": 5
}]

добавляется продукт.