#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # add test data
    mario_kart = Game(
        title="Mario Kart",
        platform="Switch",
        genre="Racing",
        price=60
    )

    session.add(mario_kart)
    session.commit()

    mk_review_1 = Review(
        score=10,
        comment="Wow, what a game",
        game_id=mario_kart.id
    )

    mk_review_2 = Review(
        score=8,
        comment="A classic",
        game_id=mario_kart.id
    )

    session.bulk_save_objects([mk_review_1, mk_review_2])
    session.commit()

    import ipdb; ipdb.set_trace()
