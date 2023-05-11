import random
from faker import Faker

fake = Faker()

ASSOC_TABLE = "ASSOC_TEST"
OBJ_TABLE = "OBJ_TEST"


def random_name():
    return fake.name().replace("'", "''")


def random_sentence():
    return fake.sentence().replace("'", "''")


def random_time():
    return random.randint(0, 1000)


def main():
    cliques = {
        "clique1": (0, 60),
        "clique2": (100, 160),
        "clique3": (200, 260),
    }

    object_types = ["USER", "POST"]
    association_types = ["FRIEND", "LIKES", "AUTHORED"]

    authored_associations = []
    friend_associations = []
    likes_associations = []

    authored_associations_sql = []
    friend_associations_sql = []
    likes_associations_sql = []

    max_likes = 5
    max_friends = 5

    with open("commands.txt", "w") as f:
        with open("commands.sql", "w") as f2:
            for clique, (start, end) in cliques.items():
                for i in range(start, end + 1, 2):
                    user_id = i
                    post_id = i + 1

                    name = random_name()
                    sentence = random_sentence()

                    # TAO Queries
                    f.write(f"OBJ ADD {user_id} {object_types[0]} \'{name}\';\n")
                    f.write(f"OBJ ADD {post_id} {object_types[1]} \'{sentence}\';\n")

                    f2.write(
                        f"INSERT INTO {OBJ_TABLE} (id, otype, data) VALUES ('{user_id}', '{object_types[0]}', '{name}');\n")
                    f2.write(
                        f"INSERT INTO {OBJ_TABLE} (id, otype, data) VALUES ('{post_id}', '{object_types[1]}', '{sentence}');\n")

                    authored_time = random_time()
                    friend_time = random_time()
                    likes_time = random_time()

                    # TAO Queries
                    authored_associations.append(
                        f"ASSOC ADD {user_id} {association_types[2]} {post_id} {authored_time} '';\n"
                    )
                    # SQL Queries
                    authored_associations_sql.append(
                        f"INSERT INTO {ASSOC_TABLE} (id1, atype, id2, t, data) VALUES ('{user_id}', '{association_types[2]}', '{post_id}', {authored_time}, '');\n"
                    )

                    for _ in range(random.randint(1, max_friends)):
                        friend_id = random.choice([x for x in range(start, end + 1, 2) if x != user_id])
                        # TAO Queries
                        friend_associations.append(
                            f"ASSOC ADD {user_id} {association_types[0]} {friend_id} {friend_time} '';\n"
                        )
                        # SQL Queries
                        friend_associations_sql.append(
                            f"INSERT INTO {ASSOC_TABLE} (id1, atype, id2, t, data) VALUES ('{user_id}', '{association_types[0]}', '{friend_id}', {friend_time}, '');\n"
                        )

                    for _ in range(random.randint(1, max_likes)):
                        liked_post_id = random.choice([x for x in range(start, end + 1, 2) if x != user_id])
                        # TAO Queries
                        likes_associations.append(
                            f"ASSOC ADD {user_id} {association_types[1]} {post_id} {likes_time} '';\n"
                        )
                        # SQL Queries
                        likes_associations_sql.append(
                            f"INSERT INTO {ASSOC_TABLE} (id1, atype, id2, t, data) VALUES ('{user_id}', '{association_types[1]}', '{post_id}', {likes_time}, '');\n"
                        )

            for association in authored_associations + friend_associations + likes_associations:
                f.write(association)
            for association in authored_associations_sql + friend_associations_sql + likes_associations_sql:
                f2.write(association)


if __name__ == "__main__":
    main()
