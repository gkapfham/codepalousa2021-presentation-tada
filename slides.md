---
theme: ./simple
class: text-center
highlighter: prism
colorSchema: light
download: true
preload: true
fonts:
  sans: IBM Plex Sans
  serif: IBM Plex
  mono: Fira Code
  italic: true
info: |
  ## CodepaLOUsa 2021
  CodepaLOUsa 2021
title: TaDa it's Magic
---

[//]: # (Slide Start {{{)

# TaDa it's Magic!

## Predicting the Performance of Programs through Automated Doubling Experiments

<div class="container my-5">
  &nbsp;
</div>

### Gregory M. Kapfhammer, Lancaster Wu, Enpu You

### CodepaLOUsa 2021

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# <em>Huh</em>, what is this about?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-4;
  }
</style>

<br>

<div v-click>

## Key Questions

> Can a tool **automatically predict** a program's performance? Is it possible to
> automatically estimate the **worst-case time complexity** of a program?

</div>

<br>

<div v-click>

## Intended Audience

> An **adventuresome** technology enthusiast who wants to explore how a new
> approach to performance evaluation can make their **programs faster**!

</div>

<div v-click>

<div class="flex row">

<uim-rocket class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Let's learn how to predict a function's performance!
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Why focus on Python programming?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-4;
  }
</style>

<br>

<div v-click>

## Prevalence of Python

> Python is consistently ranked as one of the **top programming languages**
> for web development, data science, machine learning, and general programming

</div>

<br>

<div v-click>

## Importance of Performance

> Programmers who create, say, **serverless functions** with AWS Lambda
> need to carefully **monitor** and **improve** the performance of these
> functions

</div>

<div v-click>

<div class="flex row">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Challenging about performance evaluation in Python?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<style>
  li {
  font-size: 34px;
  margin-bottom: 1px;
  }
</style>

<div class="flex row">

<uim-vector-square class="text-8xl ml-4 mt-12 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-4">
Analytical Evaluation
</div>

<div class="text-6xl text-true-gray-600 font-bold mt-16 mr-15">
<ul>
<li> Algorithm </li>
<li> Constructs </li>
<li> Growth </li>
</ul>
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-microscope class="text-9xl ml-4 mt-6 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-1">
Experimental Evaluation
</div>

<div class="text-8xl text-true-gray-600 font-bold mt-16 mr-14">
<ul>
<li> Program </li>
<li> Benchmark </li>
<li> Study </li>
</ul>
</div>

</div>

</v-clicks>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
What are the trade-offs of these two approaches?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="ml-8 grid grid-cols-2 gap-19 mt-3">
<div>

# Analytical

<style>
  li {
  font-size: 22px;
  margin-bottom: 10px;
  }
</style>

- Provides a clear means by which to compare functions
- Does not depend on the hardware or software configuration
- Yet, often requires precise mathematical reasoning skills

</div>

<div v-click>

<div>

# Experimental

- Must generate inputs to the program subject to analysis
- Must repeatedly run a program and collect performance data
- Only generally accessible to programmers if good tools exist

</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-scenery class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Analysis characterizes an algorithm as, say, O(n)
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-grid class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Experiments run program to collect performance data
</div>

</div>

</div>

[//]: # (Slide End }}})


---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
How to analytically evaluate a program's performance?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-repeat class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Commonly used growth functions
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-layer-group class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-5xl font-bold mt-8 ml-4">
Study program's code constructs
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# "Fast" Order of Growth Functions

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-17">

![Fast Order of Growth Functions](/fast-growth-functions.png)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# "Slow" Order of Growth Functions

<style>
  .constraint {
    width: 100%;
  }
</style>

<br>

<div class="constraint -mt-17">

![Slow Order of Growth Functions](/slow-growth-functions.png)

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Relationship between growth function and program's performance?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-check-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Slow growth functions → fast programs
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-exclamation-circle class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Fast growth functions → slow programs
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Analyzing the <code>add_digits</code> Function

<div class="ml-2 my-2">

```python {all|1|2|3-4|5|7-8|all}
def add_digits(digits: str) -> int:
    value = 0
    for digit in digits:
        value += int(digit)
    return value

sum_digits = add_digits("123")
print(sum_digits)
```

</div>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
What is worst-case time complexity of <code>add_digits</code>?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Analyzing the <code>factorial</code> Function

<div class="ml-2 my-2">

```python {all|1|2-3|4-5|7-8|all}
def factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

factorial_value = factorial(3)
print(factorial_value)
```

</div>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
What is worst-case time complexity of <code>factorial</code>?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Analyzing the <code>is_subset</code> Function

<div class="ml-2 my-2">

```python{all|1|2|4|5-7|8-9|all}
def is_subset(one: List, two: List) -> bool:
    for element_one in one:
        matched = False
        for element_two in two:
            if element_one == element_two:
                matched = True
                break
        if not matched:
            return False
    return True
```

</div>

<div v-click>

<div class="flex row -mt-1">

<mdi-help-box class="text-6xl ml-4 mt-0 text-blue-600" />

<div class="text-3xl font-bold mt-4 ml-4">
What is worst-case time complexity of <code>is_subset</code>?
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-5 ml-4 mb-4">
Run an experiment to get likely worst-case time complexity of program?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-chart class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
Bespoke auto-doubling experiment tool
</div>

</div>

</div>

<div v-click>

<div class="flex row mt-4">

<uim-rocket class="text-6xl ml-8 mt-6 text-blue-600" />

<div class="text-4xl font-bold mt-10 ml-4">
TaDa! auto-doubling for a Python function
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Doubling Experiment: Linear

<style>
  h2 {
    font-size: 42px;
    @apply text-orange-600 text-center mt-8 mb-4;
  }
</style>

## Double the size of the program's input

<div class="ml-0 grid grid-cols-2 gap-19 mt-1 -mb-3">

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<uim-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
14.98 seconds
</div>

</div>

</div>

<div v-click>

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<div class="flex row">

<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />
<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />

</div>

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
31.45 seconds
</div>

</div>

</div>

</div>

</div>

<div v-click>

## Doubling ratio is approximately 2

</div>

<div v-click>

<div class="flex row mt-6 ml-15">

<mdi-alert-octagram class="text-6xl ml-10 mt-0 text-blue-600" />

<div class="text-3xl font-bold mt-4 ml-4">
Likely worst-case time complexity is O(n)
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Doubling Experiment: Quadratic

<style>
  h2 {
    font-size: 42px;
    @apply text-orange-600 text-center mt-8 mb-4;
  }
</style>

## Double the size of the program's input

<div class="ml-0 grid grid-cols-2 gap-19 mt-1 -mb-3">

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<uim-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
12.63 seconds
</div>

</div>

</div>

<div v-click>

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<div class="flex row">

<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />
<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />

</div>

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
51.48 seconds
</div>

</div>

</div>

</div>

</div>

<div v-click>

## Doubling ratio is approximately 4

</div>

<div v-click>

<div class="flex row mt-6 ml-11">

<mdi-alert-octagram class="text-6xl ml-10 mt-0 text-blue-600" />

<div class="text-3xl font-bold mt-4 ml-4">
Likely worst-case time complexity is O(n^2)
</div>

</div>

</div>

[//]: # (Slide End }}})

[//]: # (Slide Start {{{)

---

# Doubling Experiment: Cubic

<style>
  h2 {
    font-size: 42px;
    @apply text-orange-600 text-center mt-8 mb-4;
  }
</style>

## Double the size of the program's input

<div class="ml-0 grid grid-cols-2 gap-19 mt-1 -mb-3">

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<uim-box class="text-6xl ml-8 mt-4 text-blue-600" />

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
11.23 seconds
</div>

</div>

</div>

<div v-click>

<div class="pb-2 border-2 mt-2 border-gray-800 border-opacity-80 rounded">

<div class="flex row">

<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />
<uim-box class="text-6xl ml-8 mt-6 text-blue-600" />

</div>

<div class="flex row">

<div>
<ic-twotone-watch-later class="text-6xl ml-8 mt-6 text-blue-600" />
</div>

<div class="ml-5 mt-10 text-4xl">
89.72 seconds
</div>

</div>

</div>

</div>

</div>

<div v-click>

## Doubling ratio is approximately 8

</div>

<div v-click>

<div class="flex row mt-6 ml-11">

<mdi-alert-octagram class="text-6xl ml-10 mt-0 text-blue-600" />

<div class="text-3xl font-bold mt-4 ml-4">
Likely worst-case time complexity is O(n^3)
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

<div class="flex row">

<div class="text-7xl text-orange-600 font-bold mt-1 ml-4 mb-1">
What are challenges with running automated doubling experiments?
</div>

</div>

<div v-click>

<div class="flex row">

<uim-exclamation-circle class="text-5xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Automatically generate inputs to the function
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-exclamation-circle class="text-5xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Determine when to stop running experiments
</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-exclamation-circle class="text-5xl ml-8 mt-6 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Establish a statistical confidence in the prediction
</div>

</div>

</div>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# TaDa! Runs a Doubling Experiment

<div class="flex row -mt-4">

<uim-repeat class="text-8xl ml-9 mt-8 text-orange-600" />

<div class="text-6xl text-true-gray-600 font-bold mt-8 ml-4">
Input is a Python function and configuration options
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-grid class="text-8xl ml-9 mt-8 text-orange-600" />

<div class="text-6xl text-true-gray-600 font-bold mt-8 ml-4">
Output is a data table and a performance prediction
</div>

</div>

</v-clicks>

<v-clicks>

<div class="flex row">

<uim-github class="text-8xl ml-9 mt-8 text-blue-600" />

<div class="text-5xl text-true-gray-600 font-bold mt-15 ml-4">
See <code>Tada-Project/tada</code> for details
</div>

</div>

</v-clicks>

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# Analyzing the <code>insertion_sort</code> Function

<div v-click>

<div class="ml-2 my-2">

```python
def insertion_sort(lst: list[int]) -> list[int]:
    for i in range(1, len(lst)):
        value = lst[i]
        pos = i
        while pos > 0 and value < lst[pos - 1]:
            lst[pos] = lst[pos - 1]
            pos -= 1
        lst[pos] = value
    return lst
```
</div>

</div>

<div v-click>

<div class="flex row mt-5">

<mdi-help-box class="text-6xl ml-4 mt-4 text-blue-600" />

<div class="text-3xl font-bold mt-8 ml-4">
Can TaDa! estimate worst-case of <code>insertion_sort</code>?
</div>

</div>

</div>

[//]: # (Slide End }}})
