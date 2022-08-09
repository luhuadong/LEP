
class DictUtil:

    '''
    Compare two dicts.
    If the two dicts are equal, return 0;
    If the first one contains the second one ( first one is a superset of the second), return 1;
    If the second one contains the first one ( first one is a subset of the second ), return -1;
    Otherwise, return 2;
    '''
    @staticmethod
    def compare(dict_1, dict_2):

        if not dict_1 and not dict_2:
            return 0

        if not dict_1:
            return -1

        if not dict_2:
            return 1

        # Store the keys of the dictionary in the collection,
        # if dict_1 is None, set(dict_1) will return empty collection.
        tdict_1 = set(dict_1)
        tdict_2 = set(dict_2)

        flag = 2

        # If the keys are exactly equal, and then judge whether
        # the value of the key corresponding to the equal.
        if tdict_1 == tdict_2:
            flag = 0
            for key in tdict_1:
                if dict_1[key] != dict_2[key]:
                    if isinstance(dict_1[key], dict):
                        flag = DictUtil.compare(dict_1[key], dict_2[key])
                    elif isinstance(dict_1[key], list):
                        len_1 = len(dict_1[key])
                        len_2 = len(dict_2[key])
                        if len_1 > len_2:
                            flag = 1
                            for val in dict_2[key]:
                                if val not in dict_1[key]:
                                    return 2
                        else:
                            flag = -1
                            for val in dict_1[key]:
                                if val not in dict_2[key]:
                                    return 2
                    else:
                        return 2

        # If the keys of dict_1 contains the keys of dict_2, and then
        # judge the value of the dict_2's key corresponding to the equal.
        elif tdict_1 > tdict_2:
            flag = 1
            for key in dict_2:
                if dict_1[key] != dict_2[key]:
                    if isinstance(dict_1[key], dict):
                        flag = DictUtil.compare(dict_1[key], dict_2[key])
                    elif isinstance(dict_1[key], list):
                        len_1 = len(dict_1[key])
                        len_2 = len(dict_2[key])
                        if len_1 > len_2:
                            for val in dict_2[key]:
                                if val not in dict_1[key]:
                                    return 2
                        else:
                            return 2
                    else:
                        return 2

        # If the keys of dict_2 contains the keys of dict_1, and then
        # judge the value of the dict_1's key corresponding to the equal.
        elif tdict_1 < tdict_2:
            flag = -1
            for key in dict_1:
                if dict_1[key] != dict_2[key]:
                    if isinstance(dict_1[key], dict):
                        flag = DictUtil.compare(dict_1[key], dict_2[key])
                    elif isinstance(dict_1[key], list):
                        len_1 = len(dict_1[key])
                        len_2 = len(dict_2[key])
                        if len_1 < len_2:
                            for val in dict_1[key]:
                                if val not in dict_2[key]:
                                    return 2
                        else:
                            return 2
                    else:
                        return 2

        return flag

    '''
        Locate the first direct child node of a dict or dict array whose specified property key has the value of property value    
    '''
    @staticmethod
    def locate_node_by_property_value(dictionary, property_key, property_value):

        s = isinstance(dictionary, dict)
        sq = isinstance(dictionary, list)

        if isinstance(dictionary, dict):
            if property_key not in dictionary:
                return None

            if dictionary[property_key] == property_value:
                return dictionary

            return None

        elif isinstance(dictionary, list):
            for sub_dictionary in dictionary:
                if not isinstance(sub_dictionary, dict):
                    continue

                if property_key not in sub_dictionary:
                    continue

                if sub_dictionary[property_key] == property_value:
                    return sub_dictionary

            return None

        else:
            raise ValueError('the specified dictionary is neither a map nor a list')


