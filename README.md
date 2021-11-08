# turtle-fibonacci
fibonacci spirals and "art" using python turtle <br>
output files are in eps format, open with GIMP to see results <br>
Tell Jing Peng and Rayner I said hi :) <br>
Please only refer to Fibo_Final_Ver.py <br>
To see the individual fibonacci spirals, go to line 147 and delete items in the list e.g. fibo([t1], 42, 800, 800) <br>
To create your own, delte everything after line 54 <br>

*everything in {} means to use your own names <br>
syntax works as such: <br>

# 1. create your turtle <br>
{turtle_name} = Turtle() <br>
{turtle_name}.shape("turtle") #note that only first line is needed. other shapes include “arrow”, “turtle”, “circle”, “square”, “triangle”, "classic” <br>
{turtle_name}.speed("fastest") #turtle speeds can be set from 1(slowest) to 10(fastest) speed(0) is actually the fastest which turns off animations and makes turtle go brrrr <br>

# 1a. set starting position (not required) <br>
{turtle_name}.penup() <br>
{turtle_name}.goto({pos_x}, {pos_y}) #turle starts at 0, 0 is nothing is defined <br>
{turtle_name}.showturtle()  <br>
{turtle_name}.pendown() <br>

# 2. define turtle and other stuff <br>
#turtle_name, function, angle_start, angle_rotate, size, rescale, colour_start, colour_final <br>
{turtle_items} = ({turtle_name}, square, {angle_start}, 10, {size}, 0.96, {colour_start}, {colour_final}) <br>
#try not to change function, angle_rotate and rescale too much as these settings help to make it look like a fibonacci spiral <br>
#colour_start and colour_final should be a tuple with rgb values e.g. (255, 255, 255). It creates a colour gradient with the outside being colour_start and inside being coulour_final <br>

# 3. draw it! <br>
fibo({list of turtle_items}, {amount_of spirals}, {screen_width}, {screen_height}) <br>
#watch the turtles draw!v <br>

# 3a. make turtle go bye bye (not required) <br>
{turtle_name}.hideturtle() <br>
this hides the cursor <br>

# 4. save <br>
ts = turtle.getscreen() <br>
ts.getcanvas().postscript(file = "{filename}.eps") <br>
#saves output file <br>
#open in GIMP to see image <br>

# 5. Run everything :) <br>