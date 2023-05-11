import random

ASSOC_TABLE = "ASSOC_decrypt"
OBJ_TABLE = "OBJ_decrypt"
association_types = ["FRIEND", "LIKES", "AUTHORED"]

def generate_assoc_get_query():
    id1 = random.randint(0, 499)
    assoc_type = random.choice(association_types)
    idset = random.sample(range(500), random.randint(5, 10))
    return f"ASSOC GET {id1} {assoc_type} {idset};"

def generate_assoc_count_query():
    id1 = random.randint(0, 499)
    assoc_type = random.choice(association_types)
    return f"ASSOC COUNT {id1} {assoc_type};"

def generate_assoc_range_query():
    id1 = random.randint(0, 499)
    assoc_type = random.choice(association_types)
    time_lo = random.randint(0, 500)
    time_hi = random.randint(501, 1000)
    lim = random.randint(1, 100)
    return f"ASSOC RANGE {id1} {assoc_type} {time_lo} {time_hi} {lim};"

def generate_assoc_rget_query():
    id1 = random.randint(0, 499)
    assoc_type = random.choice(association_types)
    idset = random.sample(range(500), random.randint(5, 10))
    time_lo = random.randint(0, 500)
    time_hi = random.randint(501, 1000)
    return f"ASSOC RGET {id1} {assoc_type} {idset} {time_lo} {time_hi};"

def generate_obj_get_query():
    id1 = random.randint(0, 499)
    obj_type = random.choice(["USER", "POST"])
    return f"OBJ GET {id1} {obj_type};"

def generate_random_query():
    query_type = random.choices(
        population=["ASSOC GET", "ASSOC RGET", "ASSOC COUNT", "ASSOC RANGE", "OBJ GET"],
        weights=[0.157, 0.409, 0.028, 0.117, 0.289]
    )[0]
    if query_type == "ASSOC GET":
        return generate_assoc_get_query()
    elif query_type == "ASSOC RGET":
        return generate_assoc_rget_query()
    elif query_type == "ASSOC COUNT":
        return generate_assoc_count_query()
    elif query_type == "ASSOC RANGE":
        return generate_assoc_range_query()
    elif query_type == "OBJ GET":
        return generate_obj_get_query()

# Generate 10000 random queries and write them to file
with open("read.txt", "w") as f:
    for i in range(10000):
        query = generate_random_query()
        f.write(query + "\n")