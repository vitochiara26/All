full_dot = '●'
empty_dot = '○'

def create_character(name,stre,inte,char):

    if not isinstance(name,str) :
        return 'The character name should be a string'
    if name == "" :
        return 'The character should have a name'
    if len(name) > 10 :
        return 'The character name is too long'
    if name.find(" ") > 0 :
        return 'The character name should not contain spaces'
    if not isinstance(stre,int) or not isinstance(inte,int) or not isinstance(char,int):
        return 'All stats should be integers'
    if stre < 1 or inte < 1 or char < 1:
        return 'All stats should be no less than 1'
    if stre > 4 or inte > 4 or char > 4:
        return 'All stats should be no more than 4'
    if (stre + inte + char) != 7:
        return 'The character should start with 7 points'
    print(f"{name}\nSTR {full_dot*stre + empty_dot*(10-stre)}\nINT {full_dot*inte + empty_dot*(10-inte)}\nCHA {full_dot*char + empty_dot*(10-char)}")

create_character('ren',4,2,1)
create_character('Victor',3,2,2)
create_character('Daniela',3,3,1)