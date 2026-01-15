# Different Approaches for Calculating Least Common Multiple (LCM)

In this project, I explored and implemented various methods to calculate the Least Common Multiple (LCM) of a set of numbers, ranging from built-in library functions to custom logic.

<br>

### `math-lcm.py`
This script utilizes the built-in `math.lcm` function. This function is powerful and efficient but is only available in **Python 3.9** or later.
* **Key tools:** `math.lcm`, `math.gcd`, and `functools.reduce`.

<br>

### `math-gcd.py`
In this version, I defined the LCM function manually while utilizing the `math.gcd` (Greatest Common Divisor) function. The calculation is based on the mathematical formula:
$LCM(a, b) = \frac{|a \cdot b|}{GCD(a, b)}$
* **Key tools:** `math.gcd` and `functools.reduce`.

<br>

### `just-reduce.py`
For this approach, I defined both the LCM and GCD functions from scratch. I implemented the **Euclidean Algorithm** to calculate the GCD.
* **Key tools:** `functools.reduce`, custom GCD (with recursion), and custom LCM.

<br>

### `copy-reduce.py`
In this script, I focused on understanding the fundamental logic behind the `reduce` function by reproducing its behavior manually.
* **Key tools:** Custom `reduce` implementation, custom LCM, and recursive GCD.

<br>

### `without-module.py`
In this final version, I calculated the LCM directly without importing any external modules or using the `reduce` function.
* **Key tools:** Recursive implementations for both LCM and GCD functions to handle multiple inputs.

<br>

### `ai_lab`
This directory contains experimental scripts and samples generated or inspired by AI tools. It serves as a testing ground for exploring AI-assisted coding and various machine learning logic patterns.
* **Key focus:** AI-driven code generation, logic testing, and experimental implementations. 
