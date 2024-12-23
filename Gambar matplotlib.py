import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data teks
text = "Happy Birthday!"
text_displayed = ""
index = 0

# Membuat figure
fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(0, 1)
text_obj = ax.text(0.5, 0.5, "", fontsize=20, ha="center")

# Fungsi update animasi
def update(frame):
    global text_displayed, index
    if index < len(text):
        text_displayed += text[index]
        index += 1
    text_obj.set_text(text_displayed)
    return text_obj,

# Membuat animasi
ani = FuncAnimation(fig, update, frames=len(text), interval=300, blit=True)

# Menampilkan animasi
plt.axis("off")
plt.show()
