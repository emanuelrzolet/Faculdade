from setuptools import setup

def search4vowel (phrase: str) -> set:
    """_summary_

    Args:
        phrase (str): Word to be converted to a set

    Returns:
        set: Returns a set with vowels
    """
    return set ('aeiou').intersection(set(phrase))

def search4letters(phrase: str, letters: str = 'aeiou'):
    """_summary_

    Args:
        phrase (str): _description_
        letters (str, optional): _description_. Defaults to 'aeiou'.

    Returns:

        _type_: _description_
    """
    return set(letters).intersection(set(phrase))
#setup(name='vsearch',version='1.0',author='Emanuel Rosa Zolet',py_modules=['vsearch'],author_email='emanuelzolet1@gmail.com',description='First toll for python',)