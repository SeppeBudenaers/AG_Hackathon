from bottle import route, run

@route('/')
def hello():
    return "Hello, World!"

run(host='localhost', port=8080)







# t = Body_Temprature(TimeStamp = datetime.datetime.now(), Temprature = 37.5)
# session.add(t)
# r = Body_Temprature(TimeStamp = datetime.datetime.now(), Temprature = 37.5)
# session.add(r)
# session.commit()

# z = session.query(Body_Temprature).all()
# print(z[0].Temprature)