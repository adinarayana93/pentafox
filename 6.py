def fun(people):
    dici = {}
    for d in people:
	    name = d['name']
	    age = d['age']
	    if age in dici:
	        dici[age].append(name)
	    else:
	        dici[age] = [name]

    return dici


people = [
{'name': 'John', 'age': 25},
{'name': 'Jane', 'age': 30},
{'name': 'Alice', 'age': 25},
{'name': 'Bob', 'age': 30}
]
print(fun(people))