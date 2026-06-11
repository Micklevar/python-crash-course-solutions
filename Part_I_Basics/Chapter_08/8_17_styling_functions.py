def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything 
    we know about a user.

        Args:
            first (str): first name of user.
            last (str): Last name of user.

        Return:
            Dict
    """

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info