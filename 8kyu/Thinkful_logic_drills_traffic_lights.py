"""

Thinkful - Logic Drills: Traffic light(8Kyu)
https://www.codewars.com/kata/58649884a1659ed6cb000072

You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, update_light('green') should return 'yellow'.
"""
def update_light(current):
    lights = ["green", "yellow", "red"]
    return lights[lights.index(current) + 1] if current != "red" else "green"
