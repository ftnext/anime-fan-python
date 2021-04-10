import web

web.config.debug = False

urls = ("/count", "Count", "/reset", "Reset")

app = web.application(urls, locals())

session = web.session.Session(
    app, web.session.DiskStore("sessions"), initializer={"count": 0}
)


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


class Reset:
    def GET(self):
        session.kill()
        return "Reset"


if __name__ == "__main__":
    app.run()
