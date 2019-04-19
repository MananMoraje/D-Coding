function jump(){
    Runner.instance_.tRex.setDuck(!1),Runner.instance_.tRex.jumping||Runner.instance_.tRex.ducking||(Runner.instance_.playSound(Runner.instance_.soundFx.BUTTON_PRESS),Runner.instance_.tRex.startJump(Runner.instance_.currentSpeed)
    )}
function duck(){Runner.instance_.tRex.jumping?Runner.instance_.tRex.setSpeedDrop():Runner.instance_.tRex.jumping||Runner.instance_.tRex.ducking||Runner.instance_.tRex.setDuck(!0)}setInterval(function(){
    Runner.instance_.horizon.obstacles.length>0&&(Runner.instance_.horizon.obstacles[0].xPos<25*Runner.instance_.currentSpeed-Runner.instance_.horizon.obstacles[0].width/2&&Runner.instance_.horizon.obstacles[0].yPos>75&&jump(),Runner.instance_.horizon.obstacles[0].xPos<30*Runner.instance_.currentSpeed-Runner.instance_.horizon.obstacles[0].width/2&&Runner.instance_.horizon.obstacles[0].yPos<=75&&duck())},5);

/*Could not hack, made a bot instead.
Usage steps:
1.	Open dinosaur game
2.	Ctrl + shift + c or f12 or ctrl + I
3.	Go to the console option
4.	paste the following code:
5.	function jump(){
    Runner.instance_.tRex.setDuck(!1),Runner.instance_.tRex.jumping||Runner.instance_.tRex.ducking||(Runner.instance_.playSound(Runner.instance_.soundFx.BUTTON_PRESS),Runner.instance_.tRex.startJump(Runner.instance_.currentSpeed)
    )}
function duck(){Runner.instance_.tRex.jumping?Runner.instance_.tRex.setSpeedDrop():Runner.instance_.tRex.jumping||Runner.instance_.tRex.ducking||Runner.instance_.tRex.setDuck(!0)}setInterval(function(){
    Runner.instance_.horizon.obstacles.length>0&&(Runner.instance_.horizon.obstacles[0].xPos<25*Runner.instance_.currentSpeed-Runner.instance_.horizon.obstacles[0].width/2&&Runner.instance_.horizon.obstacles[0].yPos>75&&jump(),Runner.instance_.horizon.obstacles[0].xPos<30*Runner.instance_.currentSpeed-Runner.instance_.horizon.obstacles[0].width/2&&Runner.instance_.horizon.obstacles[0].yPos<=75&&duck())},5);
6.	Start the game
*/