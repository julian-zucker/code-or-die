"""Functions related to team management"""

from database.key_access import get_civ, set_civ_key, civ_systems, get_civ_info


def set_token_for_team(db, old_key, new_key):
    """Sets the token for a team.

    :param db: the database to update
    :param old_key: the old key for the civilization
    :param new_key: the new key for the civilization
    :return: True, if a token was updated
    """
    old_civ_id = get_civ(db, old_key)
    if old_civ_id is None:
        return False
    return set_civ_key(db, old_civ_id, new_key)


def systems_for_team(db, key):
    """What systems does the team with the given key own?

    :param db: the database to check
    :param key: the key of the civilization to check
    :return: the list of systems that the team owns
    """
    result = civ_systems(db, key)
    if not result:
        return None
    result.sort()
    return result

def civ_info(db, key):
    """Returns info on the civilization with the given key, including their homeworld

    :param db: the database to use
    :param key: the key of the civilizatino to check3
    :return: information about the civ
    """
    return get_civ_info(db, key)