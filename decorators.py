from datetime import datetime
from DATA import ID, RESULT

def log_decorator(func):
    def write_log(*args, **kwargs):
        global ID
        func_result = func(*args, **kwargs)
        date = datetime.now().date().timetuple()
        time = datetime.now().time()
        result = {
            'id' : ID,
            'date' : f'{date[0]} - {date[1]} - {date[2]}',
            'time' : f'{time.hour} часов {time.minute} минут',
            'function_name' : func.__name__,
            'args' : args,
            'kwargs' : kwargs,
            'result' : func_result
        }
        ID += 1
        RESULT.append(result)
        RESULT.append('\n')
        with open('logs.txt', 'w', encoding='utf-8') as document:
            for el in RESULT:
                document.write(str(el))
        # pprint(result)
        return result
    return write_log