import turtle
import time

# Atur layar
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Happy Birthday Animation")

# Membuat pena
pen = turtle.Turtle()
pen.color("darkblue")
pen.width(3)
pen.speed(2)

# Fungsi menggambar huruf 'H'
def draw_H(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 50)  # Garis vertikal kiri
    pen.penup()
    pen.goto(x, y - 25)
    pen.pendown()
    pen.goto(x + 20, y - 25)  # Garis horizontal tengah
    pen.penup()
    pen.goto(x + 30, y)
    pen.pendown()
    pen.goto(x + 30, y - 50)  # Garis vertikal kanan

# Fungsi menggambar huruf 'A'
def draw_A(x, y):
    pen.penup()
    pen.goto(x, y - 50)
    pen.pendown()
    pen.goto(x + 15, y)  # Garis diagonal kiri
    pen.goto(x + 30, y - 50)  # Garis diagonal kanan
    pen.penup()
    pen.goto(x + 7, y - 25)
    pen.pendown()
    pen.goto(x + 23, y - 25)  # Garis horizontal tengah

# Fungsi menggambar huruf 'P'
def draw_P(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 50)  # Garis vertikal
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(-15, 180)  # Lengkungan huruf P (setengah lingkaran)

# Fungsi menggambar huruf 'Y'
def draw_Y(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + 15, y - 25)  # Garis diagonal kiri
    pen.goto(x + 15, y - 50)  # Garis vertikal bawah
    pen.penup()
    pen.goto(x + 15, y - 25)
    pen.pendown()
    pen.goto(x + 30, y)  # Garis diagonal kanan

# Fungsi menggambar huruf 'B'
def draw_B(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 50)  # Garis vertikal
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(-15, 180)  # Lengkungan atas
    pen.penup()
    pen.goto(x, y - 25)
    pen.pendown()
    pen.circle(-15, 180)  # Lengkungan bawah

# Fungsi menggambar huruf 'I'
def draw_I(x, y):
    pen.penup()
    pen.goto(x + 15, y)
    pen.pendown()
    pen.goto(x + 15, y - 50)  # Garis vertikal

# Fungsi menggambar huruf 'R'
def draw_R(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 50)  # Garis vertikal
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(-15, 180)  # Lengkungan atas
    pen.penup()
    pen.goto(x, y - 25)
    pen.pendown()
    pen.goto(x + 30, y - 50)  # Garis diagonal bawah

# Fungsi menggambar huruf 'T'
def draw_T(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + 30, y)  # Garis horizontal atas
    pen.penup()
    pen.goto(x + 15, y)
    pen.pendown()
    pen.goto(x + 15, y - 50)  # Garis vertikal

# Fungsi menggambar huruf 'D'
def draw_D(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y - 50)  # Garis vertikal
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.circle(-25, 180)  # Lengkungan

# Fungsi menulis kata "Happy Birthday"
def write_happy_birthday():
    x, y = -200, 100  # Posisi awal
    draw_H(x, y)
    draw_A(x + 50, y)
    draw_P(x + 100, y)
    draw_P(x + 150, y)
    draw_Y(x + 200, y)

    # Beri jeda sebelum "Birthday"
    time.sleep(1)

    # Posisi baru untuk "Birthday"
    x, y = -200, 0
    draw_B(x, y)
    draw_I(x + 50, y)
    draw_R(x + 100, y)
    draw_T(x + 150, y)
    draw_H(x + 200, y)
    draw_D(x + 250, y)
    draw_A(x + 300, y)
    draw_Y(x + 350, y)

# Menampilkan animasi menulis "Happy Birthday"
pen.hideturtle()
write_happy_birthday()

# Menutup layar ketika selesai
screen.mainloop()
