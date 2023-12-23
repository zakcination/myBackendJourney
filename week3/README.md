### Task 1

## 1) What is the ChainMap?
    
    ChainMap is a data structure provided by the Python standard library that allows you to treat multiple dictionaries as one.

The official documentation on ChainMap reads:

A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. […] Lookups search the underlying mappings successively until a key is found. […] If one of the underlying mappings gets updated, those changes will be reflected in ChainMap. […] All of the usual dictionary methods are supported.

In other words: a ChainMap is an updatable view over multiple dicts, and it behaves just like a normal dict.

However, the use cases may include:
    Searching through multiple dictionaries
    Providing a chain of default values
    Performance-critical applications that frequently compute subsets of a dictionary


Example covered in the my_chainmap.py is about shopping inventory