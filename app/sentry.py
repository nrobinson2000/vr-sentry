from threading import Timer
from pantilthat import PanTilt

MAX_ANGLE = 90
MIN_ANGLE = -90

STEP_SIZE = 20
BRIGHTNESS_LEVEL = 200

def constrain_angle(angle):
    return min(MAX_ANGLE, max(MIN_ANGLE, angle))

class Sentry:
    def __init__(self):
        self.light_state = False
        self.last_timer = Timer(30, self.light_off)
        self.hat = PanTilt()
        self.pan_angle = 0
        self.tilt_angle = 90
        self.move_auto()
    
    def move_auto(self):
        self.move(self.pan_angle, self.tilt_angle)
    
    def move(self, pan, tilt):
        self.pan_angle = constrain_angle(pan)
        self.tilt_angle = constrain_angle(tilt)
        self.hat.pan(self.pan_angle)
        self.hat.tilt(self.tilt_angle)

    def up(self):
        self.tilt_angle -= STEP_SIZE
        self.move_auto()
    
    def down(self):
        self.tilt_angle += STEP_SIZE
        self.move_auto()
    
    def left(self):
        self.pan_angle += STEP_SIZE
        self.move_auto()

    def right(self):
        self.pan_angle -= STEP_SIZE
        self.move_auto()

    def light_color(self, red, green, blue):
        self.hat.set_all(green,red,blue)
        self.hat.show()
    
    def light_on(self, r=BRIGHTNESS_LEVEL, g=BRIGHTNESS_LEVEL, b=BRIGHTNESS_LEVEL):
        self.light_color(r,g,b)
        self.light_state = True
        self.last_timer.cancel()
        off_timer = Timer(30, self.light_off)
        off_timer.start()
        self.last_timer = off_timer

    def light_off(self):
        self.light_color(0,0,0)
        self.light_state = False

    def toggle_light(self):
        if self.light_state is False:
            self.light_on()
        else:
            self.light_off()

sentry = Sentry()

