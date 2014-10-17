HEROKU_APP = "benchmarks-server"

PYTHONS = ["python2.7", "python3.4", "pypy"]

APPS = ["loader",
  "benchmarks/bottle", "benchmarks/django", "benchmarks/falcon", "benchmarks/flask", "benchmarks/tornado",
  "benchmarks/wheezy", "benchmarks/fapws3",
]

PYTHONS_HEROKU = ["cpython2", "cpython3", "pypy"]
SERVERS = ["''", "uwsgi", "cherrypy", "waitress", "gunicorn", "eventlet", "gevent", "tornado", "meinheld",]
FRAMEWORKS = ["bottle", "django", "falcon"]


def colorize(text, color)
  color_codes = {
    :black    => 30,
    :red      => 31,
    :green    => 32,
    :yellow   => 33,
    :blue     => 34,
    :magenta  => 35,
    :cyan     => 36,
    :white    => 37
  }
  code = color_codes[color]
  if code == nil
    text
  else
    "\033[#{code}m#{text}\033[0m"
  end
end

def virtual_env(command, env="env")
  sh "source #{env}/bin/activate && #{command}"
end

def create_virtual_env(dir, python)
  sh "virtualenv #{dir} -p #{python}"
end

def run(command)
    sh "#{command} ; true" # ignore errors
end

def run4all(command)
  APPS.each { |app|
    puts colorize("On #{app}", :blue)
    sh "cd #{app} ; #{command} ; cd -"
  }
end

task :clean => [] do
end

task :clean_all => [] do
  run4all("rake clean")
end

task :prepare => [] do
  PYTHONS.each { |python|
    puts colorize("Prepare #{python}", :yellow)
    env = "env#{python.sub('python', '')}"
    create_virtual_env("#{env}", "python")
    virtual_env("pip install -r requirements.txt", "#{env}")
  }
end

task :prepare_all => [] do
  run4all("rake prepare")
end

# heroku labs:enable log-runtime-metrics
# heroku restart
# heroku plugins:install https://github.com/heroku/heroku-repo.git --app #{HEROKU_APP}
# heroku repo:rebuild -a benchmarks-server --app #{HEROKU_APP}

def update_config(server, python, framework)
  puts colorize("Update to #{server} #{python} #{framework}", :blue)
  File.open(".env", 'w') { |file| file.write("SERVER=#{server}") }
  sh "cp conf/runtime-#{python}.txt runtime.txt"
  sh "cp benchmarks/#{framework}/Procfile Procfile"
end

def deploy(server, python, framework)
  update_config(server, python, framework)
  puts colorize("Deploying: #{server} #{python} #{framework}", :blue)
  sh "heroku config:set SERVER=#{server} --app #{HEROKU_APP}"
  sh "git add ."
  sh "git commit --allow-empty -m 'benchmark #{python} #{framework}'"
  sh "git push heroku master -f"
  puts colorize("Deployed: #{server} #{python} #{framework}", :blue)
end

task :deploy => [] do
  # deploy("''", "cpython2", "bottle")
  # deploy("meinheld", "pypy", "bottle")
  # deploy("meinheld", "cpython2", "bottle")
  # deploy("meinheld", "cpython3", "bottle")
  # deploy("''", "cpython2", "django")
  # deploy("''", "pypy", "falcon")
  deploy("''", "pypy", "tornado")
end

task :update => [] do
  # update_config("meinheld", "pypy", "bottle")
  # update_config("''", "pypy", "falcon")
  # update_config("''", "pypy", "django")
  # update_config("''", "pypy", "wheezy")
  update_config("''", "pypy", "tornado")
  sh "foreman start"
end

task :push => [] do
  sh "git reset --soft 96e206efc953ca809beb1231b357048ccaea72b9"
  sh "git add -u ."
  sh "git commit --amend"
  sh "git push origin master -f"
end

task :default => [:prepare]