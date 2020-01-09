

django Temlplates

# django Translations

** [Official](https://docs.djangoproject.com/en/1.10/topics/i18n/translation/#gettext-on-windows) documents.**

使用以下代码引用gettext, 然后用 `python manage.py makemessages -l es` 或者 -l <lanaugage code>生成相关的 po文件来翻译，翻译后 用 `django-admin compilemessages`编译使用

     from django.utils.translation import ugettext
     from django.http import HttpResponse

     def my_view(request):
         output = ugettext("Welcome to my site.")
         return HttpResponse(output)


**Or use gettext need tools below :**

http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/gettext-tools-0.17.zip
http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/gettext-runtime-0.17-1.zip

**It should be made clear in the docs that gettext is a third party tool.**

1. Win32 users need to dowload 3 zip files from ​[http://sourceforge.net/projects/gettext](http://sourceforge.net/projects/gettext) :

    - gettext-runtime-X.bin.woe32.zip
    - gettext-tools-X.bin.woe32.zip
    - libiconv-X.bin.woe32.zip

2. extract the 3 files in the same folder ( ie C:\Program Files\gettext-utils )
3. Update the system PATH :

Control Panel > System > Advanced > Environment Variables
In the "System variables" list, click "Path", click "Edit"
Add ";C:\Program Files\gettext-utils\bin" at the end of the "Variable value"


## Setup Translation in Django

1. Make LOCALE_PATHS directory and add to settings.py

In your Base Directory of your project, where manage.py lives, create a directory called locale. Now in settings.py add the following tuple:

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, "locale"),
    )

Now you have gettext installed and the LOCALE_PATHS set, let's make our first translation file.

    python manage.py makemessages -l es

python manage.py and django-admin.py are interchangable if manage.py is present.

6. Run makemessages again.

        python manage.py makemessages -l es

7. Complie messages:

        python manage.py compilemessages

8. Activate test in a view:

        from django.utils import translation
        from django.utils.translation import ugettext as _

        def home(request):
             title = _("Welcome")
             if 'lang' in request.GET:
                   translation.activate(request.GET.get('lang'))
             return render(request, 'home.html', {"title": title})
         