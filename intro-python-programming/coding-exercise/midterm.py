def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    frequency_dict = {}
    for tweet in tweet_list:
        retweet_start_indices = [i for i in range(len(tweet)) if tweet.startswith('RT', i)]
        if (len(retweet_start_indices) == 0):
            continue
        for index in retweet_start_indices:
            i = index + 4 
            username = []
            while(tweet[i] != ":"):
                username.append(tweet[i])
                i += 1
            username_str = "".join(username)

            if username_str not in frequency_dict.keys():
                frequency_dict[username_str] = 1
            else:
                frequency_dict[username_str] += 1
    # write code here and update return statement with your dictionary
    return frequency_dict

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    
    ans = ""
    curr_row = top
    while curr_row < bottom:
        curr_col = left
        row_list = ['-' for i in range(right - left)]
        deposits_in_row = [d for d in deposits if d[0] == curr_row]
        while curr_col < right:
            for d in deposits_in_row:
                if curr_col == d[1]:
                    row_list[curr_col - left] = 'X'
            curr_col += 1
        curr_row += 1
        row_str = "".join(row_list) + "\n"
        ans += row_str

    return ans

def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
   # pass # delete this statement before entering your code!
    total_tons = 0
    for d in deposits:
        row = d[0]
        col = d[1]
        tons = d[2]
        if row >= top and row < bottom and col >= left and col < right:
            total_tons += tons
    return total_tons


def birthday_original(dates_list):
    count = 0

    for person_a in dates_list:
        for person_b in dates_list:
            # Make sure we have different people        
            if person_a is person_b:
                continue

            # Check both month and day
            if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
                count += 1
                
    # We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:          
    return count//2

def birthday_count(dates_list):
    
    """Returns the total number of birthday pairs in the dates_list"""
    # dictionary_birthdays = {(birthday): count}
    bday_dict = {}
    bday_pairs = 0
    for date in dates_list:
        bday = (date[0], date[1])
        if bday not in bday_dict.keys():
            bday_dict[bday] = 1 # A new birthday
        else: # We've seen this birthday before
            bday_dict[bday] += 1
    
    for date in bday_dict.keys():
        bday_count = bday_dict[date]
        if bday_count > 1:
            bday_pairs += (bday_count)*(bday_count - 1) / 2
                               
    return int(bday_pairs)