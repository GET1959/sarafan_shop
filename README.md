Это проект интернет-магазина.

Для запуска надо заполлнить файл .env по образцу .env.sample.
Данные можно загрузить из фикстуры.

Модель Cart не связана с моделью Product.

POST запрос отправляется в формате:

POST запрос http://localhost:8000/shop/cart-items/
отправляется в формате:

[
    {
        "product_name":"prod_01",
        "product_price":"15",
        "product_quantity":"3"
    },
    {
        "product_name":"prod_02",
        "product_price":"20",
        "product_quantity":"5"
    }
]