import drawable.Image


class Object:
    def __init__(self, tag, image):
        self.tag = tag
        if isinstance(image, drawable.Image):
            self.img = image
        elif isinstance(image, str):
            self.img = drawable.Image(tag + "Image", image)

    def render(self, window, position):
        window.blit(self.img.image, position)