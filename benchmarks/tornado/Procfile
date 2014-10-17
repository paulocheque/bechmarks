web: sh -c "NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python benchmarks/tornado/run.py"

#web: gunicorn -k tornado --bind=0.0.0.0:$PORT app
#web: newrelic-admin run-program gunicorn -k tornado --bind=0.0.0.0:$PORT tornado/run
#web: newrelic-admin run-program uwsgi --http-socket :$PORT --wsgi-file tornado/run.py