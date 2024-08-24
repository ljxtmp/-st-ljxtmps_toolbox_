import json

def read_data():
    with open('leave_messages.json', 'r', encoding='utf-8') as f:
        messages_list = json.load(f)
    
    with open('check_out_times.json', 'r', encoding='utf-8') as f:
        times_dict = json.load(f)

    return (messages_list, times_dict)
