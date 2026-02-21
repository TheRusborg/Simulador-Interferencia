## Interference simulator
### Objective
The main purpose of this program is to make an application that works with a built in simulation that calculates the diffraction pattern created by the interference of two waves that pass through two slits (recreating the Young double slit experiment).

---

### Implementation
For this program we've (...)

---

### Dependencies
In this project we used the following dependencies to implement the simulation.

|Python libraries|Custom libraries|Other|
|:---|:---|:---:|
|python -v 3.14.0 <br>- os<br>- sys<br>- time<br>- PyQt5<br>- numpy<br>- matplotlib|- create_plots<br>- create_sliders <br>(in progress)|(...)|

### Instructions of use
To use this program we provide the following altervatives:

1. Download the executable located in the dist directory (we're working on the windows version).

2. Download directly the zip folder of this repository, unzip it and execute the **main.py** on a python interpreter with a python version equal or higher than v.3.7.0

3. You can also compile the code yourself using the module **pyinstaller**.

```
pip install pyinstaller
```
Fisrt, change the directory to the folder where you downloaded the project, for example:

```
cd User/Downloads/Simulador-interferencia
```
Next, execute the following command:

```
pyinstaller -F main.py
```