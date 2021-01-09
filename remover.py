from canvasapi import Canvas
from canvasapi.exceptions import Unauthorized

with open('api_credentials.txt') as f:
    API_URL, API_KEY = f.read().strip().splitlines()

canvas = Canvas(API_URL, API_KEY)

def delete_all_events(*context_codes):
    context_codes = list(context_codes)
    for i, context_code in enumerate(context_codes):
        if str(context_code).isdigit():
            context_codes[i] = 'course_{}'.format(context_code)

    for event in canvas.get_calendar_events(context_codes=context_codes, all_events=True):
        event.delete()
        print('Deleted', event.__str__())

while __name__ == '__main__':
    prompt = input('Enter context codes separated by spaces:\n')
    prompt = prompt.split()
    try:
        delete_all_events(*prompt)
    except Unauthorized:
        if len(prompt) > 1:
            print("Either one or more of the context codes you entered is invalid or you don't have valid API credentials for it.\n")
        else:
            print(
                "Either the context code you entered is invalid or you don't have valid API credentials for it.\n")


