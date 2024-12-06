from manim import *

class SuperpositionOfWaves(Scene):
    def construct(self):
        # Step 1: Set up the axes
        axes_top = Axes(
            x_range=[0, 4 * PI, PI / 2],
            y_range=[-2, 2, 0.5],
            axis_config={"include_numbers": False},
        ).to_edge(UP*2)
        axes_center = Axes(
            x_range=[0, 4 * PI, PI / 2],
            y_range=[-2, 2, 0.5],
            axis_config={"include_numbers": False},
        )
        axes_bottom = Axes(
            x_range=[0, 4 * PI, PI / 2],
            y_range=[-2, 2, 0.5],
            axis_config={"include_numbers": False},
        ).to_edge(DOWN*2)

        # Step 2: Define wave functions
        wave1_func = lambda x: np.sin(x)
        wave2_func = lambda x: 0.5 * np.sin(2 * x)+ np.sin(2*x+PI)
        superposition1_func = lambda x: np.sin(x) + 0.5 * np.sin(2 * x)
        wave3_func = lambda x: 0.3 * np.sin(3.1 * x+PI/2)+0.7*np.cos(1.1*x)
        final_superposition_func = lambda x: np.sin(x) + 0.5 * np.sin(2 * x) + 0.3 * np.sin(3 * x)

        # Step 3: Plot initial waves
        wave1 = axes_top.plot(wave1_func, color=BLUE)
        wave1_label = MathTex("y = \\sin(x)").next_to(axes_top, UP)
        wave2 = axes_bottom.plot(wave2_func, color=GREEN)
        wave2_label = MathTex("y = 0.5\\sin(2x)+\\sin(2x+\\pi)").next_to(axes_bottom, DOWN)

        # Step 4: Animate initial waves appearing
        self.play(Create(axes_top), Create(wave1), Write(wave1_label))
        self.wait(1)
        self.play(Create(axes_bottom), Create(wave2), Write(wave2_label))
        self.wait(1)

        # Step 5: Shift wave1 to center, remove wave2
        self.play(Transform(axes_top, axes_center), Transform(wave1, axes_center.plot(wave1_func)), FadeOut(axes_bottom), FadeOut(wave2), FadeOut(wave2_label))
        self.wait(1)

        # Step 6: Plot wave2 on the center axis
        new_wave2 = axes_center.plot(wave2_func, color=GREEN)
        self.play(Create(new_wave2))
        self.wait(1)

        # Step 7: Transform wave1 into superposition1
        superposition1 = axes_center.plot(superposition1_func, color=PURPLE)
        self.play(Transform(wave1, superposition1), FadeOut(new_wave2))
        self.wait(1)

        # Step 8: Move superposition1 up, bring wave3 below
        self.play(Transform(axes_center, axes_top), Transform(wave1, axes_top.plot(superposition1_func, color=PURPLE)))
        wave3 = axes_bottom.plot(wave3_func, color=ORANGE)
        wave3_label = MathTex("y = 0.3\\sin(3x)+0.7\\cos(1.1+\\pi/2)").next_to(axes_bottom, DOWN)
        self.play(Create(axes_bottom), Create(wave3), Write(wave3_label))
        self.wait(1)

        # Step 9: Bring wave3 to center, remove bottom axis
        self.play(Transform(axes_bottom, axes_center), Transform(wave3, axes_center.plot(wave3_func, color=ORANGE)), FadeOut(axes_top), FadeOut(wave1), FadeOut(wave1_label))
        self.wait(1)

        # Step 10: Transform superposition1 into final superposition
        final_superposition = axes_center.plot(final_superposition_func, color=RED)
        self.play(Transform(superposition1, final_superposition), FadeOut(wave3), FadeOut(wave3_label))
        self.wait(2)

        # Step 11: Move final superposition back to top
        self.play(Transform(axes_center, axes_top), Transform(superposition1, axes_top.plot(final_superposition_func, color=RED)))
        self.wait(2)

        # Clear everything
        self.play(FadeOut(superposition1), FadeOut(axes_top))

        self.play(FadeOut(axes_bottom),FadeOut(axes_center))
        fourier_img = ImageMobject("Fourier.jpg").scale(0.7).to_edge(ORIGIN)
        fourier_text = Text("Joseph Fourier").scale(0.7).next_to(fourier_img, DOWN, buff=0.5)

        self.play(Write(fourier_text))
        self.play(FadeIn(fourier_img))

