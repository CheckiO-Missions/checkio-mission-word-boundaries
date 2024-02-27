"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [2, 'a b c'],
            "answer": 'b',
        },
        {
            "input": [8, '+ - * / ( ) = 0'],
            "answer": '(',
        },
        {
            "input": [12, 'How do you do?'],
            "answer": 'do?',
        },
        {
            "input": [6, 'This is a very strange test...'],
            "answer": 'is',
        },
        {
            "input": [0, '!!! What !!!'],
            "answer": '!!!',
        },
        {
            "input": [14, 'test test ERROR'],
            "answer": 'ERROR',
        },
        {
            "input": [1, 'o o o!!!'],
            "answer": None,
        }
    ],
    "Extra": [
        {
            "input": [8, 'Aaaaaaaaaaaaaaaaa!'],
            "answer": 'Aaaaaaaaaaaaaaaaa!',
        },
        {
            "input": [20, 'This_is_a_very_long_word'],
            "answer": 'This_is_a_very_long_word',
        },
        {
            "input": [0, '___ +++ ___ === ???'],
            "answer": '___',
        },
        {
            "input": [1000, 'averyshortword'],
            "answer": None,
        },
        {
            "input": [100500, 'error'],
            "answer": None,
        },
        {
            "input": [4, 'qwer ty'],
            "answer": None,
        }
    ]
}
