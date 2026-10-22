from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.knight import Knight

KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            },
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            },
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            },
        },
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    def prepare_knight(name: str) -> Knight:
        data = knights_config[name]
        knight = Knight(
            data["name"],
            data["power"],
            data["hp"],
        )

        # apply armour
        for item in data["armour"]:
            armour = Armour(**item)
            armour.apply_armour(knight)

        # apply weapon
        weapon = Weapon(**data["weapon"])
        weapon.apply_weapon(knight)

        # apply potion if exist
        if data["potion"]:
            potion = Potion(**data["potion"])
            potion.apply_potion(knight)

        return knight

    def knightly_duel(knight_1: Knight, knight_2: Knight) -> None:
        knight_1.hp -= knight_2.power - knight_1.protection
        knight_2.hp -= knight_1.power - knight_2.protection
        knight_1.hp = max(knight_1.hp, 0)
        knight_2.hp = max(knight_2.hp, 0)

    # lancelot
    lancelot = prepare_knight("lancelot")

    # arthur
    arthur = prepare_knight("arthur")

    # mordred
    mordred = prepare_knight("mordred")

    # red_knight
    red_knight = prepare_knight("red_knight")

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knightly_duel(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    knightly_duel(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
