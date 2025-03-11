from panda3d.core import Point3, Texture
from panda3d.gui import OnscreenText
from panda3d.physics import ForceNode, LinearVectorForce
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        # Initialize the ShowBase (this gives us access to Panda3D's features)
        super().__init__()

        # Set up a 3D object (a cube)
        self.cube = self.loader.loadModel("models/box")  # You can use your own model file here
        self.cube.reparentTo(self.render)  # Attach the cube to the scene graph
        self.cube.setScale(2, 2, 2)  # Scale the cube
        self.cube.setPos(0, 10, 0)  # Position the cube in the scene

        # Load a texture for the cube
        texture = self.loader.loadTexture("textures/your_texture.png")  # Use a valid texture path
        self.cube.setTexture(texture)

        # Set up the camera position
        self.cam.setPos(0, -15, 5)  # Position the camera so we can see the cube
        self.cam.lookAt(self.cube)  # Make the camera look at the cube

        # Set up the control keys to move the camera
        self.accept("arrow_left", self.move_camera_left)
        self.accept("arrow_right", self.move_camera_right)
        self.accept("arrow_up", self.move_camera_forward)
        self.accept("arrow_down", self.move_camera_backward)

        # Add some text to display instructions
        self.instructions = OnscreenText(text="Use Arrow Keys to Move Camera", pos=(0.8, -0.8), scale=0.1)

    def move_camera_left(self):
        self.cam.setX(self.cam.getX() - 1)

    def move_camera_right(self):
        self.cam.setX(self.cam.getX() + 1)

    def move_camera_forward(self):
        self.cam.setY(self.cam.getY() + 1)

    def move_camera_backward(self):
        self.cam.setY(self.cam.getY() - 1)

# Run the game
app = MyApp()
app.run()
