# imports
from module.instapy import InstaPy
from module.instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    session.set_action_delays(enabled=True, unfollow=120, randomize=True, random_range_from=90, random_range_to=140)
    session.set_quota_supervisor(enabled=True,
                                 peak_follows_daily=560,
                                 peak_follows_hourly=56,
                                 peak_unfollows_hourly=30,
                                 peak_unfollows_daily=300,
                                 sleep_after=["unfollows_h", "unfollows_d"],
                                 stochastic_flow=True)
# activity
    session.unfollow_users(amount=100, nonFollowers=True, style="RANDOM", unfollow_after=5 * 22 * 60 * 60, sleep_delay=500)
