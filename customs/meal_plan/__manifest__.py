{
    "name":"Fewa Meal Plan",
    "version":"1.0",
    "depends":["base","mail"],
    "data":[
        "views/meal_plan.xml",
        "views/meals.xml",
        "views/active_menu.xml",
        "views/menu.xml",

        "data/cron.xml",
        "security/ir.model.access.csv"
    ],
    "assets":{
        "web.assets_backend":[
            "meal_plan/static/src/**/*.png"
        ]
    },
    "application":True
}