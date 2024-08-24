import json

def setup_data():
    messages_list = [['0', 'Liu', '欢迎留言！有什么建议或想说的话都可以写在这里哦~  注意文明！']]
    with open('leave_messages.json', 'w', encoding='utf-8') as f:
        json.dump(messages_list, f)
    
    times_dict = {}
    with open('check_out_times.json', 'w', encoding='utf-8') as f:
        json.dump(times_dict, f)
