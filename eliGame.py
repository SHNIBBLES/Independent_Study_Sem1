#!/usr/bin/env python3


import cocos
class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label(
            "Hello, World",
            font_name = "Times New Roman",
            font_size = 32,
            anchor_x="left", anchor_y="bottom"
        )
        label.position = 0, 0
        self.add(label)
cocos.director.director.init()
text_layer = HelloWorld()
main_scene = cocos.scene.Scene (text_layer)
cocos.director.director.run(main_scene)
