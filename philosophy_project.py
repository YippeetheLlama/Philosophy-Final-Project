from manim import *

class PhilosophyProject(Scene):
    def construct(self):
        title = Tex(r"Artificial Intelligence, Negligence, and Elephants")
        sub_title = Tex(r"A Cautionary (Convoluted) Tale").scale(0.7)
        title_group = VGroup(title, sub_title).arrange(DOWN)
        self.play(
            Write(title_group),
        )
        self.wait(7)

        date_title = Tex(r"November 2022")

        self.play(
            Transform(title_group, date_title)
        )

        self.wait(4)

        company_title = Tex(r"OpenAI")

        self.play(
            Transform(title_group, company_title)
        )

        self.wait(10)

        model_title = Tex(r"ChatGPT")

        self.play(
            Transform(title_group, model_title)
        )

        self.wait(2)

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

        self.wait(12)

        self.play(FadeIn(speedometer))

        self.wait(4)

        self.play(FadeOut(title_group))
        self.play(FadeOut(speedometer))
        self.play(intelligent.animate.set_opacity(0), run_time=0.2)
        self.play(accuracy.animate.set_opacity(0), run_time=0.2)
        self.play(quality.animate.set_opacity(0), run_time=0.2)

        self.wait(3)

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

        self.wait(20)

        self.play(
            FadeOut(prompt),
            FadeOut(the_prompt)
        )

        self.wait(13)

        student = ImageMobject("assets/student.jpg").scale(2.5)
        company = ImageMobject("assets/company.jpg").scale(2.5)
        teacher = ImageMobject("assets/teacher.jpg").scale(2.5)
        formula = ImageMobject("assets/formula.png")


        self.play(
            FadeIn(student)
        )

        self.wait(2)

        self.play(
            FadeIn(company),
            FadeOut(student)
        )

        self.wait(2)

        self.play(
            FadeIn(teacher),
            FadeOut(company)
        )

        self.wait(1)

        self.play(
            FadeOut(teacher)
        )

        formula.to_edge(DOWN)
        formula.shift(RIGHT * 12)

        self.play(formula.animate.shift(LEFT*13))
        self.play(formula.animate.shift(RIGHT*2))
        self.play(formula.animate.shift(LEFT*30))

        self.wait(13)

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

        self.wait(5)

        self.clear()

        self.wait(9)

        karen = ImageMobject("assets/karen.jpg").scale(2.5)

        self.play(
            FadeIn(karen)
        )

        self.play(
            FadeOut(karen)
        )

        whats_bad = Tex(r"What's actually so bad about this?")
        whats_bad.to_edge(UP)

        self.play(
            Write(whats_bad)
        )

        self.wait(9)

        just_say = ImageMobject("assets/just_say.jpg").scale(3)

        self.play(
            FadeIn(just_say)
        )

        self.wait(19)

        smurf = ImageMobject("assets/smurf.jpg").scale(3)

        self.play(
            FadeIn(smurf),
            FadeOut(just_say)
        )

        self.wait(21)

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

        self.wait(4)

        self.play(
            Transform(equals, not_equals)
        )

        self.wait(3)

        bulb = ImageMobject("assets/broken_bulb.jpg").scale(3)

        self.clear()

        self.wait(2)

        self.play(
            FadeIn(bulb)
        )

        self.wait(30)

        self.play(
            FadeOut(bulb)
        )

        self.wait(20)

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

        self.wait(12)

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

        self.wait(30)

        self.clear()

        blind_men = ImageMobject("assets/blind_men.jpg").scale(3)

        self.play(
            FadeIn(blind_men)
        )

        self.wait(70)

        crushed = ImageMobject("assets/crushed.jpg").scale(3)
        scared = ImageMobject("assets/scared.jpg").scale(3)
        kill_elephant = ImageMobject("assets/kill_elephant.png")

        self.play(
            FadeIn(crushed),
            FadeOut(blind_men)
        )

        self.wait(5)

        self.play(
            FadeIn(scared),
            FadeOut(crushed)
        )

        self.wait(5)

        self.play(
            FadeIn(kill_elephant),
            FadeOut(scared)
        )

        self.wait(5)

        self.play(
            FadeIn(blind_men),
            FadeOut(kill_elephant)
        )

        self.wait(10)

        self.play(FadeOut(blind_men))

        self.wait()

        point = Tex(r"So, what's the point?")

        self.play(
            Write(point)
        )

        self.wait(19)

        self.play(point.animate.to_edge(UP))

        errors = ImageMobject("assets/errors.jpg").scale(3)

        self.play(
            FadeIn(errors)
        )

        self.wait(11)

        akinator = ImageMobject("assets/akinator.jpg").scale(2.5)

        self.play(
            FadeIn(akinator),
            FadeOut(errors)
        )

        self.wait(15)

        mime = ImageMobject("assets/mime.jpg").scale(3)

        self.play(FadeOut(akinator))
        self.wait()
        self.play(FadeIn(mime))
        self.wait(10)
        self.play(FadeOut(mime))
        self.wait(16)

        cross = ImageMobject("assets/cross.jpg").scale(3)

        self.play(FadeIn(cross))

        self.wait(8)
        self.play(FadeOut(cross), FadeOut(point))
        self.wait(2)

        thanks = Tex(r'Thanks for putting up \\ with us professor :)')

        self.play(
            Write(thanks)
        )

        self.wait(2)