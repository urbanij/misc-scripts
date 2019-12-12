Simulation of electric field wave @ interface with a different medium


![Alt Text](./media/cosine.gif)

![Alt Text](./media/gaussian.gif)

![Alt Text](./media/rect.gif)



### Running

(Python3.7 required)

```sh
pipenv shell
pipenv sync
```

Python interactive shell example:
```python
>>> from wave import *

>>> f_0 = 1.8e9 # [Hz]

>>> E_0 = 10.0  # [V]

>>> free_space = Medium(ε_r=1, μ_r=1, σ=0)

>>> medium2 = Medium(ε_r=5, μ_r=3, σ=.04)

>>> wave = Sine(f=f_0, A=E_0)

>>> wave.add_mediums(medium1=free_space, medium2=medium2)

>>> wave.show()
Save plot animation? (y/[n])? n

>>> wave.print_data()

U_1 := σ_1/(ω*ε_0*ε_r_1) = 0  ==> medium 1 is an Insulator
U_2 := σ_2/(ω*ε_0*ε_r_2) = 7.074e-13  ==> medium 2 is an Insulator
μ_eq_1 = 1.257e-06
μ_eq_2 = 3.77e-06
ε_eq_1 = 8.854e-12
ε_eq_2 = 4.427e-11-3.537e-12j
ζ_eq_1 = 376.7
ζ_eq_2 = 291.1+11.61j
k_1 = 37.73
k_2 = 146.2-5.832j
Γ_e = -0.1278+0.01961j = 0.1293 ∠ 2.989
τ_e = 0.8722+0.01961j = 0.8724 ∠ 0.02248
δ = 0.1715
S_i = 0.1327
S_t = 0.1305 = 98.33% S_i

>>> 
```

or just run:
```sh
python main.py
```

