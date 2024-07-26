from datetime import datetime

date_format = "%d-%m-%Y"

CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_deafult=False):
    date_string = input(prompt)
    if allow_deafult and not date_string:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_deafult)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount most be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()



def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()



def get_description():
    return input("Enter a description (optional): ")