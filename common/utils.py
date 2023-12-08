from django.urls import reverse


def get_knox_auth_urls():
    login_urls = reverse('knox_login')
    logout_urls = reverse('knox_login')
    logoutall_urls = reverse('konx_logout_all')

    return {

        'login_urls': login_urls,
        'logout_urls': logout_urls,
        'logoutall_urls': logoutall_urls,

    }