"""Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)
        
        
def get_last_name(name: str) -> str:
    
    """Return the text that comes after the final space(' ') in name
    
    >>>get_last_name('Anya Tafliovich')
    'Tafliovich'
    
    """
    
    while ' ' in name:
        
        name = name[name.index(' ') + 1:]
        
    return name

def get_first_name(name: str) -> str:
    
    """Return the text from the start of name until the last space(' ') in
    name.
    
    >>>get_first_name('Hikaru Nakamura')
    'Hikaru'
    
    """
    if ' ' in name:
        
        name = name[:name.rfind(' ')]
    
    return name



def bubble_down(lis: list) -> list:
    """Bubble down through L from indexes end through start, swapping items that
    are out of place.

    >>> L = [2, 3, 4, 1, 0]
    >>> bubble_down(L)
    [4,3,2,1,0]
    
    
    """
    end = len(lis) - 1
    
    while end != 0:
        
        for i in range(end):
            if lis[i][1] < lis[i + 1][1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                
        end = end - 1
        
    return lis



def remove_blank_lists(given: dict) -> None:
    
    '''
    Remove all the keys that are equal to the value [] and return the dict.
    
    >>>remove_blank_lists({'a': []})
    {}
    '''
    
    rlist = []
    
    for i in given:
        
        if given[i] == []:
            
            rlist.append(i)
            
    for i in rlist:
        
        given.pop(i)
        
        
        
def mutual_club_implementor(person_to_friends: dict, person_to_clubs: dict, \
                            person: str) -> dict:
    
    """
    Checks for and builds score for the clubs of people who are in person's
    clubs.
    
    >>>mutual_club_implementor(P2F, P2C, 'Comet Club')
    """
    
    persons_clubs = []
    
    b = invert_and_sort(person_to_clubs)
    
    others_clubs = []
    
    others = []
    
    final = {}
    
    a = get_clubs_of_friends(person_to_friends, person_to_clubs, person)    

        
    for i in person_to_clubs[person]:
        
        persons_clubs.append(i)

    for i in persons_clubs:
        
        for k in b[i]:
            
            if k != person:
                
                others.append(k)

    for i in others:
                        
        for j in person_to_clubs[i]:
            
            if j not in person_to_clubs[person] and j not in a:
                
                others_clubs.append(j)

    for c in others_clubs:
        
        if c not in final:
            
            final[c] = [1]
            
        else:
            
            final[c].append(1)          
                    
    return final


def fr_club_mutual(i: str, person: str, person_to_clubs: dict) \
    -> int:
    
    """
    Increments the score of club i by the number of mutual club members
    person has in that club.
    
    """
    
    score = 0
    maxer = 0
    b = invert_and_sort(person_to_clubs)
    
    if person in person_to_clubs:
        
        for k in b[i]:
            
            for j in person_to_clubs[k]:
                
                if j in person_to_clubs[person] and maxer == 0:
                    
                        
                    score = score + 1
                    maxer = maxer + 1
                        
                        
            maxer = 0
            
    return score
                                

# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file.

    NOTE: Functions (including helper functions) that have a parameter
          of type TextIO do not need docstring examples.

    """
    
    lines = profiles_file.readlines()
    
    
    name = ''
    
    p2friends = {}
    
    p2clubs = {}
    
    
    
    for line in range(len(lines)):
        
        if line == 0 or lines[line - 1] == '\n':
            
            name = lines[line][lines[line].find(',') + 2: -1] + ' ' + \
                lines[line][:lines[line].find(',')]
            
            p2friends[name] = []
            
            p2clubs[name] = []
            
            
        elif ',' in lines[line]:
            
            p2friends[name].append(lines[line][lines[line].find(',') + 2:-1] + \
                                   ' ' + lines[line][:lines[line].find(',')])        

            
        elif lines[line] != '\n':
            
            p2clubs[name].append(lines[line].strip())
            
            
    remove_blank_lists(p2friends)
    remove_blank_lists(p2clubs)
    
    
    return (p2friends, p2clubs)
 
            
            
    
    


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    Precondition: person_to_clubs must have at least 1 person.
    
    >>> get_average_club_count(P2C)
    1.6

    """
    
    denom = 0
    total = 0
    
    for i in person_to_clubs:
        
        denom = denom + 1
        
        total = total + len(person_to_clubs[i])
        
    if denom == 0:
        return 0.0
        
    return total / denom
        
    # +COMPLETE
        
    

def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people
    from the "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    """
    
    last_to_first = {}
    
    for i in person_to_friends:
        
        if get_last_name(i) not in last_to_first:
            
            last_to_first[get_last_name(i)] = []
            
        if get_first_name(i) not in last_to_first[get_last_name(i)]:
            
            last_to_first[get_last_name(i)].append(get_first_name(i))
        
        for k in person_to_friends[i]:
            
            if get_last_name(k) not in last_to_first:
                
                last_to_first[get_last_name(k)] = []
            
            if get_first_name(k) not in last_to_first[get_last_name(k)]:
                
                last_to_first[get_last_name(k)].append(get_first_name(k))
                
    for i in last_to_first:
        
        last_to_first[i].sort()
                
    return last_to_first
        
        
    
    # +COMPLETE


def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    """
    inverse_dict = {}
    
    for i in key_to_value:
        
        if type(key_to_value[i]) == str or type(key_to_value[i]) == int:
            
            if key_to_value[i] not in inverse_dict:
                
                inverse_dict[key_to_value[i]] = []
                
            if i not in inverse_dict[key_to_value[i]]:
                
                inverse_dict[key_to_value[i]].append(i)
                
        else:
            
            for k in key_to_value[i]:
                
                if k not in inverse_dict:
                    
                    inverse_dict[k] = []
                    
                if i not in inverse_dict[k]:
                    
                    inverse_dict[k].append(i)
                    
    for i in inverse_dict:
        
        inverse_dict[i].sort()
        
    return inverse_dict
    
    
    # +COMPLETE
    

def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    """
    
    clubs_of_friends = []
    
    if person in person_to_friends:
    
        for i in person_to_friends[person]:
            
            if i in person_to_clubs:
            
                for k in person_to_clubs[i]:                
                    
                    clubs_of_friends.append(k)
    
    if person in person_to_clubs:
            
        for j in person_to_clubs[person]:
            
            while j in clubs_of_friends:
                
                clubs_of_friends.remove(j)
            
    clubs_of_friends.sort()
    
    return clubs_of_friends
    
    
    # +COMPLETE
    

def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

    """
    s = 0
        
    clubs_to_score = {}
    
    recommendations = []
        
    score = 0
    
    a = get_clubs_of_friends(person_to_friends, person_to_clubs, person)
    
    
    for i in a:
        
        if a.count(i) > 1:
            
            while a.count(i) > 1:
                
                a.remove(i)
                
                score = score + 1
            
        score = score + fr_club_mutual(i, person, \
                       person_to_clubs) + 1

                
        recommendations.append((i, score))
        
        score = 0
        
        a = get_clubs_of_friends(person_to_friends, person_to_clubs, person)
    
    if person in person_to_clubs:
        
        
        for i in mutual_club_implementor(person_to_friends, \
                                         person_to_clubs, person):
            
            
            if i not in clubs_to_score:
                
                clubs_to_score[i] = [1]
                
            else:
                
                while s < len(mutual_club_implementor(person_to_friends, \
                                         person_to_clubs, person)[i]):
                    
                    clubs_to_score[i].append(1)
                    
                    s = s + 1
                            
    for i in clubs_to_score:
        
        recommendations.append((i, len(clubs_to_score[i])))
    
    
    recommendations.sort()
        
    
    return bubble_down(recommendations)

# +COMPLETE

        
if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
