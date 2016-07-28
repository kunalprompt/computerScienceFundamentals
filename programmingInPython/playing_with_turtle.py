"""
Turtle is a API in Python Standard Library. It can be used to draw shapes.
"""
from turtle import Screen, Turtle


def main():
	# creating a window
	window = Screen()
	# window.bgcolor("orange")

	remo = Turtle()
	remo.shape("turtle")
	remo.color("green")
	remo.speed(50)

	for i in range(36):
		remo.circle(100)
		remo.left(10)

	remo.color("red")

	for i in range(36):
		remo.circle(80)
		remo.left(10)

	remo.color("yellow")

	for i in range(36):
		remo.circle(60)
		remo.left(10)


	window.exitonclick()

if __name__ == '__main__':
	main()


