from manim import *

class PhilosophyProject(Scene):
    def construct(self):
        title = Tex(r"Artificial Intelligence, Negligence, and Elephants")
        sub_title = Tex(r"A Cautionary (Convoluted) Tale").scale(0.7)
        title_group = VGroup(title, sub_title).arrange(DOWN)
        self.play(
            Write(title_group),
        )
        self.wait(3)

        date_title = Tex(r"November 2022")

        self.play(
            Transform(title_group, date_title)
        )

        self.wait()

        company_title = Tex(r"OpenAI")

        self.play(
            Transform(title_group, company_title)
        )

        self.wait()

        model_title = Tex(r"ChatGPT")

        self.play(
            Transform(title_group, model_title)
        )

        self.wait()

        model_title.to_corner(UP + LEFT)

        self.play(
            Transform(title_group, model_title)
        )

        self.wait()

        intelligent = ImageMobject("assets/intelligent.jpg").scale(1.5)
        accuracy = ImageMobject("assets/accuracy.jpg").scale(1.5)
        quality = ImageMobject("assets/quality.jpg").scale(1.5)
        speedometer = ImageMobject("assets/speedometer.jpg").scale(2.5)

        group = Group(intelligent, accuracy, quality).arrange(RIGHT, buff=1)


        for img in (intelligent, accuracy, quality):
            img.set_opacity(0)

        self.add(group)

        self.play(intelligent.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.play(accuracy.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.play(quality.animate.set_opacity(1), run_time=1)
        self.wait(0.5)

        self.wait(1)

        self.play(FadeIn(speedometer))

        self.wait(2)

        self.play(FadeOut(title_group))
        self.play(FadeOut(speedometer))
        self.play(intelligent.animate.set_opacity(0), run_time=0.2)
        self.play(accuracy.animate.set_opacity(0), run_time=0.2)
        self.play(quality.animate.set_opacity(0), run_time=0.2)

        self.wait()

        title = Tex(r"Totally a joke ;)")

        self.play(
            Write(title)
        )

        self.wait()

        self.play(
            FadeOut(title)
        )

        prompt = Tex(r'Prompt:')
        prompt.to_corner(UP + LEFT)
        the_prompt = Tex(r'"Write a 5,000 word essay on \\ the history of paper salt packets"')

        self.play(
            Write(prompt),
            Write(the_prompt)
        )

        self.wait()

        self.play(
            FadeOut(prompt),
            FadeOut(the_prompt)
        )

        student = ImageMobject("assets/student.jpg").scale(2.5)
        company = ImageMobject("assets/company.jpg").scale(2.5)
        teacher = ImageMobject("assets/teacher.jpg").scale(2.5)
        formula = ImageMobject("assets/formula.png")


        self.play(
            FadeIn(student)
        )

        self.wait()

        self.play(
            FadeIn(company),
            FadeOut(student)
        )

        self.wait()

        self.play(
            FadeIn(teacher),
            FadeOut(company)
        )

        self.wait()

        self.play(
            FadeOut(teacher)
        )

        formula.to_edge(DOWN)
        formula.shift(RIGHT * 12)

        self.play(formula.animate.shift(LEFT*13))
        self.play(formula.animate.shift(RIGHT*2))
        self.play(formula.animate.shift(LEFT*30))

        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[-1, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": False}
        )

        graph = axes.plot(lambda x: x**2, color=BLUE)

        self.play(Create(axes))
        self.play(Create(graph))
        self.wait()

        self.clear()

        karen = ImageMobject("assets/karen.jpg").scale(2.5)

        self.play(
            FadeIn(karen)
        )

        self.wait()

        self.play(
            FadeOut(karen)
        )

        whats_bad = Tex(r"What's actually so bad about this?")
        whats_bad.to_edge(UP)

        self.play(
            Write(whats_bad)
        )

        just_say = ImageMobject("assets/just_say.jpg").scale(3)

        self.play(
            FadeIn(just_say)
        )

        self.wait()

        smurf = ImageMobject("assets/smurf.jpg").scale(3)

        self.play(
            FadeIn(smurf),
            FadeOut(just_say)
        )

        self.wait()

        teachers_text = Tex(r"Teachers").to_edge(LEFT)
        equals = Tex(r"=")
        things_teachers_hate_1 = Tex(r"Hating the student.")
        things_teachers_hate_2 = Tex(r"Spend hours on homework.")
        group = Group(things_teachers_hate_1, things_teachers_hate_2).arrange(DOWN)
        group.to_edge(RIGHT)

        self.play(
            FadeOut(smurf),
            Write(teachers_text)
        )

        self.play(
            Write(equals)
        )

        self.play(
            Write(things_teachers_hate_1)
        )

        self.play(
            Write(things_teachers_hate_2)
        )

        not_equals = MathTex(r"\neq")

        self.play(
            Transform(equals, not_equals)
        )

        self.wait()

        bulb = ImageMobject("assets/broken_bulb.jpg").scale(3)

        self.clear()

        self.play(
            FadeIn(bulb)
        )

        self.wait()

        self.play(
            FadeOut(bulb)
        )

        transform_title = Tex("Several Blind Children")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Write(transform_title)
        )
        
        self.wait()

        children = ImageMobject("assets/children.jpg")
        children.scale(3)
        self.play(
            FadeIn(children)
        )

        self.wait()

        elephant = ImageMobject("assets/elephant.jpg").scale(3)

        elephant.scale(0.1)
        elephant.rotate(PI)   # upside‑down start (optional)
        elephant.move_to(ORIGIN)

        self.add(elephant)

        # Animate growth + spin
        self.play(
            elephant.animate.scale(15).rotate(-PI),
            run_time=2,
            rate_func=smooth
        )

        self.wait()

        self.clear()

        blind_men = ImageMobject("assets/blind_men.jpg").scale(3)

        self.play(
            FadeIn(blind_men)
        )

