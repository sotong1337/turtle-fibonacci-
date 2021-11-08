# turtle-fibonacci
 fibonacci spirals and "art" using python turtle<br>
 output files are in eps format, open with GIMP to see results
 Tell Jing Peng and Rayner I said hi :)
 To see the individual fibonacci spirals, go to line 147 and delete items in the list e.g. fibo([t1], 42, 800, 800)
 To create your own, delte everything after line 54

 *everything in {} means to use your own names
 syntax works as such:

1. create your turtle
 {turtle_name} = Turtle()
 {turtle_name}.shape("turtle") #note that only first line is needed. other shapes include “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
 {turtle_name}.speed("fastest") #turtle speeds can be set from 1(slowest) to 10(fastest) speed(0) is actually the fastest which turns off animations and makes turtle go brrrr

1a. set starting position (not required)
 {turtle_name}.penup()
 {turtle_name}.goto({pos_x}, {pos_y}) #turle starts at 0, 0 is nothing is defined
 {turtle_name}.showturtle()          
 {turtle_name}.pendown()

2. define turtle and other stuff
 #turtle_name, function, angle_start, angle_rotate, size, rescale, colour_start, colour_final
 {turtle_items} = ({turtle_name}, square, {angle_start}, 10, {size}, 0.96, {colour_start}, {colour_final})
 #try not to change function, angle_rotate and rescale too much as these settings help to make it look like a fibonacci spiral
 #colour_start and colour_final should be a tuple with rgb values e.g. (255, 255, 255). It creates a colour gradient with the outside being colour_start and inside being coulour_final

3. draw it!
 fibo({list of turtle_items}, {amount_of spirals}, {screen_width}, {screen_height})
 #watch the turtles draw!

3a. make turtle go bye bye (not required)
 {turtle_name}.hideturtle()
 this hides the cursor

4. save
 ts = turtle.getscreen()
 ts.getcanvas().postscript(file = "{filename}.eps")
 #saves output file
 #open in GIMP to see image

5. Run everything :)