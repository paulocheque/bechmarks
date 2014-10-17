


    virtualenv env -p python2.7.8
    virtualenv env -p python3.4.2
    virtualenv env -p pypy
    virtualenv env -p pypy3

    source env/bin/activate

    pip install -r requirements.txt

    run_gunicorn.sh
    run_nginx.sh
    run_waitress.sh
    run_bjoern.sh
    run_uwsgi.sh
    run_meinheld.sh
    run_gunicorn_meinheld.sh