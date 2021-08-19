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

## Predicting the Performance of Functions through Automated Doubling Experiments

<div class="container my-5">
  &nbsp;
</div>

### Gregory M. Kapfhammer

### CodepaLOUsa 2021

[//]: # (Slide End }}})

---

[//]: # (Slide Start {{{)

# <em>Okay</em>, what is this about?

<style>
  h2 {
    font-size: 36px;
    @apply text-orange-600 mb-4;
  }
</style>

<br>

<div v-click>

## Key Questions

> Can a tool **automatically predict** a function's performance? Is it possible to
> automatically estimate the **worst-case time complexity** of a function?

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

> Programmers who create serverless functions with AWS Lambda need to carefully
> **monitor** and **improve** the performance of the functions

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
  font-size: 26px;
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
<li> algorithm </li>
<li> constructs </li>
<li> growth </li>
</ul>
</div>

</div>

<v-clicks>

<div class="flex row">

<uim-microscope class="text-9xl ml-4 mt-6 text-orange-600" />

<div class="text-7xl text-true-gray-600 font-bold mt-8 ml-1">
Experimental Evaluation
</div>

<div class="text-8xl text-true-gray-600 font-bold mt-16 mr-19">
<ul>
<li> hardware </li>
<li> software </li>
<li> execute </li>
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

- Must generate inputs to the function subject to analysis
- Must repeatedly run a function and collect performance data
- Yet, generally accessible to programmers if good tools exist

</div>

</div>

</div>

<div v-click>

<div class="flex row">

<uim-scenery class="text-6xl ml-8 mt-5 text-blue-600" />

<div class="text-3xl font-bold mt-9 ml-4">
Analytical characterizes an algorithm as, say, O(n)
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

