from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
current_date = get_current_date()
print(current_date)