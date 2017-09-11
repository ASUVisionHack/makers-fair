import Leap
import thread


class JoyListener(Leap.Listener):
    def __init__(self, method):
        super(JoyListener, self).__init__()
        self.method = method

    def on_init(self, controller):
        print('Initialized Controller')

    def on_exit(self, controller):
        print('Exiting Controller')

    def on_connect(self, controller):
        print('Connected')

    def on_disconnect(self, controller):
        print('Disconnect')

    def on_frame(self, controller):
        frame = controller.frame()
        # ibox = frame.hand

        for hand in frame.hands:
            norm = hand.stabilized_palm_position

            # print(norm)

            self.method(norm)


def get_virtual_joystick(method):
    listener = JoyListener(method)
    controller = Leap.Controller()
    controller.add_listener(listener)

    return controller, listener