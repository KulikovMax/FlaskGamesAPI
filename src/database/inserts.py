from datetime import date

from src import db
from src.database.models import Game, Companion


def populate_games():
    mass_effect = Game(
        title='Mass Effect',
        release_date=date(2007, 11, 20),
        description="The galaxy is trapped in an endless cycle of extinction. Every 50,000 years, an ancient machine race invades the galaxy. With ruthless efficiency, the machines wipe out all advanced organic civilization. They leave behind only the scattered ruins of technology, destroying all evidence of their own existence.\n\nFew believe this ancient legend. You, however, know it to be true. The fight to stop this extinction event has become the most important mission in the galaxy.\n\nIt is your mission. As Commander Shepard of the SSV Normandy, you will take your elite recon squad across a galaxy in turmoil, in a desperate race to stop the return of an enemy without mercy. To stop this enemy, you must act without remorse, without hesitation, and outside the limits of the law. Your only imperative is to preserve the safety of civilized life in the galaxy - at any cost. You must become the tip of the spear of humanity, for you alone know the full extent of what is at stake if you should fail.",
        developed_by="BioWare",
        duration=43,
        rating=89
    )
    mass_effect_galaxy = Game(
        title='Mass Effect Galaxy',
        release_date=date(2009, 6, 22),
        description="The Mass Effect universe has landed on the iPhone and iPod Touch gaming platforms! Tales of human courage and individual human achievement resound throughout the galaxy. Here is your opportunity to play the story of Jacob Taylor - a new character in Mass Effect 2 - a biotic-powered super-soldier who stumbles across a plot to terrorize civilization's greatest beacon of hope.\n\nCan you prevent an heinous attack that threatens to knock humanity off the galactic stage?",
        developed_by="EA Mobile",
        duration=2,
        rating=2
    )
    mass_effect_2 = Game(
        title='Mass Effect 2',
        release_date=date(2010, 1, 26),
        description="Two years after Commander Shepard repelled invading Reapers bent on the destruction of organic life, a mysterious new enemy has emerged. On the fringes of known space, something is silently abducting entire human colonies. Now Shepard must work with Cerberus, a ruthless organization devoted to human survival at any cost, to stop the most terrifying threat mankind has ever faced.\n\nTo even attempt this perilous mission, Shepard must assemble the galaxy's most elite team and command the most powerful ship ever built. Even then, they say it would be suicide. Commander Shepard intends to prove them wrong.",
        developed_by="BioWare",
        duration=50.5,
        rating=94
    )
    mass_effect_infiltrator = Game(
        title='Mass Effect Infiltrator',
        release_date=date(2012, 3, 6),
        description="YOU’RE A CERBERUS AGENT – GONE ROGUE! As Commander Shepard battles Reapers across the galaxy, veteran Cerberus agent Randall Ezno procures aliens for illicit experiments at a secret facility. But when the Director of the facility goes too far - Randall fights back and vows to bring Cerberus down!\n\nCan you fight your way off the hostile Cerberus base and deliver their secret research to the Alliance?",
        developed_by="Iron Monkey Studios",
        duration=4,
        rating=68
    )
    mass_effect_3 = Game(
        title='Mass Effect 3',
        release_date=date(2012, 3, 6),
        description="Earth is burning. Striking from beyond known space, a race of terrifying machines have begun their destruction of the human race. As Commander Shepard, an Alliance Marine, your only hope for saving mankind is to rally the civilizations of the galaxy and launch one final mission to take back the Earth.",
        developed_by="BioWare",
        duration=50,
        rating=89
    )
    mass_effect_andromeda = Game(
        title='Mass Effect: Andromeda',
        release_date=date(2017, 3, 21),
        description="At the end of the centuries-long voyage, the Hyperion finally arrives in the Heleus Cluster and Ryder wakes up from cryostasis. Soon after, the ark strikes an unknown object in space, temporarily disabling the power and artificial gravity. Despite these complications, the Hyperion reaches Habitat 7, humanity's designated home. However, to the surprise of the crew, Habitat 7 appears vastly different from their initial scans from the Milky Way prior to departure. Unwilling to believe the journey was for naught, the Pathfinder team decides to survey the planet to determine its viability. The atmospheric conditions being more than they could anticipate, the team crash lands on the planet. There, they encounter a harsh environment, hostile aliens, and unknown mega-structures. In time, they successfully retreat from the planet but suffer a great misfortune in the process. With Habitat 7 deemed inhospitable and the team still reeling from the setback, it is up to Ryder to head into the unknown to find a new home for humanity.",
        developed_by="BioWare",
        duration=94,
        rating=71
    )
    garrus = Companion(
        name='Garrus Vakarian',
        in_game_class='Turian Agent',
        debut=date(2007, 11, 20),
        is_romance=True
    )
    kaidan = Companion(
        name="Kaidan Alenko",
        in_game_class='Systems Alliance Sentinel',
        debut=date(2007, 11, 20),
        is_romance=True
    )
    ashley = Companion(
        name='Ashley Williams',
        in_game_class='Systems Alliance Soldier',
        debut=date(2007, 11, 20),
        is_romance=True
    )
    wrex = Companion(
        name='Urdnot Wrex',
        in_game_class='Krogan Battlemaster',
        debut=date(2007, 11, 20),
        is_romance=True
    )
    liara = Companion(
        name="Liara T'Soni",
        in_game_class='Asari Scientist',
        debut=date(2007, 11, 20),
        is_romance=True
    )
    tali = Companion(
        name="Tali'Zorah nar Rayya",
        in_game_class='Quarian Machinist',
        debut=date(2007, 11, 20),
        is_romance=True
    )

    mass_effect.companions = [garrus, kaidan, ashley, wrex, liara, tali]
    mass_effect_2.companions = [garrus, tali]
    mass_effect_3.companions = [garrus, kaidan, ashley, liara, tali]

    db.session.add(garrus)
    db.session.add(kaidan)
    db.session.add(ashley)
    db.session.add(wrex)
    db.session.add(tali)
    db.session.add(liara)

    db.session.add(mass_effect)
    db.session.add(mass_effect_galaxy)
    db.session.add(mass_effect_2)
    db.session.add(mass_effect_infiltrator)
    db.session.add(mass_effect_3)
    db.session.add(mass_effect_andromeda)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_games()
    print('Successfully populated!')
