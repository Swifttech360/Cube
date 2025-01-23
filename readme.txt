OVERVIEW
  This is a program that gets a cube sidelength as a user input,
  then outputs the total surface area of the theoretical cube.

PSEUDOCODE
  Loop program until a "break" occurs.
  Get cube side length as a string.
  Print an exit message and break if the user inputs "end".
  Try to convert user input to floating point number.
  Restart loop if a Value Error occurs after sending a short error message.
  Restart loop if the user input is less than zero after sending a short error message.
  Calculate the surface area of the cube using the formula "sideLength² * 6"
  Initialize new value as "surfaceArea".
  Exclude the remainder if it's equal to zero.
  Print the cube's calculated surface area, along with the formula used to get it.
  Loop