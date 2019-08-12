
from typing import List, Union, Dict

def deep_key_test(dict_or_list: Union[Dict, List], keys: List[Union[str, int]]) -> bool:
    """A recursive method to test the presence of a key in a structure of embedded lists or dicts
    
    :return: `True` if the sequence of key is in the structure, `False` otherwise

    >>> x = {'c': [{'t': 42}]}
    >>> deep_key_test(x, ['c', 0, 't'])
    True
    >>> x['c'] and len(x['c']) > 0 and ('t' in x['c'][0])
    True
    """

    if len(keys) > 0:
        # if there is a key left to test, grab it and try to go deeper
        key, keys = keys[0], keys[1:]
        
        if isinstance(dict_or_list, dict):
            # if the structure explored is a dict, the test is locally a sucess if the key is in the 'key set' of the dict
            # if the test is locally a sucess, will try to go deeper; else will return false
            return key in dict_or_list.keys() and deep_key_test(dict_or_list[key], keys)

        elif isinstance(dict_or_list, list) and isinstance(key, int):
            # if the structure explored is a list, the test is locally a sucess if the length of the list is higher than the key
            # if the test is locally a sucess, will try to go deeper; else will return false
            return len(dict_or_list) > key and deep_key_test(dict_or_list[key], keys)
        
        return False
    
    else:
        # if there is no key left to test, the test is a success
        return True