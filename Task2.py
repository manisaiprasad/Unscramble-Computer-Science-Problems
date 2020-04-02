"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def main():
    phonenumbers =dict()
    
    #creating dict with phone numbers as key and call time as values
    for call in calls:
        for call_element in [0, 1]:
            phonenumbers[call[call_element]] = int(call[3])

    max_call_time = 0
    max_telephone_num = ''
    # print(phonenumbers)

    for number in phonenumbers:
        if phonenumbers[number] >= max_call_time:
            max_call_time = phonenumbers[number]
            max_phone_num = number

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_phone_num,max_call_time))


if __name__ == '__main__':
    main()
    
