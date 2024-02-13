import webSities

def main():
    response = input('Please enter website u want').strip().capitalize()
    if response == 'Facebook':
        webSities.get_facebook()
    elif response == 'Twitter':
        webSities.get_twitter()
    elif response == 'Google':
        webSities.get_google()
    elif response == 'Instagram':
        webSities.get_instagram()
    elif response == 'Asu':
        webSities.get_ASU()
    else:
        print("Unknown response")
    



if  __name__ == '__main__':
    main()