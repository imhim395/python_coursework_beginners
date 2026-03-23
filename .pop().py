ex = {"make": "Honda", "model": "civic", "year": 2016}
ex.pop("model")#removes model key value pair from the dictionary
print(ex)

ex = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex.pop("model")
print(popped)#prints civic because it's the popped item from model key value pair