from manim import *

class PhilosophyProject(Scene):
    def construct(self):
        title = Tex(r"Artificial Intelligence, Negligence, and Elephants")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title),
        )
        self.wait()

        transform_title = Tex("Six blind men and an elephant")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )
        
        self.wait()

        blind_men = ImageMobject("assets/blind_men.jpg")
        blind_men.scale(3)
        self.play(
            FadeIn(blind_men)
        )

        self.wait()

