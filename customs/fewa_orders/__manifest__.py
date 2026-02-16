{
    "name":"Fewa Orders",
    "version":"1.0",
    "depends":["base","meal_plan","companies_extension"],
    "data":[
        "views/user_plans.xml",
        "views/user_orders.xml",
        "views/orders_collection.xml",
        "views/menu.xml",

        "data/collectio_sequence.xml",
        "security/ir.model.access.csv"
    ],
    "assets":{
        "web.assets_backend":[
            "fewa_orders/static/src/**/*.png"
        ]
    }
}