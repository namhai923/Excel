import sys
import pandas as pd

def to_list(file_name):
    df = pd.read_excel(file_name)
    phone_list = df['SO DT'].values.tolist()
    return phone_list

def to_file(phone_list):
    with open("PhoneNumber.txt","w",encoding="utf-8") as text_file:
        for phone_number in phone_list:
            text_file.write(str(phone_number) + "\n")

def is_int(char):
    try: 
        int(char)
        return True
    except ValueError:
        return False

def Delete(phone_list):
    phone_number = []
    for Phone in phone_list:
        phone_array = list(str(Phone))
        x = 0
        while x < len(phone_array):
            if is_int(phone_array[x]) == False and phone_array[x] != '-':
                phone_array.remove(phone_array[x])
                x += -1
            x += 1
        phone_number.append(''.join(phone_array))
    return phone_number

def Mode(Mode, phone_list):
    phone_number = []
    for Phone in phone_list:
        changed_number = []
        phone_array = Phone.split('-')
        for Number in phone_array:
            if len(Number) > 12 or len(Number) < 9:
                Number = '' 
            elif len(Number) >= (len(Mode)-1):
                Number = Number.replace(Number[:(len(Mode)-1)],Mode[-(len(Mode)-1):],1)
            changed_number.append(Number+'-')
        changed_number = ''.join(changed_number)
        changed_number = changed_number[:-1]
        if len(changed_number) > 0:
            if changed_number[len(changed_number) - 1] == '-':
                changed_number = changed_number[:-1]
        phone_number.append(changed_number)
    return phone_number


def main():
    phone_list = to_list(sys.argv[1])
    phone_list = Delete(phone_list)
    phone_list = Mode(sys.argv[2],phone_list)
    to_file(phone_list)
    
if __name__ == '__main__':
    main()