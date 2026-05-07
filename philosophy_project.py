from manim import *

class PhilosophyProject(Scene):
    def construct(self):
        title = Tex(r"Artificial Intelligence, Negligence, and Elephants")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title),
        )
        self.wait(3)

        date_title = Tex(r"November 2022")

        self.play(
            Transform(title, date_title)
        )

        self.wait()

        company_title = Tex(r"OpenAI")

        self.play(
            Transform(title, company_title)
        )

        self.wait()

        model_title = Tex(r"ChatGPT")

        self.play(
            Transform(title, model_title)
        )

        self.wait()

        model_title.to_corner(UP + LEFT)

        self.play(
            Transform(title, model_title)
        )

        self.wait()

        intelligent = ImageMobject("assets/intelligent.jpg").scale(1.5)
        accuracy = ImageMobject("assets/accuracy.jpg").scale(1.5)
        quality = ImageMobject("assets/quality.jpg").scale(1.5)

        group = Group(intelligent, accuracy, quality).arrange(RIGHT, buff=1)

        # Start invisible
        for img in (intelligent, accuracy, quality):
            img.set_opacity(0)

        self.add(group)

        # Fade them in one at a time (OpenGL-safe)
        self.play(intelligent.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.play(accuracy.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.play(quality.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.wait(1)

        self.play(intelligent.animate.set_opacity(0), run_time=0.2)
        self.play(accuracy.animate.set_opacity(0), run_time=0.2)
        self.play(quality.animate.set_opacity(0), run_time=0.2)



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

