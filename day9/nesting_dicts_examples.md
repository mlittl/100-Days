## Python Dictionaries

```python
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}
```
### To retrieve items from the dictionary, you can use the key:
```
    print(programming_dictionary["Function"])
```
### You can add new items to the dictionary like this:
```
    programming_dictionary["Loop"] = "The action of doing something over and over again."
```
### You can create an empty dictionary:
```
    empty_dictionary = {}
```
### You can wipe an existing dictionary:
```
    programming_dictionary = {}
    print(programming_dictionary)
```
### You can edit an item in a dictionary:
```
    programming_dictionary["Bug"] = "A moth in your computer."
    print(programming_dictionary)
```
### You can loop through a dictionary:

```
    for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```

## Nesting

### You can nest dictionaries:
```
    capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    }
```
### You can nest a list in a dictionary:
```
    travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    }
```
### You can nest a dictionary in a dictionary:
```
    travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    }
```
### You can nest dictionaries in lists:
```
    travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12,
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
    },
    ]
```
