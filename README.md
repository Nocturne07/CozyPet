# 🐾 CozyPet
This project was developed for the **COMP9001 Final Project**.  
CozyPet is a simple yet engaging command-line game where players can raise and care for a virtual pet. Choose from a variety of animals like a dog, cat, rabbit, chipmunk, or raccoon. Keep your pet alive and happy by feeding it, playing with it, and handling unexpected events.

---

# 🎮 Features

- Choose from 5 species: `Dog`, `Cat`, `Rabbit`, `Chipmunk`, `Raccoon`
- Feed your pet with different food: `kibble`, `tin`, `salmon`, or `medicine`
- Play with fun toys: `ball`, `laser pointer`, `squeaky toy`
- Random events (illness, dreams, mood swings, and more)
- Track pet stats: **Health**, **Hunger**, **Happiness**, **Mood**（0～100）
- Pet can die or run away if not treated well

---

# 📖 Game Props Description
## 🍽️ Edible Items
| Item Name    | Effect                   |
| ------------ | ------------------------ |
| **kibble**   | +30 Hunger.              |
| **tin**      | +20 Hunger, +5 Mood.     |
| **salmon**   | +15 Hunger, +10 Mood.    |
| **medicine** | +25 Health, -10 Hunger.  |

## 🧸 Toys
| Toy Name          | Effect                             |
| ----------------- | -----------------------------------|
| **ball**          | +10 Happiness, -10 Hunger.         |
| **laser pointer** | +15 Mood, -5 Health, -10 Hunger.   |
| **squeaky toy**   | +5 Happiness, +5 Mood -10 Hunger.  |


---

# 🚀 How to Run

1. Make sure Python 3 is installed on your machine.
2. Download this repository.
3. Run the game:

```bash
python3 main.py
