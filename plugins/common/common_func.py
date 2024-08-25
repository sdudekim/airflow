def get_sftp():
    print("sftp starting!!")


def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 옵션들: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 옵션들: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email:
        print(email)
    if phone:
        print(phone)