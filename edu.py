import datetime as dt
def log_attempt(attempt, value_at_index, hint):
    with open("search_log.csv", "a") as f:
        f.write(f",{dt.datetime.now()},attempt:{attempt},value:{value_at_index},result:{hint}")

log_attempt(1, 28, "greater_then_choice")