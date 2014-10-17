from locust import HttpLocust, TaskSet


def short_message(l):
    l.client.get("/short-message")


def average_message(l):
    l.client.get("/average-message")


def long_message(l):
    l.client.get("/long-message")


def slow_request(l):
    l.client.get("/slow-request")


def html_request(l):
    l.client.get("/")


class Benchmark1(TaskSet):
    tasks = {short_message: 1}


class Benchmark(HttpLocust):
    task_set = Benchmark1
    host = 'http://benchmarks-server.herokuapp.com'
    min_wait=5000
    max_wait=9000
