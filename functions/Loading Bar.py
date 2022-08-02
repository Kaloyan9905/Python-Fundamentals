def loading_bar():
    if num == 10:
        print(f'10% [%.........]')
        print(f'Still loading...')
    elif num == 20:
        print(f'20% [%%........]')
        print(f'Still loading...')
    elif num == 30:
        print(f'30% [%%%.......]')
        print(f'Still loading...')
    elif num == 40:
        print(f'40% [%%%%......]')
        print(f'Still loading...')
    elif num == 50:
        print(f'50% [%%%%%.....]')
        print(f'Still loading...')
    elif num == 60:
        print(f'60% [%%%%%%....]')
        print(f'Still loading...')
    elif num == 70:
        print(f'70% [%%%%%%%...]')
        print(f'Still loading...')
    elif num == 80:
        print(f'80% [%%%%%%%%..]')
        print(f'Still loading...')
    elif num == 90:
        print(f'90% [%%%%%%%%%.]')
        print(f'Still loading...')
    elif num == 100:
        print(f'100% Complete!')
        print(f'[%%%%%%%%%%]')


num = int(input())
loading_bar()
