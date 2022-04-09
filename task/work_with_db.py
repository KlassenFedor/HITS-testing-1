from main import formula
from SQLite_Integration import new_connection, cur


def insert_value(number):  # adding new answer in db
    try:
        answer = formula(number)
    except Exception:
        return "wrong data"
    if check_if_same_answer_exists(number):
        return "Successfully"
    else:
        try:
            cur.execute("""INSERT INTO answers(input_number, value) 
            VALUES(?, ?);""", (number, answer,))
            new_connection.commit()
            return "Successfully"
        except Exception:
            return "Unexpected error during adding data in database"


def check_if_same_answer_exists(answer):  # checking if the same answer already exists
    if type(answer) != int:
        raise ValueError
    try:
        cur.execute("SELECT * FROM answers WHERE input_number = answer;")
        one_result = cur.fetchone()
    except Exception:
        return False
    if len(one_result) == 0:
        return False
    return True


def get_value(number):  # get existing answer from db
    if type(number) != int:
        raise ValueError
    try:
        cur.execute("SELECT * FROM answers WHERE input_number = ?;", (number,))
        result = cur.fetchone()
    except Exception:
        return "Unexpected error during receiving data from database"
    if result is None:
        return "Result for this number doesn't exists now"
    else:
        return result
