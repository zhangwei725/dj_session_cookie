def user(request):
    username = request.session.get('username')
    is_login = True if username else False
    return {'user': {'is_login': is_login, 'username': username}}
