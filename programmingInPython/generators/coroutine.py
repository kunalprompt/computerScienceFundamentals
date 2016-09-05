def coroutine(number=0):
    while True:
        try:
            input_value = (yield)
        except StopIteration as e:
            input_value = e
        print input_value

c = coroutine(10)

# jumping to yield statement so that it can receive messages
c.next()  # you can also use c.send(None)

# sending messages to coroutine
for i in range(1, 11):
    c.send(i)
c.close()
